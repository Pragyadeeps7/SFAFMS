# SFAFMS Backend

Backend API implementation for Smart Fuel Authorization & Fleet Monitoring System.

## Structure

```
app/
├── api/
│   ├── v1/
│   │   ├── auth.py          # Authentication endpoints
│   │   ├── vehicles.py      # Vehicle management
│   │   └── ...
│   └── deps.py              # Dependency injection
├── db/
│   ├── models/              # SQLAlchemy models
│   ├── base.py              # ORM base
│   └── session.py           # DB connection
├── repositories/            # Data access layer
├── services/                # Business logic
├── schemas/                 # Pydantic models
├── ai/anpr/                 # ANPR pipeline
├── tasks/                   # Celery async tasks
├── core/
│   ├── config.py            # Settings
│   ├── security.py          # JWT & password
│   └── middleware/          # Middlewares
└── main.py                  # FastAPI app
```

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload

# Start Celery worker
celery -A app.tasks.celery_app worker --loglevel=info

# Start Celery beat
celery -A app.tasks.celery_app beat --loglevel=info
```

## API Documentation

Available at `http://localhost:8000/api/docs`

## Database

PostgreSQL 16 with async connection pooling via SQLAlchemy 2.0

## Testing

```bash
pytest tests/ -v --cov=app
```
