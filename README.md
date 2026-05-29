# Job Tracker Platform

A secure Job Application Tracking Platform built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Docker.

## Features

* User Registration and Login
* JWT Authentication and Authorization
* Create Job Applications
* Update Job Applications
* Delete Job Applications
* Search Jobs by Company
* Filter Jobs by Status
* Dashboard Analytics
* Pagination Support
* PostgreSQL Database Integration
* Dockerized Deployment
* Interactive Swagger API Documentation


# Job Tracker Platform

A secure Job Application Tracking Platform built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and Docker.

## Features

- User Registration and Login
- JWT Authentication
- CRUD Operations for Jobs
- Search Jobs by Company
- Filter Jobs by Status
- Dashboard Analytics
- Pagination
- Docker Support

## Key Features

✅ JWT Authentication & Authorization

✅ Job Application CRUD Operations

✅ Search Jobs by Company

✅ Filter Jobs by Status

✅ Dashboard Analytics

✅ Pagination Support

✅ PostgreSQL Integration

✅ Docker Containerization

✅ Interactive Swagger Documentation

## Sample Analytics Response

```json
{
  "total_jobs": 25,
  "applied": 15,
  "interview": 5,
  "rejected": 3,
  "offer": 2
}

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT Authentication
* Docker
* Pydantic

## API Endpoints

### Authentication

* Register User
* Login User

### Jobs

* Create Job
* Get All Jobs
* Get Single Job
* Update Job
* Delete Job
* Search Jobs by Company
* Filter Jobs by Status

### Dashboard

* Analytics Dashboard
* Job Status Statistics

## Project Structure

```text
backend/
│
├── app/
│   ├── auth/
│   │   └── dependencies.py
│   │
│   ├── config/
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── job.py
│   │
│   ├── routes/
│   │   ├── user_routes.py
│   │   └── job_routes.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── job_schema.py
│   │
│   └── main.py
│
├── Dockerfile
├── requirements.txt
└── .gitignore
```


## Future Enhancements

* Resume Upload
* Email Notifications
* Interview Scheduling
* Job Application Reminders
* Frontend Dashboard using React
* AWS Deployment

## Author

Sumanth Nandipati
