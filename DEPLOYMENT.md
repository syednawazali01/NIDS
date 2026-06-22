# Deployment Guide

This guide covers deploying the Network Intrusion Detection System to production environments.

## Table of Contents

- [Local Deployment](#local-deployment)
- [Docker Deployment](#docker-deployment)
- [Cloud Deployment](#cloud-deployment)
- [Security Considerations](#security-considerations)
- [Monitoring](#monitoring)
- [Scaling](#scaling)

## Local Deployment

### System Requirements

- Python 3.7+
- 4GB RAM minimum
- 2GB free disk space
- Network connectivity

### Installation Steps

```bash
# 1. Clone repository
git clone https://github.com/syednawazali01/NIDS.git
cd NIDS

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train models (if needed)
python train_model.py

# 5. Run application
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Using Docker Directly

```bash
# Build image
docker build -t nids:latest .

# Run container
docker run -d \
  --name nids \
  -p 8501:8501 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/models:/app/models \
  nids:latest

# View logs
docker logs -f nids

# Stop container
docker stop nids
docker rm nids
```

### Docker Environment Variables

```dockerfile
# In docker-compose.yml or docker run
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
```

## Cloud Deployment

### Heroku

1. **Install Heroku CLI**
   ```bash
   curl https://cli.heroku.com/install.sh | sh
   ```

2. **Create Heroku app**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Create Procfile**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Create runtime.txt**
   ```
   python-3.10.0
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

### AWS Deployment

#### Using Elastic Container Service (ECS)

1. **Build and push Docker image to ECR**
   ```bash
   aws ecr get-login-password | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.<region>.amazonaws.com
   
   docker tag nids:latest <aws-account-id>.dkr.ecr.<region>.amazonaws.com/nids:latest
   docker push <aws-account-id>.dkr.ecr.<region>.amazonaws.com/nids:latest
   ```

2. **Create ECS task definition**
   ```json
   {
     "family": "nids",
     "containerDefinitions": [{
       "name": "nids",
       "image": "<aws-account-id>.dkr.ecr.<region>.amazonaws.com/nids:latest",
       "portMappings": [{
         "containerPort": 8501,
         "hostPort": 8501
       }],
       "memory": 2048,
       "cpu": 1024
     }]
   }
   ```

3. **Create ECS service and run**

#### Using EC2

1. **SSH into EC2 instance**
2. **Install Docker and Docker Compose**
3. **Clone repository and deploy using Docker Compose**

### Google Cloud Run

```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/PROJECT_ID/nids

# Deploy to Cloud Run
gcloud run deploy nids \
  --image gcr.io/PROJECT_ID/nids \
  --platform managed \
  --region us-central1 \
  --port 8501 \
  --memory 2Gi
```

### Azure Container Instances

```bash
az acr build --registry myregistry --image nids:latest .

az container create \
  --resource-group mygroup \
  --name nids \
  --image myregistry.azurecr.io/nids:latest \
  --ports 8501 \
  --memory 2
```

## Security Considerations

### 1. HTTPS/TLS Configuration

**Using Nginx Reverse Proxy**

```nginx
server {
    listen 443 ssl http2;
    server_name nids.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/nids.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/nids.yourdomain.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}

server {
    listen 80;
    server_name nids.yourdomain.com;
    return 301 https://$server_name$request_uri;
}
```

### 2. Authentication

**Using HTTP Basic Auth**

```nginx
location / {
    auth_basic "NIDS Administration";
    auth_basic_user_file /etc/nginx/.htpasswd;
    
    proxy_pass http://localhost:8501;
}
```

**Using OAuth2 Proxy**

```bash
docker run -d \
  --name oauth2-proxy \
  -p 4180:4180 \
  quay.io/oauth2-proxy/oauth2-proxy:v7.3.0 \
  --provider=google \
  --client-id=YOUR_CLIENT_ID \
  --client-secret=YOUR_CLIENT_SECRET
```

### 3. Network Security

```yaml
# docker-compose.yml with network isolation
version: '3.8'
services:
  nids:
    image: nids:latest
    networks:
      - private
    environment:
      STREAMLIT_SERVER_HEADLESS: "true"
    restart: on-failure

  nginx:
    image: nginx:latest
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    networks:
      - private
    restart: on-failure

networks:
  private:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

### 4. Environment Secrets

**Using Environment Variables (Docker)**

```bash
docker run -d \
  --env-file .env \
  --name nids \
  nids:latest
```

**.env file**

```
MODEL_PATH=/app/models/best_model.joblib
DATA_PATH=/app/data/
LOG_LEVEL=INFO
```

### 5. Data Protection

- Encrypt data at rest: Use EBS encryption (AWS), persistent volume encryption
- Encrypt data in transit: Use TLS/HTTPS
- Access control: Implement role-based access
- Audit logging: Monitor all access and changes

## Monitoring

### Health Checks

**Docker Health Check**

```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1
```

### Logging

**Configure Streamlit Logging**

```bash
streamlit run app.py \
  --logger.level=info \
  --logger.messageFormat="%(levelname)s [%(asctime)s]: %(message)s"
```

### Prometheus Metrics

Integrate with monitoring stack:

```bash
docker run -d \
  --name prometheus \
  -p 9090:9090 \
  -v prometheus.yml:/etc/prometheus/prometheus.yml \
  prom/prometheus
```

### Application Monitoring

```python
# app.py integration example
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

## Scaling

### Load Balancing

**Using Nginx**

```nginx
upstream nids_backend {
    server app1:8501;
    server app2:8501;
    server app3:8501;
}

server {
    listen 80;
    server_name nids.yourdomain.com;
    
    location / {
        proxy_pass http://nids_backend;
    }
}
```

### Docker Swarm

```bash
# Initialize swarm
docker swarm init

# Deploy service
docker service create \
  --name nids \
  --replicas 3 \
  -p 8501:8501 \
  nids:latest
```

### Kubernetes

**deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nids
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nids
  template:
    metadata:
      labels:
        app: nids
    spec:
      containers:
      - name: nids
        image: nids:latest
        ports:
        - containerPort: 8501
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
---
apiVersion: v1
kind: Service
metadata:
  name: nids-service
spec:
  selector:
    app: nids
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8501
  type: LoadBalancer
```

Deploy to Kubernetes:

```bash
kubectl apply -f deployment.yaml
```

## Backup and Recovery

### Database Backups

```bash
# Backup models and data
tar -czf nids-backup-$(date +%Y%m%d).tar.gz models/ data/

# Restore from backup
tar -xzf nids-backup-20260622.tar.gz
```

### Docker Volume Backups

```bash
docker run --rm \
  -v nids-data:/data \
  -v $(pwd):/backup \
  ubuntu tar czf /backup/nids-backup.tar.gz -C /data .
```

## Maintenance

### Regular Updates

```bash
# Check for updates
git pull origin main

# Rebuild Docker image
docker-compose build

# Restart services
docker-compose restart
```

### Cleanup

```bash
# Remove unused Docker images
docker image prune -a

# Remove unused Docker volumes
docker volume prune

# Clear logs
docker logs --all --clear
```

## Troubleshooting Deployment

### Port Already in Use

```bash
# Find process using port
lsof -i :8501
# or on Windows
netstat -ano | findstr :8501

# Kill process or use different port
```

### Out of Memory

Increase memory allocation:

```bash
# Docker
docker run -m 4G ...

# Docker Compose
services:
  nids:
    mem_limit: 4g
```

### Slow Performance

```bash
# Profile application
streamlit run app.py --logger.level=debug

# Check system resources
docker stats
```

## Support

For deployment issues:
1. Check logs: `docker-compose logs nids`
2. Review [SECURITY.md](SECURITY.md)
3. Open GitHub Issue with deployment details
4. See [CONTRIBUTING.md](CONTRIBUTING.md) for community support

---

**Happy Deploying!** 🚀
