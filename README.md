#Job Tracker API

A RESTful API built with Python to manage and track job applications.
This project allows users to create, update, delete, and monitor job applications efficiently.

#FEATURES
- Add a new job application
- Update job status (applied, interview, accepted, rejected)
- Delete a job application
- Retrieve all job applications
- REST API architecture

#TECHNOLOGIES USED
- Python 3
- Flask or FastAPI
- REST API
- JSON
- Git & GitHub

#PROJECT STRUCTURE
job-tracker-api/
- app.py
- requirements.txt
- README.txt

#INSTALLATION
1. Clone the repository:
   git clone https://github.com/Ghaniomix/job-tracker-api.git

2. Navigate to the project folder:
   cd job-tracker-api

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   python app.py

#API ENDPOINTS (EXAMPLE)
GET    /jobs        -> Get all job applications
POST   /jobs        -> Add a new job
PUT    /jobs/{id}   -> Update job status
DELETE /jobs/{id}   -> Delete a job

#EXAMPLE REQUEST (POST)
{
  "company": "Google",
  "position": "Backend Developer",
  "status": "Applied"
}

#PROJECT PURPOSE
This project was developed to practice backend development with Python
and demonstrate the use of REST APIs and application logic.

#FUTURE IMPROVEMENTS
- Database integration (SQLite / PostgreSQL)
- User authentication
- Deployment

#AUTHOR
Ghanioviç
GitHub: https://github.com/Ghaniomix
