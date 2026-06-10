# Smart Fuel Authorization & Fleet Monitoring System (SFAFMS)

A comprehensive, production-grade solution for fuel authorization, fleet monitoring, and ANPR-based vehicle tracking.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose 20.10+
- Python 3.12
- Node.js 20+

### Development Setup

```bash
git clone https://github.com/Pragyadeeps7/SFAFMS.git
cd SFAFMS
cp .env.example .env
docker-compose up -d
docker-compose exec backend alembic upgrade head
```

**Access:**
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs
- Frontend: http://localhost:3000
- MinIO: http://localhost:9001

## 📋 Tech Stack

- **Backend**: FastAPI + SQLAlchemy + Async Celery
- **Frontend**: Next.js 15 + React 19 + TypeScript
- **Database**: PostgreSQL 16
- **Cache**: Redis 7
- **AI/ML**: YOLOv8 + EasyOCR
- **Infra**: Kubernetes, Docker, Nginx

## 🔐 Key Features

- Multi-tenant RBAC architecture
- Real-time ANPR with YOLOv8
- Fuel authorization engine with consumption limits
- Automated video recording & retention
- JWT authentication (15min access + 7day refresh)
- Audit logging on all data changes
- Production-ready with comprehensive tests

## 📁 Structure

```
SFAFMS/
├── backend/          # FastAPI application
├── frontend/         # Next.js application
├── infrastructure/   # Docker, K8s, monitoring
├── docs/            # Technical blueprint
└── docker-compose.yml
```

## 📚 Documentation

See `docs/TECHNICAL_BLUEPRINT.md` for complete architecture details.

## 📝 License

Fabulus Graphic Private Limited © 2025
