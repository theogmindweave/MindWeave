# MindWeave DevOps & CI/CD

## Document Information

| Field | Value |
|-------|-------|
| Document ID | MW-ENG-073 |
| Version | 1.0.0 |
| Last Updated | 2025-01-15 |
| Owner | Platform Engineering |
| Classification | Internal |
| Status | Active |

---

## Executive Summary

This document defines MindWeave's DevOps practices and CI/CD pipeline configuration. Our approach emphasizes automation, security, and reliability throughout the software delivery lifecycle.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CI/CD PIPELINE OVERVIEW                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│   │  Code   │───►│  Build  │───►│  Test   │───►│ Security│───►│  Deploy │  │
│   │  Push   │    │         │    │         │    │  Scan   │    │         │  │
│   └─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘  │
│       │              │              │              │              │         │
│       ▼              ▼              ▼              ▼              ▼         │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                        QUALITY GATES                                 │  │
│   ├─────────────────────────────────────────────────────────────────────┤  │
│   │  ✓ Lint Pass    ✓ Unit Tests   ✓ Integration   ✓ SAST/DAST   ✓ E2E │  │
│   │  ✓ Type Check   ✓ Coverage     ✓ API Tests     ✓ License     ✓ Perf│  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     DEPLOYMENT ENVIRONMENTS                          │  │
│   ├─────────────────────────────────────────────────────────────────────┤  │
│   │                                                                       │  │
│   │   ┌───────────┐    ┌───────────┐    ┌───────────┐                   │  │
│   │   │    DEV    │───►│  STAGING  │───►│PRODUCTION │                   │  │
│   │   │           │    │           │    │           │                   │  │
│   │   │ Auto      │    │ Auto      │    │ Manual    │                   │  │
│   │   │ Deploy    │    │ Deploy    │    │ Approval  │                   │  │
│   │   └───────────┘    └───────────┘    └───────────┘                   │  │
│   │                                                                       │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. GitHub Actions Workflows

### 1.1 Main CI Workflow

