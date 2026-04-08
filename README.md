# Events API

REST API for managing events, participants, and registrations, with JWT authentication.

## Technologies

- Python 3
- Django
- Django REST Framework
- django-filter
- Simple JWT
- PostgreSQL

## Features

- Full CRUD for events
- Full CRUD for participants
- Registration CRUD with event capacity control
- Endpoints to list registrations by event and by participant
- JWT authentication (`access` and `refresh`)
- Search, ordering, and pagination on main endpoints
- Alternative participant serializer via query parameter (`?version=v2`)

## Requirements

- Python 3.11+ (recommended)
- `pip`
- `.env` file with required variables

## Environment variables

Use `.env.example` as a base:

```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=your-database-url
ALLOWED_HOSTS=127.0.0.1,localhost
```

Local SQLite example:

```env
DATABASE_URL=sqlite:///db.sqlite3
```

## Installation and run

1. Clone the repository:
   ```bash
   git clone https://github.com/SilvanoMarini/events-api.git
   cd events-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   ```

   Linux/macOS:
   ```bash
   source .venv/bin/activate
   ```

   Windows (PowerShell):
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure `.env`:
   ```bash
   cp .env.example .env
   ```
   Windows (PowerShell):
   ```powershell
   Copy-Item .env.example .env
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Authentication

All API endpoints require an authenticated user by default.

- Obtain token:
  - `POST /api/token/`
- Refresh token:
  - `POST /api/token/refresh/`

Include the token in requests:

```http
Authorization: Bearer <access_token>
```

## Main endpoints

`ModelViewSet` routes use trailing slashes (`/`).

### Events

- `GET /events/`
- `POST /events/`
- `GET /events/{id}/`
- `PUT /events/{id}/`
- `PATCH /events/{id}/`
- `DELETE /events/{id}/`
- `GET /events/{id}/registrations`

### Participants

- `GET /participants/`
- `POST /participants/`
- `GET /participants/{id}/`
- `PUT /participants/{id}/`
- `PATCH /participants/{id}/`
- `DELETE /participants/{id}/`
- `GET /participants/{id}/registrations`

### Registrations

- `GET /registrations/`
- `POST /registrations/`
- `GET /registrations/{id}/`
- `PUT /registrations/{id}/`
- `PATCH /registrations/{id}/`
- `DELETE /registrations/{id}/`

Note: registration operations require admin permissions.

## Payload examples

### Create event

```json
{
  "name": "Tech Conference 2026",
  "description": "Annual event about technology and innovation.",
  "date": "2026-10-20T19:00:00-03:00",
  "location": "Sao Paulo",
  "capacity": 200
}
```

### Create participant

```json
{
  "name": "Maria Silva",
  "cpf": "123.456.789-09",
  "email": "maria@example.com",
  "phone": "+55 11 99999-9999"
}
```

### Create registration

```json
{
  "event": 1,
  "participant": 1
}
```
