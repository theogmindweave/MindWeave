# MindWeave Deployment Strategy

## Document Information

| Field | Value |
|-------|-------|
| Document ID | MW-ENG-070 |
| Version | 1.0.0 |
| Last Updated | 2025-01-15 |
| Owner | Platform Engineering |
| Classification | Internal |
| Status | Active |

---

## Executive Summary

This document defines MindWeave's deployment strategy, covering infrastructure provisioning, deployment patterns, release management, and rollback procedures. Our deployment approach prioritizes zero-downtime releases, automated validation, and rapid rollback capabilities.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DEPLOYMENT PIPELINE OVERVIEW                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Source  │───►│  Build   │───►│  Test    │───►│  Stage   │              │
│  │   Code   │    │  & Scan  │    │  Suite   │    │  Deploy  │              │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘              │
│                                                        │                    │
│                                                        ▼                    │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Prod    │◄───│  Canary  │◄───│ Approval │◄───│  Smoke   │              │
│  │ Rollout  │    │  Deploy  │    │   Gate   │    │  Tests   │              │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘              │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     DEPLOYMENT TARGETS                               │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐       │   │
│  │   │  us-east-1    │    │  us-west-2    │    │  eu-west-1    │       │   │
│  │   │   PRIMARY     │    │   SECONDARY   │    │    EU DATA    │       │   │
│  │   │               │    │               │    │               │       │   │
│  │   │ ┌───────────┐ │    │ ┌───────────┐ │    │ ┌───────────┐ │       │   │
│  │   │ │ EKS       │ │    │ │ EKS       │ │    │ │ EKS       │ │       │   │
│  │   │ │ Cluster   │ │    │ │ Cluster   │ │    │ │ Cluster   │ │       │   │
│  │   │ └───────────┘ │    │ └───────────┘ │    │ └───────────┘ │       │   │
│  │   └───────────────┘    └───────────────┘    └───────────────┘       │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Infrastructure as Code

### 1.1 Terraform Configuration Structure

```
infrastructure/
├── modules/
│   ├── vpc/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   └── vpc.tf
│   ├── eks/
│   │   ├── main.tf
│   │   ├── cluster.tf
│   │   ├── node-groups.tf
│   │   └── addons.tf
│   ├── rds/
│   │   ├── main.tf
│   │   ├── postgresql.tf
│   │   └── timescaledb.tf
│   ├── elasticache/
│   │   ├── main.tf
│   │   └── redis.tf
│   ├── msk/
│   │   ├── main.tf
│   │   └── kafka.tf
│   └── security/
│       ├── kms.tf
│       ├── waf.tf
│       └── secrets.tf
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   └── production/
│       ├── main.tf
│       ├── terraform.tfvars
│       └── backend.tf
└── global/
    ├── iam/
    ├── route53/
    └── s3-state/
```

### 1.2 VPC Module

```hcl
# modules/vpc/main.tf

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

variable "environment" {
  type        = string
  description = "Environment name (dev, staging, production)"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "availability_zones" {
  type        = list(string)
  description = "List of availability zones"
}

locals {
  name_prefix = "mindweave-${var.environment}"

  public_subnets = [
    for i, az in var.availability_zones :
    cidrsubnet(var.vpc_cidr, 8, i + 1)
  ]

  private_app_subnets = [
    for i, az in var.availability_zones :
    cidrsubnet(var.vpc_cidr, 8, i + 10)
  ]

  private_data_subnets = [
    for i, az in var.availability_zones :
    cidrsubnet(var.vpc_cidr, 8, i + 20)
  ]
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "${local.name_prefix}-vpc"
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name        = "${local.name_prefix}-igw"
    Environment = var.environment
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count                   = length(var.availability_zones)
  vpc_id                  = aws_vpc.main.id
  cidr_block              = local.public_subnets[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name                                           = "${local.name_prefix}-public-${var.availability_zones[count.index]}"
    Environment                                    = var.environment
    "kubernetes.io/role/elb"                       = "1"
    "kubernetes.io/cluster/${local.name_prefix}"   = "shared"
  }
}

# Private App Subnets
resource "aws_subnet" "private_app" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = local.private_app_subnets[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = {
    Name                                           = "${local.name_prefix}-private-app-${var.availability_zones[count.index]}"
    Environment                                    = var.environment
    "kubernetes.io/role/internal-elb"              = "1"
    "kubernetes.io/cluster/${local.name_prefix}"   = "shared"
  }
}

# Private Data Subnets
resource "aws_subnet" "private_data" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = local.private_data_subnets[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = {
    Name        = "${local.name_prefix}-private-data-${var.availability_zones[count.index]}"
    Environment = var.environment
  }
}

# NAT Gateways
resource "aws_eip" "nat" {
  count  = length(var.availability_zones)
  domain = "vpc"

  tags = {
    Name        = "${local.name_prefix}-nat-eip-${count.index + 1}"
    Environment = var.environment
  }
}

resource "aws_nat_gateway" "main" {
  count         = length(var.availability_zones)
  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = aws_subnet.public[count.index].id

  tags = {
    Name        = "${local.name_prefix}-nat-${var.availability_zones[count.index]}"
    Environment = var.environment
  }

  depends_on = [aws_internet_gateway.main]
}

# Route Tables
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name        = "${local.name_prefix}-public-rt"
    Environment = var.environment
  }
}

resource "aws_route_table" "private" {
  count  = length(var.availability_zones)
  vpc_id = aws_vpc.main.id

  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.main[count.index].id
  }

  tags = {
    Name        = "${local.name_prefix}-private-rt-${var.availability_zones[count.index]}"
    Environment = var.environment
  }
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  count          = length(var.availability_zones)
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private_app" {
  count          = length(var.availability_zones)
  subnet_id      = aws_subnet.private_app[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

resource "aws_route_table_association" "private_data" {
  count          = length(var.availability_zones)
  subnet_id      = aws_subnet.private_data[count.index].id
  route_table_id = aws_route_table.private[count.index].id
}

# VPC Endpoints
resource "aws_vpc_endpoint" "s3" {
  vpc_id            = aws_vpc.main.id
  service_name      = "com.amazonaws.${data.aws_region.current.name}.s3"
  vpc_endpoint_type = "Gateway"
  route_table_ids   = aws_route_table.private[*].id

  tags = {
    Name        = "${local.name_prefix}-s3-endpoint"
    Environment = var.environment
  }
}

resource "aws_vpc_endpoint" "ecr_api" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.ecr.api"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.private_app[*].id
  security_group_ids  = [aws_security_group.vpc_endpoints.id]
  private_dns_enabled = true

  tags = {
    Name        = "${local.name_prefix}-ecr-api-endpoint"
    Environment = var.environment
  }
}

resource "aws_vpc_endpoint" "ecr_dkr" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.ecr.dkr"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.private_app[*].id
  security_group_ids  = [aws_security_group.vpc_endpoints.id]
  private_dns_enabled = true

  tags = {
    Name        = "${local.name_prefix}-ecr-dkr-endpoint"
    Environment = var.environment
  }
}

resource "aws_vpc_endpoint" "secretsmanager" {
  vpc_id              = aws_vpc.main.id
  service_name        = "com.amazonaws.${data.aws_region.current.name}.secretsmanager"
  vpc_endpoint_type   = "Interface"
  subnet_ids          = aws_subnet.private_app[*].id
  security_group_ids  = [aws_security_group.vpc_endpoints.id]
  private_dns_enabled = true

  tags = {
    Name        = "${local.name_prefix}-secretsmanager-endpoint"
    Environment = var.environment
  }
}

# Security Group for VPC Endpoints
resource "aws_security_group" "vpc_endpoints" {
  name_prefix = "${local.name_prefix}-vpc-endpoints-"
  vpc_id      = aws_vpc.main.id
  description = "Security group for VPC endpoints"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "${local.name_prefix}-vpc-endpoints-sg"
    Environment = var.environment
  }
}

data "aws_region" "current" {}

# Outputs
output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_app_subnet_ids" {
  value = aws_subnet.private_app[*].id
}

output "private_data_subnet_ids" {
  value = aws_subnet.private_data[*].id
}
```