```yaml
# .github/workflows/ci.yaml

name: CI Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ============================================
  # STAGE 1: Code Quality
  # ============================================
  lint:
    name: Lint & Format
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run ESLint
        run: npm run lint

      - name: Check Prettier formatting
        run: npm run format:check

      - name: Run TypeScript type check
        run: npm run type-check

  # ============================================
  # STAGE 2: Testing
  # ============================================
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit -- --coverage

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          fail_ci_if_error: true

  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    needs: lint
    services:
      postgres:
        image: timescale/timescaledb:latest-pg15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: mindweave_test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      redis:
        image: redis:7-alpine
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      kafka:
        image: confluentinc/cp-kafka:7.5.0
        ports:
          - 9092:9092
        env:
          KAFKA_BROKER_ID: 1
          KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
          KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
          KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run database migrations
        run: npm run db:migrate
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/mindweave_test

      - name: Run integration tests
        run: npm run test:integration
        env:
          DATABASE_URL: postgresql://test:test@localhost:5432/mindweave_test
          REDIS_URL: redis://localhost:6379
          KAFKA_BROKERS: localhost:9092

      - name: Upload test results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: integration-test-results
          path: reports/

  # ============================================
  # STAGE 3: Security Scanning
  # ============================================
  security-scan:
    name: Security Scan
    runs-on: ubuntu-latest
    needs: lint
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      # SAST - Static Application Security Testing
      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: >-
            p/security-audit
            p/secrets
            p/owasp-top-ten
            p/typescript

      # Dependency Scanning
      - name: Run Snyk
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      # Secret Scanning
      - name: Run TruffleHog
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD
          extra_args: --only-verified

      # License Compliance
      - name: Check licenses
        run: npx license-checker --onlyAllow 'MIT;Apache-2.0;BSD-2-Clause;BSD-3-Clause;ISC;0BSD;CC0-1.0;Unlicense'

  # ============================================
  # STAGE 4: Build
  # ============================================
  build:
    name: Build Application
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests, security-scan]
    outputs:
      version: ${{ steps.version.outputs.version }}
      image-tag: ${{ steps.meta.outputs.tags }}
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build application
        run: npm run build

      - name: Generate version
        id: version
        run: |
          VERSION=$(git describe --tags --always --dirty)
          echo "version=$VERSION" >> $GITHUB_OUTPUT

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=sha,prefix=

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
          build-args: |
            VERSION=${{ steps.version.outputs.version }}
            BUILD_TIME=${{ github.event.head_commit.timestamp }}
            COMMIT_SHA=${{ github.sha }}

  # ============================================
  # STAGE 5: Container Scanning
  # ============================================
  container-scan:
    name: Container Security Scan
    runs-on: ubuntu-latest
    needs: build
    if: github.event_name != 'pull_request'
    steps:
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          format: 'sarif'
          output: 'trivy-results.sarif'
          severity: 'CRITICAL,HIGH'

      - name: Upload Trivy scan results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: 'trivy-results.sarif'

  # ============================================
  # STAGE 6: Deploy to Dev
  # ============================================
  deploy-dev:
    name: Deploy to Dev
    runs-on: ubuntu-latest
    needs: [build, container-scan]
    if: github.ref == 'refs/heads/develop'
    environment: development
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Update kubeconfig
        run: aws eks update-kubeconfig --name mindweave-dev --region us-east-1

      - name: Deploy to Dev
        run: |
          helm upgrade --install mindweave ./helm/mindweave \
            --namespace mindweave-dev \
            --set image.tag=${{ github.sha }} \
            --set environment=development \
            --values ./helm/values-dev.yaml \
            --wait --timeout 10m

      - name: Run smoke tests
        run: |
          kubectl wait --for=condition=ready pod -l app=mindweave -n mindweave-dev --timeout=300s
          curl -sf https://dev.mindweave.io/health/ready || exit 1

  # ============================================
  # STAGE 7: Deploy to Staging
  # ============================================
  deploy-staging:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    needs: [build, container-scan]
    if: github.ref == 'refs/heads/main'
    environment: staging
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Update kubeconfig
        run: aws eks update-kubeconfig --name mindweave-staging --region us-east-1

      - name: Deploy to Staging
        run: |
          helm upgrade --install mindweave ./helm/mindweave \
            --namespace mindweave-staging \
            --set image.tag=${{ github.sha }} \
            --set environment=staging \
            --values ./helm/values-staging.yaml \
            --wait --timeout 10m

      - name: Run E2E tests
        run: npm run test:e2e
        env:
          E2E_BASE_URL: https://staging.mindweave.io

  # ============================================
  # STAGE 8: Deploy to Production
  # ============================================
  deploy-production:
    name: Deploy to Production
    runs-on: ubuntu-latest
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Update kubeconfig
        run: aws eks update-kubeconfig --name mindweave-production --region us-east-1

      - name: Deploy Canary
        run: |
          helm upgrade --install mindweave ./helm/mindweave \
            --namespace mindweave-production \
            --set image.tag=${{ github.sha }} \
            --set environment=production \
            --set canary.enabled=true \
            --set canary.weight=5 \
            --values ./helm/values-production.yaml \
            --wait --timeout 10m

      - name: Monitor Canary (5 minutes)
        run: |
          sleep 300
          # Check error rate
          ERROR_RATE=$(kubectl exec -n mindweave-monitoring prometheus-0 -- \
            promtool query instant \
            'sum(rate(http_requests_total{status_code=~"5..",version="canary"}[5m])) / sum(rate(http_requests_total{version="canary"}[5m]))')

          if (( $(echo "$ERROR_RATE > 0.01" | bc -l) )); then
            echo "Error rate too high: $ERROR_RATE"
            exit 1
          fi

      - name: Promote to 100%
        run: |
          helm upgrade --install mindweave ./helm/mindweave \
            --namespace mindweave-production \
            --set image.tag=${{ github.sha }} \
            --set environment=production \
            --set canary.enabled=false \
            --values ./helm/values-production.yaml \
            --wait --timeout 10m

      - name: Create release
        uses: softprops/action-gh-release@v1
        if: startsWith(github.ref, 'refs/tags/')
        with:
          generate_release_notes: true
```

### 1.2 Pull Request Workflow

