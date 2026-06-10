# Infrastructure

Deployment configurations and infrastructure setup for SFAFMS.

## Components

### Docker Compose (Development)

```bash
docker-compose up -d
```

Starts:
- PostgreSQL 16
- Redis 7
- MinIO (S3-compatible)
- Backend (FastAPI)
- Frontend (Next.js)
- Celery Worker & Beat
- Nginx

### Kubernetes (Production)

```bash
# Create namespace and secrets
kubectl apply -f k8s/namespace.yaml

# Deploy backend
kubectl apply -f k8s/backend-deployment.yaml

# Deploy frontend
kubectl apply -f k8s/frontend-deployment.yaml

# Deploy database
kubectl apply -f k8s/postgres-statefulset.yaml
kubectl apply -f k8s/redis-deployment.yaml

# Configure ingress
kubectl apply -f k8s/nginx-ingress.yaml
```

### Services

#### PostgreSQL
- Version: 16
- Storage: Persistent Volume
- Replicas: 1 (StatefulSet)

#### Redis
- Version: 7
- Use: Sessions, Celery queue
- Persistence: AOF enabled

#### Backend
- Replicas: 3-10 (auto-scaling)
- Health checks: Readiness + Liveness
- Resource limits: 512Mi-1Gi memory, 250m-500m CPU

#### Frontend
- Replicas: 2-5 (auto-scaling)
- CDN-ready configuration

### Monitoring

Prometheus & Grafana ready (see `monitoring/`)

### Security

- TLS/SSL termination at Nginx
- Secrets management via Kubernetes
- Network policies for pod isolation
- RBAC for user access control

## Environment Setup

### Production Secrets

Create a `.env` file with:

```
DATABASE_URL=postgresql+asyncpg://user:pass@postgres:5432/sfafms
REDIS_URL=redis://:password@redis:6379/0
SECRET_KEY=<random-32-char-string>
REFRESH_SECRET_KEY=<random-32-char-string>
AWS_ACCESS_KEY_ID=<your-key>
AWS_SECRET_ACCESS_KEY=<your-secret>
```

Then create K8s secret:

```bash
kubectl create secret generic sfafms-secrets \
  --from-env-file=.env \
  -n sfafms
```

## Deployment Checklist

- [ ] Create namespace
- [ ] Set up secrets
- [ ] Deploy databases (PostgreSQL, Redis)
- [ ] Run migrations
- [ ] Deploy backend
- [ ] Deploy frontend
- [ ] Configure Ingress/Nginx
- [ ] Set up monitoring
- [ ] Enable auto-scaling
- [ ] Configure backup policies

## Scaling

### Horizontal Scaling
- Backend: 3-10 replicas based on CPU/Memory
- Frontend: 2-5 replicas based on CPU

### Database Scaling
- Read replicas for PostgreSQL (via RDS or similar)
- Redis Cluster for HA

## Backup & Recovery

- Database backups: Daily snapshots
- Configuration backups: Git
- Media retention: 30 days (configurable)