### 1.3 EKS Cluster Module

```hcl
# modules/eks/main.tf

variable "environment" {
  type = string
}

variable "vpc_id" {
  type = string
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "cluster_version" {
  type    = string
  default = "1.28"
}

locals {
  name_prefix  = "mindweave-${var.environment}"
  cluster_name = "${local.name_prefix}-eks"
}

# EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = local.cluster_name
  version  = var.cluster_version
  role_arn = aws_iam_role.cluster.arn

  vpc_config {
    subnet_ids              = var.private_subnet_ids
    endpoint_private_access = true
    endpoint_public_access  = var.environment == "dev" ? true : false
    security_group_ids      = [aws_security_group.cluster.id]
  }

  encryption_config {
    provider {
      key_arn = aws_kms_key.eks.arn
    }
    resources = ["secrets"]
  }

  enabled_cluster_log_types = [
    "api",
    "audit",
    "authenticator",
    "controllerManager",
    "scheduler"
  ]

  tags = {
    Name        = local.cluster_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }

  depends_on = [
    aws_iam_role_policy_attachment.cluster_policy,
    aws_iam_role_policy_attachment.cluster_vpc_policy,
  ]
}

# EKS Node Groups
resource "aws_eks_node_group" "application" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${local.name_prefix}-app-nodes"
  node_role_arn   = aws_iam_role.node.arn
  subnet_ids      = var.private_subnet_ids
  instance_types  = var.environment == "production" ? ["m6i.xlarge"] : ["m6i.large"]
  capacity_type   = "ON_DEMAND"

  scaling_config {
    desired_size = var.environment == "production" ? 6 : 3
    max_size     = var.environment == "production" ? 20 : 10
    min_size     = var.environment == "production" ? 3 : 2
  }

  update_config {
    max_unavailable_percentage = 25
  }

  labels = {
    role        = "application"
    environment = var.environment
  }

  taint {
    key    = "dedicated"
    value  = "application"
    effect = "NO_SCHEDULE"
  }

  tags = {
    Name        = "${local.name_prefix}-app-nodes"
    Environment = var.environment
  }

  depends_on = [
    aws_iam_role_policy_attachment.node_policy,
    aws_iam_role_policy_attachment.node_cni_policy,
    aws_iam_role_policy_attachment.node_ecr_policy,
  ]
}

resource "aws_eks_node_group" "system" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${local.name_prefix}-system-nodes"
  node_role_arn   = aws_iam_role.node.arn
  subnet_ids      = var.private_subnet_ids
  instance_types  = ["m6i.large"]
  capacity_type   = "ON_DEMAND"

  scaling_config {
    desired_size = 3
    max_size     = 5
    min_size     = 2
  }

  labels = {
    role        = "system"
    environment = var.environment
  }

  taint {
    key    = "CriticalAddonsOnly"
    value  = "true"
    effect = "NO_SCHEDULE"
  }

  tags = {
    Name        = "${local.name_prefix}-system-nodes"
    Environment = var.environment
  }
}

# KMS Key for EKS Secrets Encryption
resource "aws_kms_key" "eks" {
  description             = "KMS key for EKS cluster secrets encryption"
  deletion_window_in_days = 7
  enable_key_rotation     = true

  tags = {
    Name        = "${local.name_prefix}-eks-kms"
    Environment = var.environment
  }
}

# IAM Roles
resource "aws_iam_role" "cluster" {
  name = "${local.name_prefix}-eks-cluster-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cluster_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
  role       = aws_iam_role.cluster.name
}

resource "aws_iam_role_policy_attachment" "cluster_vpc_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
  role       = aws_iam_role.cluster.name
}

resource "aws_iam_role" "node" {
  name = "${local.name_prefix}-eks-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "node_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
  role       = aws_iam_role.node.name
}

resource "aws_iam_role_policy_attachment" "node_cni_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
  role       = aws_iam_role.node.name
}

resource "aws_iam_role_policy_attachment" "node_ecr_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
  role       = aws_iam_role.node.name
}

# Security Group
resource "aws_security_group" "cluster" {
  name_prefix = "${local.name_prefix}-eks-cluster-"
  vpc_id      = var.vpc_id
  description = "EKS cluster security group"

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "${local.name_prefix}-eks-cluster-sg"
    Environment = var.environment
  }
}

# EKS Addons
resource "aws_eks_addon" "vpc_cni" {
  cluster_name                = aws_eks_cluster.main.name
  addon_name                  = "vpc-cni"
  addon_version               = "v1.15.0-eksbuild.2"
  resolve_conflicts_on_update = "PRESERVE"
}

resource "aws_eks_addon" "coredns" {
  cluster_name                = aws_eks_cluster.main.name
  addon_name                  = "coredns"
  addon_version               = "v1.10.1-eksbuild.4"
  resolve_conflicts_on_update = "PRESERVE"

  depends_on = [aws_eks_node_group.system]
}

resource "aws_eks_addon" "kube_proxy" {
  cluster_name                = aws_eks_cluster.main.name
  addon_name                  = "kube-proxy"
  addon_version               = "v1.28.1-eksbuild.1"
  resolve_conflicts_on_update = "PRESERVE"
}

resource "aws_eks_addon" "ebs_csi_driver" {
  cluster_name                = aws_eks_cluster.main.name
  addon_name                  = "aws-ebs-csi-driver"
  addon_version               = "v1.25.0-eksbuild.1"
  service_account_role_arn    = aws_iam_role.ebs_csi.arn
  resolve_conflicts_on_update = "PRESERVE"
}

# OIDC Provider for IRSA
data "tls_certificate" "eks" {
  url = aws_eks_cluster.main.identity[0].oidc[0].issuer
}

resource "aws_iam_openid_connect_provider" "eks" {
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = [data.tls_certificate.eks.certificates[0].sha1_fingerprint]
  url             = aws_eks_cluster.main.identity[0].oidc[0].issuer

  tags = {
    Name        = "${local.name_prefix}-eks-oidc"
    Environment = var.environment
  }
}

# EBS CSI Driver IAM Role (IRSA)
resource "aws_iam_role" "ebs_csi" {
  name = "${local.name_prefix}-ebs-csi-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRoleWithWebIdentity"
      Effect = "Allow"
      Principal = {
        Federated = aws_iam_openid_connect_provider.eks.arn
      }
      Condition = {
        StringEquals = {
          "${replace(aws_eks_cluster.main.identity[0].oidc[0].issuer, "https://", "")}:sub" = "system:serviceaccount:kube-system:ebs-csi-controller-sa"
        }
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ebs_csi" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
  role       = aws_iam_role.ebs_csi.name
}

# Outputs
output "cluster_name" {
  value = aws_eks_cluster.main.name
}

output "cluster_endpoint" {
  value = aws_eks_cluster.main.endpoint
}

output "cluster_certificate_authority_data" {
  value = aws_eks_cluster.main.certificate_authority[0].data
}

output "oidc_provider_arn" {
  value = aws_iam_openid_connect_provider.eks.arn
}
```