```yaml
# .github/workflows/pr.yaml

name: Pull Request

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  pr-checks:
    name: PR Checks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Check commit messages
        uses: wagoid/commitlint-github-action@v5
        with:
          configFile: .commitlintrc.json

      - name: Check PR title
        uses: amannn/action-semantic-pull-request@v5
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          types: |
            feat
            fix
            docs
            style
            refactor
            perf
            test
            build
            ci
            chore
            revert

      - name: Check for breaking changes
        run: |
          if [[ "${{ github.event.pull_request.title }}" == *"!"* ]] || \
             [[ "${{ github.event.pull_request.body }}" == *"BREAKING CHANGE"* ]]; then
            echo "::warning::This PR contains breaking changes"
          fi

      - name: Label PR based on files changed
        uses: actions/labeler@v4
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}

  size-check:
    name: PR Size Check
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check PR size
        uses: codelytv/pr-size-labeler@v1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          xs_label: 'size/xs'
          xs_max_size: '10'
          s_label: 'size/s'
          s_max_size: '100'
          m_label: 'size/m'
          m_max_size: '500'
          l_label: 'size/l'
          l_max_size: '1000'
          xl_label: 'size/xl'
          fail_if_xl: 'false'
          message_if_xl: >
            This PR is quite large. Consider breaking it into smaller, focused PRs
            for easier review.

  preview-deploy:
    name: Deploy Preview
    runs-on: ubuntu-latest
    if: github.event.pull_request.head.repo.full_name == github.repository
    steps:
      - uses: actions/checkout@v4

      - name: Deploy preview environment
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          scope: ${{ secrets.VERCEL_ORG_ID }}
          alias-domains: |
            pr-${{ github.event.number }}.preview.mindweave.io

      - name: Comment preview URL
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '🚀 Preview deployed to https://pr-${{ github.event.number }}.preview.mindweave.io'
            })
```

---

## 2. Docker Configuration

### 2.1 Multi-Stage Dockerfile

```dockerfile
# Dockerfile

# ============================================
# Stage 1: Dependencies
# ============================================
FROM node:20-alpine AS deps
WORKDIR /app

# Install dependencies only when package files change
COPY package.json package-lock.json ./
RUN npm ci --only=production

# ============================================
# Stage 2: Builder
# ============================================
FROM node:20-alpine AS builder
WORKDIR /app

# Copy dependencies
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Build arguments
ARG VERSION=dev
ARG BUILD_TIME
ARG COMMIT_SHA

# Set build-time environment variables
ENV NEXT_PUBLIC_VERSION=$VERSION
ENV NEXT_PUBLIC_BUILD_TIME=$BUILD_TIME
ENV NEXT_PUBLIC_COMMIT_SHA=$COMMIT_SHA

# Build application
RUN npm run build

# ============================================
# Stage 3: Production Runner
# ============================================
FROM node:20-alpine AS runner
WORKDIR /app

# Security: Run as non-root user
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 mindweave

# Set environment
ENV NODE_ENV=production
ENV PORT=3000

# Copy necessary files
COPY --from=builder --chown=mindweave:nodejs /app/dist ./dist
COPY --from=builder --chown=mindweave:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=mindweave:nodejs /app/package.json ./

# Copy runtime configs
COPY --chown=mindweave:nodejs docker-entrypoint.sh ./

# Make entrypoint executable
RUN chmod +x docker-entrypoint.sh

# Switch to non-root user
USER mindweave

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health/live || exit 1

# Start application
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["node", "dist/main.js"]
```

### 2.2 Docker Entrypoint

```bash
#!/bin/sh
# docker-entrypoint.sh

set -e

# Wait for dependencies
echo "Waiting for dependencies..."

# Wait for PostgreSQL
if [ -n "$DATABASE_URL" ]; then
  echo "Waiting for PostgreSQL..."
  until pg_isready -h "$DATABASE_HOST" -p "${DATABASE_PORT:-5432}" -U "$DATABASE_USER"; do
    sleep 1
  done
  echo "PostgreSQL is ready"
fi

# Wait for Redis
if [ -n "$REDIS_URL" ]; then
  echo "Waiting for Redis..."
  until redis-cli -h "$REDIS_HOST" -p "${REDIS_PORT:-6379}" ping; do
    sleep 1
  done
  echo "Redis is ready"
fi

# Run database migrations if enabled
if [ "$RUN_MIGRATIONS" = "true" ]; then
  echo "Running database migrations..."
  npm run db:migrate
fi

# Start application
echo "Starting application..."
exec "$@"
```

