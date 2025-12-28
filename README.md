# Job Tracker API

A simple and clean **REST API** for tracking job applications, built with **FastAPI**, **SQLModel**, and **SQLite**.  
It provides full CRUD operations and auto-generated interactive documentation (Swagger UI).

---

## ✨ Features

- Create a job application
- List all applications
- Get an application by ID
- Update an application
- Delete an application
- Persistent storage using SQLite

---

## 🧰 Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

---

## 📁 Project Structure

job-tracker-api/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI app entrypoint
│ ├── db.py # Database engine/session setup
│ └── models.py # SQLModel models
├── .gitignore
├── README.md
└── job_tracker.db # created at runtime (ignored by git)


---

## 🔌 API Endpoints

| Method | Endpoint                 | Description               |
|------:|---------------------------|---------------------------|
| POST  | `/applications`           | Create an application     |
| GET   | `/applications`           | List all applications     |
| GET   | `/applications/{id}`      | Get an application by ID  |
| PUT   | `/applications/{id}`      | Update an application     |
| DELETE| `/applications/{id}`      | Delete an application     |

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.10+ recommended

### Installation

1) Clone the repository: 
git clone https://github.com/Ghaniomix/Job-tracker-api.git
cd Job-tracker-api

2) Create and activate a virtual environment:
python -m venv .venv

# Windows:
.venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

Install dependencies:
Option A (recommended): if you add a requirements.txt
pip install -r requirements.txt
Option B: install manually
pip install fastapi "uvicorn[standard]" sqlmodel
Run the API
uvicorn app.main:app --reload
API base URL:
http://127.0.0.1:8000
Interactive Docs:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

Example (Create Application)
The request fields depend on your SQLModel schema in app/models.py.
curl -X POST "http://127.0.0.1:8000/applications" \
  -H "Content-Type: application/json" \
  -d '{"company":"Acme","position":"Backend Developer","status":"applied"}'
🧭 Roadmap
Add pagination & filtering for GET /applications
Improve validation & error handling
Add tests with pytest
Add CI with GitHub Actions
Deploy the API (Render / Railway / Fly.io)
Optional: Docker support