---

## 2. Kubernetes Manifests

### 2.1 Namespace Configuration

```yaml
# k8s/base/namespaces.yaml

apiVersion: v1
kind: Namespace
metadata:
  name: mindweave-system
  labels:
    app.kubernetes.io/managed-by: argocd
    istio-injection: enabled
---
apiVersion: v1
kind: Namespace
metadata:
  name: mindweave-services
  labels:
    app.kubernetes.io/managed-by: argocd
    istio-injection: enabled
---
apiVersion: v1
kind: Namespace
metadata:
  name: mindweave-data
  labels:
    app.kubernetes.io/managed-by: argocd
    istio-injection: enabled
---
apiVersion: v1
kind: Namespace
metadata:
  name: mindweave-monitoring
  labels:
    app.kubernetes.io/managed-by: argocd
```

### 2.2 Service Deployment

```yaml
# k8s/services/api-gateway/deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
  namespace: mindweave-services
  labels:
    app: api-gateway
    version: v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-gateway
  template:
    metadata:
      labels:
        app: api-gateway
        version: v1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "9090"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: api-gateway
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        fsGroup: 1000
      containers:
        - name: api-gateway
          image: mindweave/api-gateway:latest
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 3000
            - name: metrics
              containerPort: 9090
          env:
            - name: NODE_ENV
              value: "production"
            - name: PORT
              value: "3000"
            - name: LOG_LEVEL
              value: "info"
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: api-gateway-secrets
                  key: database-url
            - name: REDIS_URL
              valueFrom:
                secretKeyRef:
                  name: api-gateway-secrets
                  key: redis-url
            - name: JWT_SECRET
              valueFrom:
                secretKeyRef:
                  name: api-gateway-secrets
                  key: jwt-secret
          resources:
            requests:
              cpu: "250m"
              memory: "512Mi"
            limits:
              cpu: "1000m"
              memory: "1Gi"
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
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop:
                - ALL
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
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: api-gateway
                topologyKey: kubernetes.io/hostname
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: ScheduleAnyway
          labelSelector:
            matchLabels:
              app: api-gateway
---
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  type: ClusterIP
  ports:
    - name: http
      port: 80
      targetPort: http
    - name: metrics
      port: 9090
      targetPort: metrics
  selector:
    app: api-gateway
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-gateway
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
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
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max
---
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: api-gateway
```