### 2.3 Docker Compose for Development

```yaml
# docker-compose.yml

version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    volumes:
      - .:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://mindweave:mindweave@postgres:5432/mindweave
      - REDIS_URL=redis://redis:6379
      - KAFKA_BROKERS=kafka:9092
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
      kafka:
        condition: service_healthy

  postgres:
    image: timescale/timescaledb:latest-pg15
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: mindweave
      POSTGRES_PASSWORD: mindweave
      POSTGRES_DB: mindweave
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts/init-db.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U mindweave"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:29092,PLAINTEXT_HOST://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
      KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'true'
    depends_on:
      - zookeeper
    healthcheck:
      test: ["CMD", "kafka-broker-api-versions", "--bootstrap-server", "localhost:9092"]
      interval: 10s
      timeout: 5s
      retries: 5

  kafka-ui:
    image: provectuslabs/kafka-ui
    ports:
      - "8080:8080"
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:29092
    depends_on:
      - kafka

  mailhog:
    image: mailhog/mailhog
    ports:
      - "1025:1025"
      - "8025:8025"

volumes:
  postgres_data:
  redis_data:
```

---

## 3. Helm Charts

### 3.1 Chart Structure

```
helm/mindweave/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-staging.yaml
├── values-production.yaml
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── pdb.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── serviceaccount.yaml
│   └── servicemonitor.yaml
└── charts/
    └── postgresql/
```

### 3.2 Main Values File

```yaml
# helm/mindweave/values.yaml

# Global settings
global:
  environment: development
  domain: mindweave.io

# Application settings
replicaCount: 3

image:
  repository: ghcr.io/mindweave/platform
  pullPolicy: IfNotPresent
  tag: "latest"

imagePullSecrets:
  - name: ghcr-secret

nameOverride: ""
fullnameOverride: ""

serviceAccount:
  create: true
  annotations:
    eks.amazonaws.com/role-arn: ""
  name: ""

podAnnotations:
  prometheus.io/scrape: "true"
  prometheus.io/port: "9090"
  prometheus.io/path: "/metrics"

podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1001
  fsGroup: 1001

securityContext:
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop:
      - ALL

service:
  type: ClusterIP
  port: 80
  targetPort: 3000
  metricsPort: 9090

ingress:
  enabled: true
  className: nginx
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/rate-limit: "100"
    nginx.ingress.kubernetes.io/rate-limit-window: "1m"
  hosts:
    - host: api.mindweave.io
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: mindweave-tls
      hosts:
        - api.mindweave.io

resources:
  limits:
    cpu: 1000m
    memory: 1Gi
  requests:
    cpu: 250m
    memory: 512Mi

autoscaling:
  enabled: true
  minReplicas: 3
  maxReplicas: 20
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15

podDisruptionBudget:
  enabled: true
  minAvailable: 2

nodeSelector: {}

tolerations: []

affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchLabels:
              app.kubernetes.io/name: mindweave
          topologyKey: kubernetes.io/hostname

topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: ScheduleAnyway
    labelSelector:
      matchLabels:
        app.kubernetes.io/name: mindweave

# Environment variables
env:
  NODE_ENV: production
  PORT: "3000"
  LOG_LEVEL: info

# Secrets (reference external secrets)
secrets:
  databaseUrl:
    secretName: mindweave-secrets
    key: database-url
  redisUrl:
    secretName: mindweave-secrets
    key: redis-url
  jwtSecret:
    secretName: mindweave-secrets
    key: jwt-secret

# Health checks
livenessProbe:
  httpGet:
    path: /health/live
    port: http
  initialDelaySeconds: 10
  periodSeconds: 10
  timeoutSeconds: 5
  failureThreshold: 3

readinessProbe:
  httpGet:
    path: /health/ready
    port: http
  initialDelaySeconds: 5
  periodSeconds: 5
  timeoutSeconds: 3
  failureThreshold: 3

# Canary deployment
canary:
  enabled: false
  weight: 0
  analysis:
    enabled: true
    interval: 1m
    threshold: 5
    stepWeight: 10
    maxWeight: 50

# Service monitor for Prometheus
serviceMonitor:
  enabled: true
  interval: 30s
  path: /metrics
  labels:
    release: prometheus
```

