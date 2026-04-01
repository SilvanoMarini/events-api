# Events API

A REST API for managing events, participants, and registrations, providing CRUD operations and user authentication.

## 🚀 Technologies

### Backend
- Python
- Django
- Django REST Framework

### Authentication
- JWT Authentication

## 🚧 In Progress

### Database
- PostgreSQL

### DevOps
- Docker
- Docker Compose


## Features

- Manage events (CRUD operations)
- Manage participants
- Handle event registrations
- Authenticate users


## Installation

1. Clone the repository:
  ```bash
  git clone https://github.com/SilvanoMarini/events-api.git
  ```

2. Navigate to the project directory:
  ```bash 
  cd events-api
  ```

3. Create and activate a virtual environment:
  ```bash
  python -m venv venv

  # Linux/macOS
  source venv/bin/activate

  # Windows
  venv\Scripts\activate
  ```

4. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

5. Apply database migrations:
  ```bash
  python manage.py migrate
  ```

6. Run the development server:
  ```bash
  python manage.py runserver
  ``` 


## API Endpoints

### Events  

- GET /events → List all events
- POST /events → Create a new event
- GET /events/{id} → Retrieve a specific event
- PUT /events/{id} → Update an event
- DELETE /events/{id} → Delete an event

### Participants

- GET /participants → List all participants
- POST /participants → Create a new participant 

### Registrations

- GET /registrations → List all registrations
- POST /registrations → Create a new registration

### Authentication

- POST /auth/login → Authenticate user and return JWT token

### Example Request

```json
{
  "title": "Tech Conference",
  "description": "Annual tech event",
  "date": "2026-01-01",
  "location": "São Paulo"
}