### 2.3 Service Account with IRSA

```yaml
# k8s/services/api-gateway/service-account.yaml

apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-gateway
  namespace: mindweave-services
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT_ID:role/mindweave-production-api-gateway-role
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: api-gateway
  namespace: mindweave-services
rules:
  - apiGroups: [""]
    resources: ["configmaps"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    resourceNames: ["api-gateway-secrets"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-gateway
  namespace: mindweave-services
subjects:
  - kind: ServiceAccount
    name: api-gateway
roleRef:
  kind: Role
  name: api-gateway
  apiGroup: rbac.authorization.k8s.io
```

---

## 3. Deployment Strategies

### 3.1 Blue-Green Deployment

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       BLUE-GREEN DEPLOYMENT                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                          ┌──────────────┐                                   │
│                          │   Ingress    │                                   │
│                          │  Controller  │                                   │
│                          └──────┬───────┘                                   │
│                                 │                                           │
│                     ┌───────────┴───────────┐                               │
│                     │                       │                               │
│              ┌──────▼──────┐         ┌──────▼──────┐                       │
│              │   Service   │         │   Service   │                       │
│              │   (Blue)    │         │  (Green)    │                       │
│              │  ACTIVE     │         │  STANDBY    │                       │
│              └──────┬──────┘         └──────┬──────┘                       │
│                     │                       │                               │
│         ┌───────────┼───────────┐   ┌──────┼───────────┐                   │
│         │           │           │   │      │           │                   │
│    ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐            │
│    │  Pod    │ │  Pod    │ │  Pod    │ │  Pod    │ │  Pod    │            │
│    │  v1.0   │ │  v1.0   │ │  v1.0   │ │  v1.1   │ │  v1.1   │            │
│    └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘            │
│                                                                              │
│    CUTOVER: Switch service selector from blue to green                      │
│    ROLLBACK: Switch service selector back to blue                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

```yaml
# k8s/deployments/blue-green/blue-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway-blue
  namespace: mindweave-services
  labels:
    app: api-gateway
    slot: blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-gateway
      slot: blue
  template:
    metadata:
      labels:
        app: api-gateway
        slot: blue
        version: v1.0.0
    spec:
      containers:
        - name: api-gateway
          image: mindweave/api-gateway:v1.0.0
          # ... rest of container spec
---
# k8s/deployments/blue-green/green-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway-green
  namespace: mindweave-services
  labels:
    app: api-gateway
    slot: green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api-gateway
      slot: green
  template:
    metadata:
      labels:
        app: api-gateway
        slot: green
        version: v1.1.0
    spec:
      containers:
        - name: api-gateway
          image: mindweave/api-gateway:v1.1.0
          # ... rest of container spec
---
# k8s/deployments/blue-green/active-service.yaml

apiVersion: v1
kind: Service
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  type: ClusterIP
  selector:
    app: api-gateway
    slot: blue  # Change to 'green' for cutover
  ports:
    - name: http
      port: 80
      targetPort: 3000
```

### 3.2 Canary Deployment with Istio

```yaml
# k8s/deployments/canary/virtual-service.yaml

apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  hosts:
    - api-gateway
    - api.mindweave.io
  gateways:
    - mindweave-gateway
  http:
    - match:
        - headers:
            x-canary:
              exact: "true"
      route:
        - destination:
            host: api-gateway
            subset: canary
    - route:
        - destination:
            host: api-gateway
            subset: stable
          weight: 95
        - destination:
            host: api-gateway
            subset: canary
          weight: 5
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  host: api-gateway
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 100
      http:
        h2UpgradePolicy: UPGRADE
        http1MaxPendingRequests: 100
        http2MaxRequests: 1000
    loadBalancer:
      simple: LEAST_REQUEST
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 30s
      maxEjectionPercent: 50
  subsets:
    - name: stable
      labels:
        version: stable
    - name: canary
      labels:
        version: canary
```

### 3.3 Canary Analysis with Flagger

```yaml
# k8s/deployments/canary/flagger-canary.yaml

apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: api-gateway
  namespace: mindweave-services
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-gateway
  progressDeadlineSeconds: 600
  service:
    port: 80
    targetPort: 3000
    gateways:
      - mindweave-gateway
    hosts:
      - api.mindweave.io
    trafficPolicy:
      tls:
        mode: ISTIO_MUTUAL
  analysis:
    interval: 1m
    threshold: 5
    maxWeight: 50
    stepWeight: 10
    metrics:
      - name: request-success-rate
        thresholdRange:
          min: 99
        interval: 1m
      - name: request-duration
        thresholdRange:
          max: 500
        interval: 1m
    webhooks:
      - name: acceptance-test
        type: pre-rollout
        url: http://flagger-loadtester.mindweave-system/
        timeout: 30s
        metadata:
          type: bash
          cmd: "curl -s http://api-gateway-canary.mindweave-services/health/ready"
      - name: load-test
        type: rollout
        url: http://flagger-loadtester.mindweave-system/
        timeout: 5s
        metadata:
          type: cmd
          cmd: "hey -z 1m -q 10 -c 2 http://api-gateway-canary.mindweave-services/"
---
# Custom Prometheus Metrics for Canary Analysis
apiVersion: flagger.app/v1beta1
kind: MetricTemplate
metadata:
  name: request-success-rate
  namespace: mindweave-system
spec:
  provider:
    type: prometheus
    address: http://prometheus.mindweave-monitoring:9090
  query: |
    sum(rate(istio_requests_total{
      destination_workload_namespace="{{ namespace }}",
      destination_workload="{{ target }}",
      response_code!~"5.*"
    }[{{ interval }}])) /
    sum(rate(istio_requests_total{
      destination_workload_namespace="{{ namespace }}",
      destination_workload="{{ target }}"
    }[{{ interval }}])) * 100
---
apiVersion: flagger.app/v1beta1
kind: MetricTemplate
metadata:
  name: request-duration
  namespace: mindweave-system
spec:
  provider:
    type: prometheus
    address: http://prometheus.mindweave-monitoring:9090
  query: |
    histogram_quantile(0.99, sum(rate(istio_request_duration_milliseconds_bucket{
      destination_workload_namespace="{{ namespace }}",
      destination_workload="{{ target }}"
    }[{{ interval }}])) by (le))
```