### 3.3 Deployment Template

```yaml
# helm/mindweave/templates/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "mindweave.fullname" . }}
  labels:
    {{- include "mindweave.labels" . | nindent 4 }}
spec:
  {{- if not .Values.autoscaling.enabled }}
  replicas: {{ .Values.replicaCount }}
  {{- end }}
  selector:
    matchLabels:
      {{- include "mindweave.selectorLabels" . | nindent 6 }}
  template:
    metadata:
      annotations:
        checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
        checksum/secret: {{ include (print $.Template.BasePath "/secret.yaml") . | sha256sum }}
        {{- with .Values.podAnnotations }}
        {{- toYaml . | nindent 8 }}
        {{- end }}
      labels:
        {{- include "mindweave.selectorLabels" . | nindent 8 }}
        {{- if .Values.canary.enabled }}
        version: canary
        {{- else }}
        version: stable
        {{- end }}
    spec:
      {{- with .Values.imagePullSecrets }}
      imagePullSecrets:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      serviceAccountName: {{ include "mindweave.serviceAccountName" . }}
      securityContext:
        {{- toYaml .Values.podSecurityContext | nindent 8 }}
      containers:
        - name: {{ .Chart.Name }}
          securityContext:
            {{- toYaml .Values.securityContext | nindent 12 }}
          image: "{{ .Values.image.repository }}:{{ .Values.image.tag | default .Chart.AppVersion }}"
          imagePullPolicy: {{ .Values.image.pullPolicy }}
          ports:
            - name: http
              containerPort: {{ .Values.service.targetPort }}
              protocol: TCP
            - name: metrics
              containerPort: {{ .Values.service.metricsPort }}
              protocol: TCP
          env:
            {{- range $key, $value := .Values.env }}
            - name: {{ $key }}
              value: {{ $value | quote }}
            {{- end }}
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.secrets.databaseUrl.secretName }}
                  key: {{ .Values.secrets.databaseUrl.key }}
            - name: REDIS_URL
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.secrets.redisUrl.secretName }}
                  key: {{ .Values.secrets.redisUrl.key }}
            - name: JWT_SECRET
              valueFrom:
                secretKeyRef:
                  name: {{ .Values.secrets.jwtSecret.secretName }}
                  key: {{ .Values.secrets.jwtSecret.key }}
          livenessProbe:
            {{- toYaml .Values.livenessProbe | nindent 12 }}
          readinessProbe:
            {{- toYaml .Values.readinessProbe | nindent 12 }}
          resources:
            {{- toYaml .Values.resources | nindent 12 }}
          volumeMounts:
            - name: tmp
              mountPath: /tmp
            - name: cache
              mountPath: /app/.cache
      volumes:
        - name: tmp
          emptyDir: {}
        - name: cache
          emptyDir: {}
      {{- with .Values.nodeSelector }}
      nodeSelector:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.affinity }}
      affinity:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.tolerations }}
      tolerations:
        {{- toYaml . | nindent 8 }}
      {{- end }}
      {{- with .Values.topologySpreadConstraints }}
      topologySpreadConstraints:
        {{- toYaml . | nindent 8 }}
      {{- end }}
```

---

## 4. Infrastructure as Code

### 4.1 Terraform Provider Configuration

```hcl
# terraform/providers.tf

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.11"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }

  backend "s3" {
    bucket         = "mindweave-terraform-state"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "mindweave-terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "MindWeave"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)

  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
  }
}

provider "helm" {
  kubernetes {
    host                   = module.eks.cluster_endpoint
    cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)

    exec {
      api_version = "client.authentication.k8s.io/v1beta1"
      command     = "aws"
      args        = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
    }
  }
}
```

### 4.2 Environment Configuration

