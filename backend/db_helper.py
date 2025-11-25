import os
from contextlib import contextmanager
from logging_setup import setup_logger

try:
    # prefer python-dotenv if installed
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

logger = setup_logger('db_helper')

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "root")
DB_NAME = os.getenv("DB_NAME", "expense_manager")
DB_PORT = int(os.getenv("DB_PORT", os.getenv("PORT", 3306)) or 3306)

import mysql.connector

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        port=DB_PORT
    )
    cursor = connection.cursor(dictionary=True)
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()


def add_expense(amount, category, notes, expense_date):
    query = \"\"\"
    INSERT INTO expenses (amount, category, notes, expense_date)
    VALUES (%s, %s, %s, %s)
    \"\"\"
    with get_db_cursor(commit=True) as cur:
        cur.execute(query, (amount, category, notes, expense_date))
        logger.info("Added expense: %s %s", amount, category)


def fetch_expenses_for_date(expense_date):
    query = \"\"\"
    SELECT id, amount, category, notes, expense_date
    FROM expenses
    WHERE expense_date = %s
    \"\"\"
    with get_db_cursor() as cur:
        cur.execute(query, (expense_date,))
        rows = cur.fetchall()
        return rows


def delete_expenses_for_date(expense_date):
    query = \"\"\"
    DELETE FROM expenses
    WHERE expense_date = %s
    \"\"\"
    with get_db_cursor(commit=True) as cur:
        cur.execute(query, (expense_date,))
        logger.info("Deleted expenses for date: %s", expense_date)


def fetch_expense_summary(start_date, end_date):
    query = \"\"\"
    SELECT category, SUM(amount) as total
    FROM expenses
    WHERE expense_date BETWEEN %s AND %s
    GROUP BY category
    \"\"\"
    with get_db_cursor() as cur:
        cur.execute(query, (start_date, end_date))
        data = cur.fetchall()

    if not data:
        return []

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total'] / total) * 100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown


if __name__ == "__main__":
    # small manual test (won't run during import)
    print(fetch_expenses_for_date("2024-09-30"))