---

## 4. GitOps with ArgoCD

### 4.1 ArgoCD Application

```yaml
# argocd/applications/mindweave-services.yaml

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: mindweave-services
  namespace: argocd
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: mindweave
  source:
    repoURL: https://github.com/mindweave/platform.git
    targetRevision: HEAD
    path: k8s/services
    directory:
      recurse: true
  destination:
    server: https://kubernetes.default.svc
    namespace: mindweave-services
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
      - CreateNamespace=true
      - PrunePropagationPolicy=foreground
      - PruneLast=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
  revisionHistoryLimit: 10
---
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: mindweave-microservices
  namespace: argocd
spec:
  generators:
    - git:
        repoURL: https://github.com/mindweave/platform.git
        revision: HEAD
        directories:
          - path: k8s/services/*
  template:
    metadata:
      name: '{{path.basename}}'
      namespace: argocd
    spec:
      project: mindweave
      source:
        repoURL: https://github.com/mindweave/platform.git
        targetRevision: HEAD
        path: '{{path}}'
      destination:
        server: https://kubernetes.default.svc
        namespace: mindweave-services
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
```

### 4.2 ArgoCD Project

```yaml
# argocd/projects/mindweave.yaml

apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: mindweave
  namespace: argocd
spec:
  description: MindWeave Platform Project
  sourceRepos:
    - https://github.com/mindweave/platform.git
    - https://github.com/mindweave/infrastructure.git
  destinations:
    - namespace: mindweave-*
      server: https://kubernetes.default.svc
    - namespace: istio-system
      server: https://kubernetes.default.svc
  clusterResourceWhitelist:
    - group: ''
      kind: Namespace
    - group: networking.istio.io
      kind: '*'
    - group: security.istio.io
      kind: '*'
  namespaceResourceWhitelist:
    - group: ''
      kind: '*'
    - group: apps
      kind: '*'
    - group: autoscaling
      kind: '*'
    - group: batch
      kind: '*'
    - group: networking.k8s.io
      kind: '*'
    - group: policy
      kind: '*'
  roles:
    - name: admin
      description: Admin privileges for mindweave project
      policies:
        - p, proj:mindweave:admin, applications, *, mindweave/*, allow
      groups:
        - mindweave-platform-admins
    - name: developer
      description: Developer privileges
      policies:
        - p, proj:mindweave:developer, applications, get, mindweave/*, allow
        - p, proj:mindweave:developer, applications, sync, mindweave/*, allow
      groups:
        - mindweave-developers
```

---

## 5. Rollback Procedures

### 5.1 Automated Rollback Script

