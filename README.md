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

## Public routes

These endpoints do **not** require a JWT (or session) for the listed method:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | API root (links to resources and auth URLs) |
| `GET` | `/health/` | Health check |
| `GET` | `/api/events/` | List events |
| `GET` | `/api/events/{id}/` | Event detail |
| `GET` | `/api/participants/` | List participants |
| `GET` | `/api/participants/{id}/` | Participant detail |
| `POST` | `/api/token/` | Obtain JWT (body: `username`, `password`) |
| `POST` | `/api/token/refresh/` | Refresh access token (body: `refresh`) |

The Django admin login page is reachable at `GET /admin/` without API auth; using the admin UI still requires a staff/superuser account.

All other API routes (writes on events/participants, any registration route, nested registration lists) require authentication as described below.

## Authentication

Use JWT for protected requests:

- **Obtain token:** `POST /api/token/`
- **Refresh token:** `POST /api/token/refresh/`

Include the access token on protected requests:

```http
Authorization: Bearer <access_token>
```

- **Events & participants:** `create`, `update`, and `destroy` require an authenticated user; `list` and `retrieve` are public (see table above).
- **Registrations** (`/api/registrations/…`): all methods require an **admin** user (`IsAdminUser`).
- **Nested lists** `GET /api/events/{id}/registrations/` and `GET /api/participants/{id}/registrations/` require an authenticated user (default DRF permission).

Participant payload variant: add `?version=v2` to participant endpoints when supported.

## Main endpoints

Base URL for CRUD resources: **`/api/`** (router uses trailing slashes).

### Events

- `GET /api/events/`
- `POST /api/events/`
- `GET /api/events/{id}/`
- `PUT /api/events/{id}/`
- `PATCH /api/events/{id}/`
- `DELETE /api/events/{id}/`
- `GET /api/events/{id}/registrations/`

### Participants

- `GET /api/participants/`
- `POST /api/participants/`
- `GET /api/participants/{id}/`
- `PUT /api/participants/{id}/`
- `PATCH /api/participants/{id}/`
- `DELETE /api/participants/{id}/`
- `GET /api/participants/{id}/registrations/`

### Registrations (admin only)

- `GET /api/registrations/`
- `POST /api/registrations/`
- `GET /api/registrations/{id}/`
- `PUT /api/registrations/{id}/`
- `PATCH /api/registrations/{id}/`
- `DELETE /api/registrations/{id}/`

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
