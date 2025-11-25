# 💰 Expense Management System

A clean, modular full-stack application for tracking and analyzing expenses using **FastAPI**, **Streamlit**, and **MySQL**.

---

## 📸 Screenshots

<p align="center">
  <img src="./analytics_ui_demo1.png" width="600"/>
  <br><em>Analytics Dashboard</em>
</p>

<p align="center">
  <img src="./analytics_ui_demo2.png" width="600"/>
  <br><em>Analytics Graph View</em>
</p>

<p align="center">
  <img src="./app_frontend_ui.png" width="600"/>
  <br><em>Main UI – Add & View Expenses</em>
</p>

---

## 🌟 Overview
This system provides a simple UI for adding, viewing, and analyzing expenses.  
The backend handles data storage and processing using MySQL, while the frontend offers an intuitive interface built with Streamlit.

---

## 🚀 Features

### 🔧 Backend (FastAPI)
- Add / view expenses  
- MySQL integration  
- Layered logic (db helper, endpoints)  
- Logging included  

### 🎨 Frontend (Streamlit)
- Add expenses  
- Date-based search  
- Analytics dashboard  

### 🧪 Testing
- Pytest tests for DB helper  

---

## 🧩 Architecture

```
Streamlit UI  →  FastAPI Backend  →  MySQL Database
```

---

## 📂 Folder Structure

```
expense-management-system/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   ├── logging_setup.py
│
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   ├── analytics_ui.py
│
├── tests/
│   ├── backend/test_db_helper.py
│   ├── conftest.py
│
├── .env.example
├── schema.sql
├── requirements.txt
└── README.md

```

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend  | FastAPI |
| Database | MySQL |
| Testing  | Pytest |
| Language | Python 3.10+ |

---

## 📘 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/expenses/add`           | Add expense |
| GET    | `/expenses/{date}`        | Get expenses for a date |
| GET    | `/summary/{start}/{end}`  | Summary analytics |

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kaushiks-info/expense-management-system.git
cd expense-management-system
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# Windows (cmd)
venv\Scripts\activate.bat
```


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🗄️ MySQL Setup (Required)

### 4️⃣ Create Database
```sql
CREATE DATABASE expense_manager;
```

### 5️⃣ Configure Credentials
Update `.env` (copy `.env.example` first):

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASS=root
DB_NAME=expense_manager
```

---

## ▶️ Running the Application

### Backend (FastAPI)
```bash
uvicorn backend.server:app --reload
```

### Frontend (Streamlit)
```bash
streamlit run frontend/app.py
```

---

## 🧪 Testing
```bash
pytest
```

---

## 📄 License
MIT License