```bash
#!/bin/bash
# scripts/rollback.sh

set -euo pipefail

# Configuration
NAMESPACE="${NAMESPACE:-mindweave-services}"
SERVICE="${SERVICE:-api-gateway}"
ROLLBACK_REVISION="${ROLLBACK_REVISION:-}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Get current deployment info
get_current_revision() {
    kubectl get deployment "$SERVICE" -n "$NAMESPACE" \
        -o jsonpath='{.metadata.annotations.deployment\.kubernetes\.io/revision}'
}

# Get deployment history
get_deployment_history() {
    log_info "Deployment History for $SERVICE:"
    kubectl rollout history deployment/"$SERVICE" -n "$NAMESPACE"
}

# Rollback to previous revision
rollback_deployment() {
    local target_revision="${1:-}"

    if [[ -n "$target_revision" ]]; then
        log_info "Rolling back $SERVICE to revision $target_revision..."
        kubectl rollout undo deployment/"$SERVICE" -n "$NAMESPACE" \
            --to-revision="$target_revision"
    else
        log_info "Rolling back $SERVICE to previous revision..."
        kubectl rollout undo deployment/"$SERVICE" -n "$NAMESPACE"
    fi
}

# Wait for rollback to complete
wait_for_rollback() {
    log_info "Waiting for rollback to complete..."
    kubectl rollout status deployment/"$SERVICE" -n "$NAMESPACE" --timeout=300s
}

# Verify rollback health
verify_health() {
    log_info "Verifying service health..."

    local ready_pods
    ready_pods=$(kubectl get deployment "$SERVICE" -n "$NAMESPACE" \
        -o jsonpath='{.status.readyReplicas}')

    local desired_pods
    desired_pods=$(kubectl get deployment "$SERVICE" -n "$NAMESPACE" \
        -o jsonpath='{.spec.replicas}')

    if [[ "$ready_pods" == "$desired_pods" ]]; then
        log_info "All $ready_pods/$desired_pods pods are ready"
        return 0
    else
        log_error "Only $ready_pods/$desired_pods pods are ready"
        return 1
    fi
}

# Run health checks
run_health_checks() {
    log_info "Running health checks..."

    local pod
    pod=$(kubectl get pods -n "$NAMESPACE" -l "app=$SERVICE" \
        -o jsonpath='{.items[0].metadata.name}')

    # Liveness check
    if kubectl exec -n "$NAMESPACE" "$pod" -- \
        curl -sf http://localhost:3000/health/live > /dev/null 2>&1; then
        log_info "Liveness check passed"
    else
        log_error "Liveness check failed"
        return 1
    fi

    # Readiness check
    if kubectl exec -n "$NAMESPACE" "$pod" -- \
        curl -sf http://localhost:3000/health/ready > /dev/null 2>&1; then
        log_info "Readiness check passed"
    else
        log_error "Readiness check failed"
        return 1
    fi
}

# Create rollback notification
send_notification() {
    local status="$1"
    local message="$2"

    # Slack notification
    if [[ -n "${SLACK_WEBHOOK_URL:-}" ]]; then
        curl -X POST -H 'Content-type: application/json' \
            --data "{
                \"text\": \"Deployment Rollback: $SERVICE\",
                \"attachments\": [{
                    \"color\": \"$([ "$status" == "success" ] && echo "good" || echo "danger")\",
                    \"fields\": [{
                        \"title\": \"Status\",
                        \"value\": \"$status\",
                        \"short\": true
                    }, {
                        \"title\": \"Service\",
                        \"value\": \"$SERVICE\",
                        \"short\": true
                    }, {
                        \"title\": \"Namespace\",
                        \"value\": \"$NAMESPACE\",
                        \"short\": true
                    }, {
                        \"title\": \"Message\",
                        \"value\": \"$message\",
                        \"short\": false
                    }]
                }]
            }" \
            "$SLACK_WEBHOOK_URL"
    fi

    # PagerDuty incident
    if [[ "$status" == "failure" && -n "${PAGERDUTY_KEY:-}" ]]; then
        curl -X POST \
            -H 'Content-Type: application/json' \
            -d "{
                \"routing_key\": \"$PAGERDUTY_KEY\",
                \"event_action\": \"trigger\",
                \"payload\": {
                    \"summary\": \"Rollback failed for $SERVICE\",
                    \"severity\": \"critical\",
                    \"source\": \"kubernetes-rollback\",
                    \"custom_details\": {
                        \"service\": \"$SERVICE\",
                        \"namespace\": \"$NAMESPACE\",
                        \"message\": \"$message\"
                    }
                }
            }" \
            https://events.pagerduty.com/v2/enqueue
    fi
}

# Main execution
main() {
    log_info "Starting rollback procedure for $SERVICE in $NAMESPACE"

    # Show current state
    local current_revision
    current_revision=$(get_current_revision)
    log_info "Current revision: $current_revision"

    # Show history
    get_deployment_history

    # Perform rollback
    rollback_deployment "$ROLLBACK_REVISION"

    # Wait for completion
    if wait_for_rollback; then
        log_info "Rollback completed successfully"
    else
        log_error "Rollback failed to complete in time"
        send_notification "failure" "Rollback timed out"
        exit 1
    fi

    # Verify health
    if verify_health && run_health_checks; then
        log_info "Rollback verified successfully"
        send_notification "success" "Rollback completed and verified"
    else
        log_error "Health verification failed after rollback"
        send_notification "failure" "Health checks failed after rollback"
        exit 1
    fi

    # Show new state
    local new_revision
    new_revision=$(get_current_revision)
    log_info "New revision: $new_revision"
}

main "$@"
```

### 5.2 ArgoCD Rollback

```yaml
# argocd/rollback-job.yaml

apiVersion: batch/v1
kind: Job
metadata:
  name: argocd-rollback
  namespace: argocd
spec:
  template:
    spec:
      serviceAccountName: argocd-admin
      containers:
        - name: rollback
          image: argoproj/argocd:v2.9.0
          command:
            - /bin/sh
            - -c
            - |
              # Login to ArgoCD
              argocd login argocd-server.argocd.svc.cluster.local \
                --username admin \
                --password "${ARGOCD_PASSWORD}" \
                --insecure

              # Get application history
              argocd app history "${APP_NAME}"

              # Rollback to specified revision
              argocd app rollback "${APP_NAME}" "${REVISION}"

              # Wait for sync
              argocd app wait "${APP_NAME}" --health --timeout 300
          env:
            - name: APP_NAME
              value: "mindweave-services"
            - name: REVISION
              value: "1"  # Revision to rollback to
            - name: ARGOCD_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: argocd-initial-admin-secret
                  key: password
      restartPolicy: Never
  backoffLimit: 2
```

---

## 6. Environment Promotion

### 6.1 Promotion Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ENVIRONMENT PROMOTION FLOW                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                           DEV ENVIRONMENT                            │   │
│  │                                                                       │   │
│  │   • Automatic deployment on merge to main                            │   │
│  │   • Feature branches auto-deploy to preview                          │   │
│  │   • Unit tests, integration tests                                    │   │
│  │   • Code quality gates (lint, security scan)                        │   │
│  │                                                                       │   │
│  └───────────────────────────┬─────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼ Automatic (on passing tests)                 │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        STAGING ENVIRONMENT                           │   │
│  │                                                                       │   │
│  │   • Production-like configuration                                    │   │
│  │   • Full E2E test suite execution                                   │   │
│  │   • Performance testing                                              │   │
│  │   • Security scanning (DAST)                                        │   │
│  │   • Minimum 24-hour soak time                                       │   │
│  │                                                                       │   │
│  └───────────────────────────┬─────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼ Manual Approval Required                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      PRODUCTION ENVIRONMENT                          │   │
│  │                                                                       │   │
│  │   • Canary deployment (5% → 25% → 50% → 100%)                       │   │
│  │   • Real-time metrics monitoring                                     │   │
│  │   • Automatic rollback on error threshold                           │   │
│  │   • Post-deployment smoke tests                                     │   │
│  │                                                                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Promotion Configuration

