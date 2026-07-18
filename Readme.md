# Job Application Tracker API

A backend API built with **FastAPI** for tracking job applications. Users can register, log in, create job applications, update application status, delete their own applications, and filter/search applications. Admin users can manage all users and applications.

This project is designed as a professional backend portfolio project using authentication, authorization, PostgreSQL, Alembic migrations, testing, and Docker.

---

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* JWT Authentication
* Password Hashing
* pytest
* Docker
* Docker Compose

---

## Main Features

### Authentication

* Register user
* Login user
* JWT access token
* Password hashing
* Protected routes

### User Features

* Create job application
* View own job applications
* Update own job application
* Delete own job application
* Filter applications by status
* Search applications by company or position

### Admin Features

* View all users
* View all job applications
* Delete any application
* Admin-only protected routes

---

## Project Structure

```text
job_tracker_api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── application.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── application.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── applications.py
│   │   └── admin.py
│   │   └──user.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── password.py
│   │   └── jwt_handler.py
│   │
│   └── dependencies/
│       ├── __init__.py
│       └── getcurrent_user.py
│       └──get_role.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_applications.py
│   └── test_admin.py
│
├── alembic/
├── requirements.txt
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## Environment Variables

Create a `.env` file in the root folder.

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/job_tracker_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

For Docker, the database host will be different:

```env
DATABASE_URL=postgresql://postgres:password@db:5432/job_tracker_db
```

---

## Run Locally

### 1. Create virtual environment

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
uvicorn app.main:app --reload
```

Open API docs:

```text
http://localhost:8000/docs
```

---

## Run with Docker

Make sure Docker Desktop is installed and running.

Start the project:

```bash
docker compose up --build
```

Open API docs:

```text
http://localhost:8000/docs
```

Stop containers:

```bash
docker compose down
```

---

## Database Access with Docker

PostgreSQL runs inside Docker.

From the FastAPI container, the app connects to PostgreSQL using:

```text
db:5432
```

From your local computer, PostgreSQL is exposed on:

```text
localhost:5433
```

Example connection details:

```text
Host: localhost
Port: 5433
Database: job_tracker_db
Username: postgres
Password: password
```

---

## Docker Volume

PostgreSQL data is saved in a Docker volume.

This means database data will stay saved even after running:

```bash
docker compose down
```

Do not run this unless you want to delete database data:

```bash
docker compose down -v
```

The `-v` option removes Docker volumes and deletes saved PostgreSQL data.

---

## Testing

Run tests with:

```bash
pytest
```

The project will include tests for:

* User registration
* User login
* JWT protected routes
* Creating applications
* Updating applications
* Deleting applications
* User ownership authorization
* Admin-only routes

---

## API Endpoints

### Auth Routes

```text
POST /register
POST /login
```

### Application Routes

```text
POST /user/application

```

### Admin Routes

```text
GET /admin/users
GET /admin/applications
DELETE /admin/applications/delete/{application_id}
DELETE /admin/user/delete/{application_id}

```
### user Routes

```text
GET /user/list/applications
PUT /user/application/update/{id}
DELETE /user/application/delete/{id}


```
---

## Job Application Status Examples

Applications can have statuses like:

```text
applied
interview
offer
rejected
accepted
```

---

## Goal of This Project

The goal of this project is to demonstrate real backend development skills:

* Clean FastAPI project structure
* PostgreSQL database design
* SQLAlchemy ORM relationships
* Alembic database migrations
* JWT authentication
* Role-based authorization
* API testing with pytest
* Dockerized development setup
* Professional README and GitHub-ready project

---

## Author

Built by Lakhvir as a backend portfolio project.