```hcl
# terraform/environments/production/main.tf

module "vpc" {
  source = "../../modules/vpc"

  environment        = "production"
  vpc_cidr          = "10.0.0.0/16"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

module "eks" {
  source = "../../modules/eks"

  environment        = "production"
  vpc_id             = module.vpc.vpc_id
  private_subnet_ids = module.vpc.private_app_subnet_ids
  cluster_version    = "1.28"

  node_groups = {
    application = {
      instance_types = ["m6i.xlarge"]
      min_size       = 3
      max_size       = 20
      desired_size   = 6
    }
    system = {
      instance_types = ["m6i.large"]
      min_size       = 2
      max_size       = 5
      desired_size   = 3
    }
  }
}

module "rds" {
  source = "../../modules/rds"

  environment     = "production"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_data_subnet_ids

  instance_class  = "db.r6i.xlarge"
  engine_version  = "15.4"

  multi_az        = true
  storage_type    = "gp3"
  allocated_storage = 500
  max_allocated_storage = 2000

  backup_retention_period = 30
  backup_window          = "03:00-04:00"
  maintenance_window     = "Mon:04:00-Mon:05:00"

  performance_insights_enabled = true
}

module "elasticache" {
  source = "../../modules/elasticache"

  environment     = "production"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_data_subnet_ids

  node_type       = "cache.r6g.xlarge"
  num_cache_nodes = 3

  automatic_failover_enabled = true
  multi_az_enabled          = true

  snapshot_retention_limit = 7
  snapshot_window         = "05:00-06:00"
}

module "msk" {
  source = "../../modules/msk"

  environment     = "production"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_data_subnet_ids

  kafka_version   = "3.5.1"
  instance_type   = "kafka.m5.xlarge"
  number_of_broker_nodes = 3

  ebs_volume_size = 500
}
```

---

## 5. Secrets Management

### 5.1 AWS Secrets Manager Integration

```yaml
# k8s/secrets/external-secrets.yaml

apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: aws-secrets-manager
  namespace: mindweave-services
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-east-1
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa
---
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: mindweave-secrets
  namespace: mindweave-services
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: SecretStore
  target:
    name: mindweave-secrets
    creationPolicy: Owner
  data:
    - secretKey: database-url
      remoteRef:
        key: mindweave/production/database
        property: url
    - secretKey: redis-url
      remoteRef:
        key: mindweave/production/redis
        property: url
    - secretKey: jwt-secret
      remoteRef:
        key: mindweave/production/jwt
        property: secret
    - secretKey: stripe-secret-key
      remoteRef:
        key: mindweave/production/stripe
        property: secret_key
    - secretKey: sendgrid-api-key
      remoteRef:
        key: mindweave/production/sendgrid
        property: api_key
```

### 5.2 Secret Rotation

```hcl
# terraform/modules/secrets/rotation.tf

resource "aws_secretsmanager_secret_rotation" "database" {
  secret_id           = aws_secretsmanager_secret.database.id
  rotation_lambda_arn = aws_lambda_function.secret_rotation.arn

  rotation_rules {
    automatically_after_days = 30
  }
}

resource "aws_lambda_function" "secret_rotation" {
  filename         = "rotation_lambda.zip"
  function_name    = "${var.environment}-secret-rotation"
  role            = aws_iam_role.rotation_lambda.arn
  handler         = "lambda_function.handler"
  runtime         = "python3.11"
  timeout         = 30

  vpc_config {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [aws_security_group.rotation_lambda.id]
  }

  environment {
    variables = {
      SECRETS_MANAGER_ENDPOINT = "https://secretsmanager.${var.aws_region}.amazonaws.com"
    }
  }
}
```

---

## 6. Monitoring & Alerting Pipeline

### 6.1 Pipeline Health Monitoring