```yaml
# .github/workflows/promote.yaml

name: Environment Promotion

on:
  workflow_dispatch:
    inputs:
      target_environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production
      version:
        description: 'Version to promote (e.g., v1.2.3)'
        required: true
        type: string

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate version exists
        run: |
          # Check if the version tag exists
          if ! git rev-parse "refs/tags/${{ inputs.version }}" >/dev/null 2>&1; then
            echo "Error: Version ${{ inputs.version }} does not exist"
            exit 1
          fi

      - name: Check source environment
        run: |
          if [[ "${{ inputs.target_environment }}" == "staging" ]]; then
            SOURCE_ENV="dev"
          elif [[ "${{ inputs.target_environment }}" == "production" ]]; then
            SOURCE_ENV="staging"
          fi

          # Verify version is deployed in source environment
          DEPLOYED_VERSION=$(kubectl get deployment api-gateway \
            -n mindweave-services \
            --context "${SOURCE_ENV}" \
            -o jsonpath='{.spec.template.spec.containers[0].image}' | \
            cut -d: -f2)

          if [[ "$DEPLOYED_VERSION" != "${{ inputs.version }}" ]]; then
            echo "Warning: Version ${{ inputs.version }} not deployed in $SOURCE_ENV"
            echo "Currently deployed: $DEPLOYED_VERSION"
          fi

  promote-to-staging:
    if: inputs.target_environment == 'staging'
    needs: validate
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v4

      - name: Update staging manifests
        run: |
          cd k8s/environments/staging
          kustomize edit set image mindweave/*=*:${{ inputs.version }}

      - name: Create PR for staging
        uses: peter-evans/create-pull-request@v5
        with:
          commit-message: "chore: promote ${{ inputs.version }} to staging"
          title: "Promote ${{ inputs.version }} to Staging"
          branch: promote-staging-${{ inputs.version }}
          base: main

  promote-to-production:
    if: inputs.target_environment == 'production'
    needs: validate
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4

      - name: Verify staging deployment
        run: |
          # Get staging version
          STAGING_VERSION=$(kubectl get deployment api-gateway \
            -n mindweave-services \
            --context staging \
            -o jsonpath='{.spec.template.spec.containers[0].image}' | \
            cut -d: -f2)

          if [[ "$STAGING_VERSION" != "${{ inputs.version }}" ]]; then
            echo "Error: Version ${{ inputs.version }} not in staging"
            exit 1
          fi

      - name: Check staging soak time
        run: |
          DEPLOY_TIME=$(kubectl get deployment api-gateway \
            -n mindweave-services \
            --context staging \
            -o jsonpath='{.metadata.creationTimestamp}')

          DEPLOY_EPOCH=$(date -d "$DEPLOY_TIME" +%s)
          NOW_EPOCH=$(date +%s)
          HOURS_DEPLOYED=$(( (NOW_EPOCH - DEPLOY_EPOCH) / 3600 ))

          if [[ $HOURS_DEPLOYED -lt 24 ]]; then
            echo "Error: Version deployed for only $HOURS_DEPLOYED hours"
            echo "Minimum 24 hours required before production promotion"
            exit 1
          fi

      - name: Update production manifests
        run: |
          cd k8s/environments/production
          kustomize edit set image mindweave/*=*:${{ inputs.version }}

      - name: Create PR for production
        uses: peter-evans/create-pull-request@v5
        with:
          commit-message: "chore: promote ${{ inputs.version }} to production"
          title: "Promote ${{ inputs.version }} to Production"
          branch: promote-production-${{ inputs.version }}
          base: main
          reviewers: platform-leads
```

---

## 7. Deployment Checklist

### 7.1 Pre-Deployment

| Step | Description | Owner | Required |
|------|-------------|-------|----------|
| 1 | All tests passing in CI | Developer | Yes |
| 2 | Security scan completed | Security | Yes |
| 3 | Code review approved | Tech Lead | Yes |
| 4 | Change request approved | Release Manager | Yes |
| 5 | Runbook updated | SRE | Conditional |
| 6 | Database migrations tested | DBA | Conditional |
| 7 | Feature flags configured | Product | Conditional |
| 8 | Monitoring dashboards ready | SRE | Yes |
| 9 | Rollback plan documented | SRE | Yes |

### 7.2 During Deployment

| Step | Description | Owner | Required |
|------|-------------|-------|----------|
| 1 | Notify stakeholders | Release Manager | Yes |
| 2 | Create deployment ticket | Release Manager | Yes |
| 3 | Execute deployment | SRE | Yes |
| 4 | Monitor canary metrics | SRE | Yes |
| 5 | Run smoke tests | QA | Yes |
| 6 | Verify health checks | SRE | Yes |
| 7 | Monitor error rates | SRE | Yes |
| 8 | Gradual traffic shift | SRE | Yes |

### 7.3 Post-Deployment

| Step | Description | Owner | Required |
|------|-------------|-------|----------|
| 1 | Verify all replicas healthy | SRE | Yes |
| 2 | Confirm no increase in errors | SRE | Yes |
| 3 | Run integration tests | QA | Yes |
| 4 | Update deployment ticket | Release Manager | Yes |
| 5 | Notify completion | Release Manager | Yes |
| 6 | Clean up old resources | SRE | Yes |
| 7 | Update documentation | Developer | Conditional |
| 8 | Post-mortem if issues | SRE | Conditional |

---

## 8. Multi-Region Deployment

### 8.1 Region Configuration