```yaml
# .github/workflows/pipeline-monitoring.yaml

name: Pipeline Monitoring

on:
  workflow_run:
    workflows: ["CI Pipeline"]
    types:
      - completed

jobs:
  report-metrics:
    runs-on: ubuntu-latest
    steps:
      - name: Send metrics to DataDog
        run: |
          curl -X POST "https://api.datadoghq.com/api/v1/series" \
            -H "Content-Type: application/json" \
            -H "DD-API-KEY: ${{ secrets.DD_API_KEY }}" \
            -d @- <<EOF
          {
            "series": [
              {
                "metric": "ci.pipeline.duration",
                "points": [[$(date +%s), ${{ github.event.workflow_run.run_duration }}]],
                "type": "gauge",
                "tags": [
                  "workflow:${{ github.event.workflow_run.name }}",
                  "conclusion:${{ github.event.workflow_run.conclusion }}",
                  "branch:${{ github.event.workflow_run.head_branch }}"
                ]
              },
              {
                "metric": "ci.pipeline.status",
                "points": [[$(date +%s), ${{ github.event.workflow_run.conclusion == 'success' && 1 || 0 }}]],
                "type": "gauge",
                "tags": [
                  "workflow:${{ github.event.workflow_run.name }}",
                  "branch:${{ github.event.workflow_run.head_branch }}"
                ]
              }
            ]
          }
          EOF

      - name: Alert on failure
        if: github.event.workflow_run.conclusion == 'failure'
        run: |
          curl -X POST "${{ secrets.SLACK_WEBHOOK_URL }}" \
            -H "Content-Type: application/json" \
            -d @- <<EOF
          {
            "text": "🔴 Pipeline Failed",
            "attachments": [
              {
                "color": "danger",
                "fields": [
                  {
                    "title": "Workflow",
                    "value": "${{ github.event.workflow_run.name }}",
                    "short": true
                  },
                  {
                    "title": "Branch",
                    "value": "${{ github.event.workflow_run.head_branch }}",
                    "short": true
                  },
                  {
                    "title": "Run URL",
                    "value": "${{ github.event.workflow_run.html_url }}",
                    "short": false
                  }
                ]
              }
            ]
          }
          EOF
```

---

## 7. Release Management

### 7.1 Semantic Release Configuration

```javascript
// release.config.js

module.exports = {
  branches: [
    'main',
    { name: 'beta', prerelease: true },
    { name: 'alpha', prerelease: true },
  ],
  plugins: [
    [
      '@semantic-release/commit-analyzer',
      {
        preset: 'conventionalcommits',
        releaseRules: [
          { type: 'feat', release: 'minor' },
          { type: 'fix', release: 'patch' },
          { type: 'perf', release: 'patch' },
          { type: 'refactor', release: 'patch' },
          { type: 'docs', scope: 'README', release: 'patch' },
          { type: 'style', release: false },
          { type: 'test', release: false },
          { type: 'chore', release: false },
          { breaking: true, release: 'major' },
        ],
      },
    ],
    [
      '@semantic-release/release-notes-generator',
      {
        preset: 'conventionalcommits',
        presetConfig: {
          types: [
            { type: 'feat', section: 'Features' },
            { type: 'fix', section: 'Bug Fixes' },
            { type: 'perf', section: 'Performance Improvements' },
            { type: 'refactor', section: 'Code Refactoring' },
            { type: 'docs', section: 'Documentation' },
            { type: 'style', section: 'Styles', hidden: true },
            { type: 'chore', section: 'Miscellaneous Chores', hidden: true },
            { type: 'test', section: 'Tests', hidden: true },
          ],
        },
      },
    ],
    [
      '@semantic-release/changelog',
      {
        changelogFile: 'CHANGELOG.md',
      },
    ],
    [
      '@semantic-release/npm',
      {
        npmPublish: false,
      },
    ],
    [
      '@semantic-release/git',
      {
        assets: ['CHANGELOG.md', 'package.json', 'package-lock.json'],
        message: 'chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}',
      },
    ],
    '@semantic-release/github',
  ],
};
```

### 7.2 Release Workflow

```yaml
# .github/workflows/release.yaml

name: Release

on:
  push:
    branches:
      - main
      - beta
      - alpha

permissions:
  contents: write
  issues: write
  pull-requests: write
  packages: write

jobs:
  release:
    name: Release
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [DEPLOYMENT-STRATEGY.md](./DEPLOYMENT-STRATEGY.md) | Deployment procedures |
| [TESTING-STRATEGY.md](./TESTING-STRATEGY.md) | Testing approach |
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Monitoring setup |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security controls |
| [INCIDENT-RESPONSE.md](./INCIDENT-RESPONSE.md) | Incident handling |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Platform Engineering | Initial DevOps & CI/CD documentation |