```yaml
# k8s/multi-region/region-config.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: region-config
  namespace: mindweave-system
data:
  regions.yaml: |
    regions:
      - name: us-east-1
        role: primary
        weight: 50
        failover_priority: 1
        endpoints:
          api: api-use1.mindweave.io
          internal: api-gateway.mindweave-services.svc.cluster.local
        database:
          primary: true
          endpoint: mindweave-use1.cluster-xxx.us-east-1.rds.amazonaws.com
        redis:
          endpoint: mindweave-use1.xxx.cache.amazonaws.com

      - name: us-west-2
        role: secondary
        weight: 30
        failover_priority: 2
        endpoints:
          api: api-usw2.mindweave.io
          internal: api-gateway.mindweave-services.svc.cluster.local
        database:
          primary: false
          endpoint: mindweave-usw2.cluster-ro-xxx.us-west-2.rds.amazonaws.com
        redis:
          endpoint: mindweave-usw2.xxx.cache.amazonaws.com

      - name: eu-west-1
        role: eu-data
        weight: 20
        failover_priority: 3
        endpoints:
          api: api-euw1.mindweave.io
          internal: api-gateway.mindweave-services.svc.cluster.local
        database:
          primary: true  # EU data sovereignty
          endpoint: mindweave-euw1.cluster-xxx.eu-west-1.rds.amazonaws.com
        redis:
          endpoint: mindweave-euw1.xxx.cache.amazonaws.com
```

### 8.2 Global Load Balancer

```hcl
# modules/global-lb/main.tf

# Route 53 Health Checks
resource "aws_route53_health_check" "us_east_1" {
  fqdn              = "api-use1.mindweave.io"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health/ready"
  failure_threshold = 3
  request_interval  = 10

  tags = {
    Name = "mindweave-us-east-1-health-check"
  }
}

resource "aws_route53_health_check" "us_west_2" {
  fqdn              = "api-usw2.mindweave.io"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health/ready"
  failure_threshold = 3
  request_interval  = 10

  tags = {
    Name = "mindweave-us-west-2-health-check"
  }
}

resource "aws_route53_health_check" "eu_west_1" {
  fqdn              = "api-euw1.mindweave.io"
  port              = 443
  type              = "HTTPS"
  resource_path     = "/health/ready"
  failure_threshold = 3
  request_interval  = 10

  tags = {
    Name = "mindweave-eu-west-1-health-check"
  }
}

# Latency-based routing with failover
resource "aws_route53_record" "api" {
  zone_id = var.route53_zone_id
  name    = "api.mindweave.io"
  type    = "A"

  latency_routing_policy {
    region = "us-east-1"
  }

  set_identifier  = "us-east-1"
  health_check_id = aws_route53_health_check.us_east_1.id

  alias {
    name                   = var.alb_dns_name_use1
    zone_id                = var.alb_zone_id_use1
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "api_usw2" {
  zone_id = var.route53_zone_id
  name    = "api.mindweave.io"
  type    = "A"

  latency_routing_policy {
    region = "us-west-2"
  }

  set_identifier  = "us-west-2"
  health_check_id = aws_route53_health_check.us_west_2.id

  alias {
    name                   = var.alb_dns_name_usw2
    zone_id                = var.alb_zone_id_usw2
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "api_euw1" {
  zone_id = var.route53_zone_id
  name    = "api.mindweave.io"
  type    = "A"

  latency_routing_policy {
    region = "eu-west-1"
  }

  set_identifier  = "eu-west-1"
  health_check_id = aws_route53_health_check.eu_west_1.id

  alias {
    name                   = var.alb_dns_name_euw1
    zone_id                = var.alb_zone_id_euw1
    evaluate_target_health = true
  }
}

# Geolocation routing for EU data sovereignty
resource "aws_route53_record" "api_eu_geo" {
  zone_id = var.route53_zone_id
  name    = "api.mindweave.io"
  type    = "A"

  geolocation_routing_policy {
    continent = "EU"
  }

  set_identifier  = "eu-geo"
  health_check_id = aws_route53_health_check.eu_west_1.id

  alias {
    name                   = var.alb_dns_name_euw1
    zone_id                = var.alb_zone_id_euw1
    evaluate_target_health = true
  }
}
```

---

## 9. Deployment Metrics

### 9.1 Key Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Deployment Frequency | Daily | Deployments per day |
| Lead Time | < 1 hour | Commit to production |
| Change Failure Rate | < 5% | Failed deployments / total |
| MTTR | < 15 minutes | Mean time to recovery |
| Rollback Rate | < 2% | Rollbacks / total deploys |
| Canary Success Rate | > 98% | Successful canaries |

### 9.2 Deployment Dashboard

```yaml
# grafana/dashboards/deployments.yaml

apiVersion: v1
kind: ConfigMap
metadata:
  name: deployment-dashboard
  namespace: mindweave-monitoring
  labels:
    grafana_dashboard: "1"
data:
  deployment-dashboard.json: |
    {
      "title": "Deployment Metrics",
      "panels": [
        {
          "title": "Deployment Frequency",
          "type": "stat",
          "targets": [
            {
              "expr": "sum(increase(argocd_app_sync_total{project=\"mindweave\"}[24h]))"
            }
          ]
        },
        {
          "title": "Deployment Success Rate",
          "type": "gauge",
          "targets": [
            {
              "expr": "sum(argocd_app_sync_total{status=\"Succeeded\",project=\"mindweave\"}) / sum(argocd_app_sync_total{project=\"mindweave\"}) * 100"
            }
          ]
        },
        {
          "title": "Canary Analysis Results",
          "type": "timeseries",
          "targets": [
            {
              "expr": "sum by (name, result) (flagger_canary_total{namespace=\"mindweave-services\"})"
            }
          ]
        },
        {
          "title": "Rollback Count (7d)",
          "type": "stat",
          "targets": [
            {
              "expr": "sum(increase(kubernetes_deployment_rollback_total{namespace=\"mindweave-services\"}[7d]))"
            }
          ]
        }
      ]
    }
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | Overall system design |
| [DEVOPS-CICD.md](./DEVOPS-CICD.md) | CI/CD pipeline configuration |
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Monitoring and alerting |
| [INCIDENT-RESPONSE.md](./INCIDENT-RESPONSE.md) | Incident handling procedures |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security controls |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Platform Engineering | Initial deployment strategy |
