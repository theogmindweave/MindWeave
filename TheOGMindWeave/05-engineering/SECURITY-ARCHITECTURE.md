# MindWeave Security Architecture

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-009 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's comprehensive security architecture, including defense-in-depth strategies, data protection, compliance controls, and incident response procedures. Security is foundational for an enterprise AI governance platform handling sensitive customer data.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SECURITY ARCHITECTURE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    LAYER 1: PERIMETER                                │   │
│  │  WAF │ DDoS Protection │ CDN │ TLS 1.3 │ Certificate Pinning        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    LAYER 2: NETWORK                                  │   │
│  │  VPC Isolation │ Security Groups │ NACLs │ Private Subnets          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    LAYER 3: APPLICATION                              │   │
│  │  Authentication │ Authorization │ Input Validation │ Rate Limiting   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    LAYER 4: DATA                                     │   │
│  │  Encryption at Rest │ Encryption in Transit │ Key Management        │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                      │                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    LAYER 5: MONITORING                               │   │
│  │  SIEM │ Threat Detection │ Audit Logging │ Alerting                 │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Security Principles

### 1.1 Core Principles

| Principle | Description | Implementation |
|-----------|-------------|----------------|
| **Defense in Depth** | Multiple security layers | 5-layer security model |
| **Least Privilege** | Minimal required access | RBAC + Just-in-time access |
| **Zero Trust** | Never trust, always verify | mTLS, continuous auth |
| **Secure by Default** | Security enabled by default | Secure configurations |
| **Fail Secure** | Safe failure modes | Deny-by-default |
| **Audit Everything** | Complete audit trail | Immutable audit logs |

### 1.2 Security Requirements

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      SECURITY REQUIREMENTS                                  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CONFIDENTIALITY                                                           │
│  ───────────────                                                           │
│  • All data encrypted at rest (AES-256)                                   │
│  • All data encrypted in transit (TLS 1.3)                                │
│  • PII masked in logs                                                      │
│  • Secrets managed via secure vault                                        │
│                                                                             │
│  INTEGRITY                                                                 │
│  ─────────                                                                 │
│  • Input validation on all endpoints                                      │
│  • Database constraints and triggers                                      │
│  • Immutable audit logs                                                   │
│  • Code signing for releases                                              │
│                                                                             │
│  AVAILABILITY                                                              │
│  ────────────                                                              │
│  • 99.9% uptime SLA                                                       │
│  • DDoS protection                                                        │
│  • Multi-AZ deployment                                                    │
│  • Automated failover                                                     │
│                                                                             │
│  COMPLIANCE                                                                │
│  ──────────                                                                │
│  • SOC 2 Type II                                                          │
│  • GDPR compliant                                                         │
│  • CCPA compliant                                                         │
│  • HIPAA ready (Enterprise)                                               │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Perimeter Security

### 2.1 Web Application Firewall (WAF)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         WAF CONFIGURATION                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  AWS WAF RULES:                                                            │
│  ──────────────                                                            │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  RULE                          ACTION      PRIORITY                  │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  AWS Managed - Known Bad Input  Block       1                       │   │
│  │  AWS Managed - SQL Injection    Block       2                       │   │
│  │  AWS Managed - XSS              Block       3                       │   │
│  │  AWS Managed - Core Rule Set    Block       4                       │   │
│  │  Rate Limit (IP)                Rate 2000/5min  5                   │   │
│  │  Geo Block (Sanctioned)         Block       6                       │   │
│  │  Bot Control                    Challenge   7                       │   │
│  │  API Gateway Integration        Allow       99                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  CUSTOM RULES:                                                             │
│  ─────────────                                                             │
│                                                                             │
│  • Block requests with suspicious headers                                 │
│  • Block oversized request bodies (>10MB)                                 │
│  • Block requests without valid User-Agent                                │
│  • Challenge requests from Tor exit nodes                                 │
│  • Rate limit authentication endpoints                                    │
│                                                                             │
│  LOGGING:                                                                  │
│  ────────                                                                  │
│                                                                             │
│  • All blocked requests logged to S3                                      │
│  • Real-time alerts for attack patterns                                   │
│  • Weekly WAF rule effectiveness review                                   │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 DDoS Protection

| Layer | Protection | Provider |
|-------|------------|----------|
| L3/L4 | Network floods | AWS Shield Standard |
| L7 | Application attacks | AWS Shield Advanced + WAF |
| DNS | DNS amplification | Route 53 Resolver |
| CDN | Origin protection | CloudFront |

### 2.3 TLS Configuration

```yaml
# TLS Configuration
tls:
  minimum_version: TLS1.3
  cipher_suites:
    - TLS_AES_256_GCM_SHA384
    - TLS_AES_128_GCM_SHA256
    - TLS_CHACHA20_POLY1305_SHA256

  # Certificate configuration
  certificate:
    issuer: "AWS Certificate Manager"
    key_algorithm: "ECDSA P-384"
    auto_renewal: true
    ocsp_stapling: true

  # HSTS
  hsts:
    enabled: true
    max_age: 31536000  # 1 year
    include_subdomains: true
    preload: true
```

---

## 3. Network Security

### 3.1 VPC Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         VPC ARCHITECTURE                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                        VPC: 10.0.0.0/16                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  PUBLIC SUBNETS                                                     │   │
│  │  ─────────────────                                                  │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│  │  │  10.0.1.0/24    │  │  10.0.2.0/24    │  │  10.0.3.0/24    │     │   │
│  │  │  us-east-1a     │  │  us-east-1b     │  │  us-east-1c     │     │   │
│  │  │                 │  │                 │  │                 │     │   │
│  │  │  • ALB          │  │  • ALB          │  │  • ALB          │     │   │
│  │  │  • NAT Gateway  │  │  • NAT Gateway  │  │                 │     │   │
│  │  │  • Bastion      │  │                 │  │                 │     │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│  │                                                                      │   │
│  │  PRIVATE SUBNETS (Applications)                                     │   │
│  │  ─────────────────────────────────                                  │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│  │  │  10.0.10.0/24   │  │  10.0.11.0/24   │  │  10.0.12.0/24   │     │   │
│  │  │  us-east-1a     │  │  us-east-1b     │  │  us-east-1c     │     │   │
│  │  │                 │  │                 │  │                 │     │   │
│  │  │  • EKS Nodes    │  │  • EKS Nodes    │  │  • EKS Nodes    │     │   │
│  │  │  • Services     │  │  • Services     │  │  • Services     │     │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│  │                                                                      │   │
│  │  PRIVATE SUBNETS (Data)                                             │   │
│  │  ─────────────────────────                                          │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐     │   │
│  │  │  10.0.20.0/24   │  │  10.0.21.0/24   │  │  10.0.22.0/24   │     │   │
│  │  │  us-east-1a     │  │  us-east-1b     │  │  us-east-1c     │     │   │
│  │  │                 │  │                 │  │                 │     │   │
│  │  │  • RDS Primary  │  │  • RDS Replica  │  │  • ElastiCache  │     │   │
│  │  │  • TimescaleDB  │  │  • MSK Kafka    │  │  • MSK Kafka    │     │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘     │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  VPC ENDPOINTS:                                                            │
│  ──────────────                                                            │
│  • S3 Gateway Endpoint                                                     │
│  • ECR Interface Endpoint                                                  │
│  • Secrets Manager Interface Endpoint                                     │
│  • KMS Interface Endpoint                                                 │
│  • CloudWatch Logs Interface Endpoint                                     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Security Groups

```hcl
# API Service Security Group
resource "aws_security_group" "api_service" {
  name        = "mindweave-api-service"
  description = "Security group for API services"
  vpc_id      = aws_vpc.main.id

  # Inbound from ALB only
  ingress {
    from_port       = 3000
    to_port         = 3000
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
    description     = "API traffic from ALB"
  }

  # Inbound from other services (internal)
  ingress {
    from_port   = 3000
    to_port     = 3009
    protocol    = "tcp"
    self        = true
    description = "Internal service communication"
  }

  # Outbound to database
  egress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.database.id]
    description     = "PostgreSQL access"
  }

  # Outbound to Redis
  egress {
    from_port       = 6379
    to_port         = 6379
    protocol        = "tcp"
    security_groups = [aws_security_group.redis.id]
    description     = "Redis access"
  }

  # Outbound to Kafka
  egress {
    from_port       = 9092
    to_port         = 9094
    protocol        = "tcp"
    security_groups = [aws_security_group.kafka.id]
    description     = "Kafka access"
  }

  # Outbound HTTPS (external APIs)
  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "HTTPS outbound"
  }

  tags = {
    Name = "mindweave-api-service"
  }
}

# Database Security Group
resource "aws_security_group" "database" {
  name        = "mindweave-database"
  description = "Security group for databases"
  vpc_id      = aws_vpc.main.id

  # Only from API services
  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.api_service.id]
    description     = "PostgreSQL from API services"
  }

  # No outbound internet access
  # Only VPC-internal replication
  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    self        = true
    description = "Database replication"
  }

  tags = {
    Name = "mindweave-database"
  }
}
```

---

## 4. Application Security

### 4.1 OWASP Top 10 Mitigations

| Vulnerability | Mitigation |
|---------------|------------|
| **Injection** | Parameterized queries, input validation |
| **Broken Authentication** | MFA, secure session management |
| **Sensitive Data Exposure** | Encryption, data masking |
| **XXE** | Disabled XML external entities |
| **Broken Access Control** | RBAC, resource authorization |
| **Security Misconfiguration** | Hardened configs, security scanning |
| **XSS** | Output encoding, CSP headers |
| **Insecure Deserialization** | Schema validation, allowlists |
| **Using Vulnerable Components** | Dependency scanning, updates |
| **Insufficient Logging** | Comprehensive audit logging |

### 4.2 Input Validation

```typescript
// Comprehensive input validation middleware
import { z } from 'zod';

// Schema definitions
const schemas = {
  // User creation
  createUser: z.object({
    email: z.string()
      .email('Invalid email format')
      .max(255)
      .transform(e => e.toLowerCase()),
    password: z.string()
      .min(10, 'Password must be at least 10 characters')
      .regex(/[A-Z]/, 'Password must contain uppercase letter')
      .regex(/[a-z]/, 'Password must contain lowercase letter')
      .regex(/[0-9]/, 'Password must contain number')
      .regex(/[^A-Za-z0-9]/, 'Password must contain special character'),
    name: z.string()
      .min(1)
      .max(100)
      .regex(/^[a-zA-Z\s'-]+$/, 'Invalid characters in name'),
  }),

  // API request
  apiRequest: z.object({
    model: z.enum(['claude-3-opus', 'claude-3-sonnet', 'claude-3-haiku']),
    messages: z.array(z.object({
      role: z.enum(['user', 'assistant', 'system']),
      content: z.string().max(100000),
    })).max(100),
    max_tokens: z.number().int().positive().max(4096),
  }),

  // Project creation
  createProject: z.object({
    name: z.string()
      .min(1)
      .max(100)
      .regex(/^[\w\s-]+$/, 'Invalid project name'),
    slug: z.string()
      .min(1)
      .max(50)
      .regex(/^[a-z0-9-]+$/, 'Slug must be lowercase alphanumeric'),
    settings: z.object({
      allowedModels: z.array(z.string()).optional(),
      mcpAutoApprove: z.boolean().optional(),
    }).optional(),
  }),
};

// Validation middleware
export const validate = (schemaName: keyof typeof schemas) => {
  return async (req: Request, res: Response, next: NextFunction) => {
    try {
      const schema = schemas[schemaName];
      req.body = await schema.parseAsync(req.body);
      next();
    } catch (error) {
      if (error instanceof z.ZodError) {
        res.status(400).json({
          error: 'Validation error',
          details: error.errors.map(e => ({
            field: e.path.join('.'),
            message: e.message,
          })),
        });
      } else {
        next(error);
      }
    }
  };
};
```

### 4.3 Content Security Policy

```typescript
// Security headers configuration
const securityHeaders = {
  // Content Security Policy
  'Content-Security-Policy': [
    "default-src 'self'",
    "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net",
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
    "font-src 'self' https://fonts.gstatic.com",
    "img-src 'self' data: https:",
    "connect-src 'self' https://api.mindweave.ai wss://api.mindweave.ai",
    "frame-ancestors 'none'",
    "form-action 'self'",
    "base-uri 'self'",
    "upgrade-insecure-requests",
  ].join('; '),

  // Other security headers
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'DENY',
  'X-XSS-Protection': '1; mode=block',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
};
```

---

## 5. Data Protection

### 5.1 Encryption at Rest

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      ENCRYPTION AT REST                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DATABASE ENCRYPTION:                                                      │
│  ────────────────────                                                      │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  PostgreSQL (RDS)                                                    │   │
│  │  • Storage: AES-256 via AWS KMS                                     │   │
│  │  • Key: Customer-managed CMK (aws/rds)                              │   │
│  │  • Automated key rotation: 1 year                                   │   │
│  │                                                                      │   │
│  │  Sensitive columns (PII) - Application-level encryption:            │   │
│  │  • email → encrypted with tenant-specific key                       │   │
│  │  • phone → encrypted with tenant-specific key                       │   │
│  │  • payment_info → encrypted with compliance key                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  OBJECT STORAGE:                                                           │
│  ───────────────                                                           │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  S3 Buckets                                                          │   │
│  │  • Default: SSE-S3 (AES-256)                                        │   │
│  │  • Sensitive: SSE-KMS with CMK                                      │   │
│  │  • Compliance: SSE-KMS with compliance CMK                          │   │
│  │  • Bucket policies enforce encryption                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  CACHE ENCRYPTION:                                                         │
│  ─────────────────                                                         │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Redis (ElastiCache)                                                 │   │
│  │  • At-rest encryption enabled                                       │   │
│  │  • AUTH token required                                              │   │
│  │  • TLS in-transit                                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Key Management

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      KEY MANAGEMENT (AWS KMS)                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  KEY HIERARCHY:                                                            │
│  ──────────────                                                            │
│                                                                             │
│                    ┌─────────────────┐                                     │
│                    │   Master Key    │                                     │
│                    │   (HSM-backed)  │                                     │
│                    └────────┬────────┘                                     │
│                             │                                               │
│         ┌───────────────────┼───────────────────┐                          │
│         │                   │                   │                          │
│  ┌──────▼──────┐    ┌───────▼───────┐   ┌──────▼──────┐                   │
│  │ Database    │    │ Application   │   │ Compliance  │                   │
│  │ Encryption  │    │ Encryption    │   │ Encryption  │                   │
│  │ Key         │    │ Key           │   │ Key         │                   │
│  └──────┬──────┘    └───────┬───────┘   └──────┬──────┘                   │
│         │                   │                   │                          │
│   RDS, S3              API keys,          Audit logs,                      │
│   backups              tokens             compliance data                  │
│                                                                             │
│  KEY POLICIES:                                                             │
│  ─────────────                                                             │
│                                                                             │
│  • Automatic rotation: 365 days                                           │
│  • Multi-region replication for DR                                        │
│  • Key deletion: 30-day waiting period                                    │
│  • Access via IAM roles only                                              │
│  • All key operations logged to CloudTrail                                │
│                                                                             │
│  KEY USAGE AUDIT:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  {                                                                         │
│    "eventTime": "2024-01-15T10:30:00Z",                                   │
│    "eventSource": "kms.amazonaws.com",                                    │
│    "eventName": "Decrypt",                                                │
│    "userIdentity": {...},                                                 │
│    "resources": ["arn:aws:kms:...:key/xxx"],                             │
│    "requestParameters": {"keyId": "...", "encryptionContext": {...}}     │
│  }                                                                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 5.3 Secrets Management

```yaml
# AWS Secrets Manager configuration
secrets:
  database:
    name: mindweave/prod/database
    rotation:
      enabled: true
      schedule: "rate(30 days)"
      lambda: rotate-rds-password

  api_keys:
    name: mindweave/prod/api-keys
    rotation:
      enabled: false  # Manual rotation via API

  external_services:
    stripe:
      name: mindweave/prod/stripe
      fields:
        - secret_key
        - webhook_secret
    sendgrid:
      name: mindweave/prod/sendgrid
      fields:
        - api_key
    anthropic:
      name: mindweave/prod/anthropic
      fields:
        - api_key

# Application access pattern
# Environment variables at runtime (via IAM role)
# Never stored in code or configuration files
```

---

## 6. Compliance Controls

### 6.1 SOC 2 Controls

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      SOC 2 TRUST PRINCIPLES                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SECURITY (CC)                                                             │
│  ─────────────                                                             │
│  CC1.1  Control Environment                    ✓ Implemented              │
│  CC2.1  Information and Communication          ✓ Implemented              │
│  CC3.1  Risk Assessment                        ✓ Implemented              │
│  CC4.1  Monitoring Activities                  ✓ Implemented              │
│  CC5.1  Control Activities                     ✓ Implemented              │
│  CC6.1  Logical and Physical Access            ✓ Implemented              │
│  CC7.1  System Operations                      ✓ Implemented              │
│  CC8.1  Change Management                      ✓ Implemented              │
│  CC9.1  Risk Mitigation                        ✓ Implemented              │
│                                                                             │
│  AVAILABILITY (A)                                                          │
│  ─────────────────                                                         │
│  A1.1   Capacity Management                    ✓ Implemented              │
│  A1.2   Environmental Safeguards               ✓ Implemented (AWS)        │
│  A1.3   Data Backup                            ✓ Implemented              │
│                                                                             │
│  CONFIDENTIALITY (C)                                                       │
│  ────────────────────                                                      │
│  C1.1   Confidential Information Identification ✓ Implemented             │
│  C1.2   Confidential Information Disposal       ✓ Implemented             │
│                                                                             │
│  PROCESSING INTEGRITY (PI)                                                 │
│  ─────────────────────────                                                 │
│  PI1.1  Processing Integrity Policies          ✓ Implemented              │
│  PI1.2  Processing Accuracy                    ✓ Implemented              │
│  PI1.3  Processing Completeness                ✓ Implemented              │
│                                                                             │
│  PRIVACY (P)                                                               │
│  ───────────                                                               │
│  P1-P8  Privacy Principles                     ✓ GDPR/CCPA compliant     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 GDPR Compliance

| Requirement | Implementation |
|-------------|----------------|
| **Lawful Basis** | Consent management, legitimate interest |
| **Data Minimization** | Collect only necessary data |
| **Purpose Limitation** | Data used only for stated purposes |
| **Accuracy** | User data correction mechanisms |
| **Storage Limitation** | Data retention policies enforced |
| **Integrity & Confidentiality** | Encryption, access controls |
| **Accountability** | DPO appointed, documentation |
| **Data Subject Rights** | Self-service portal for DSAR |
| **Breach Notification** | 72-hour notification procedure |
| **Data Protection Impact** | DPIA for high-risk processing |

### 6.3 Audit Logging

```sql
-- Audit log schema
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Actor
    actor_type VARCHAR(20) NOT NULL,  -- 'user', 'api_key', 'system'
    actor_id UUID,
    actor_email VARCHAR(255),
    actor_ip INET,
    actor_user_agent TEXT,

    -- Context
    org_id UUID,
    project_id UUID,
    request_id UUID,
    session_id UUID,

    -- Action
    action VARCHAR(100) NOT NULL,      -- 'user.login', 'project.create', etc.
    resource_type VARCHAR(50),
    resource_id UUID,

    -- Details
    old_values JSONB,
    new_values JSONB,
    metadata JSONB,

    -- Classification
    sensitivity VARCHAR(20) DEFAULT 'normal',  -- 'normal', 'sensitive', 'critical'
    compliance_relevant BOOLEAN DEFAULT FALSE,

    -- Integrity
    checksum VARCHAR(64),              -- SHA-256 of log entry
    previous_checksum VARCHAR(64)      -- Chain for tamper detection
);

-- Hypertable for efficient time-series queries
SELECT create_hypertable('audit_logs', 'timestamp');

-- Retention policy (7 years for compliance)
SELECT add_retention_policy('audit_logs', INTERVAL '7 years');

-- Tamper detection trigger
CREATE OR REPLACE FUNCTION calculate_audit_checksum()
RETURNS TRIGGER AS $$
BEGIN
    NEW.checksum = encode(sha256(
        (NEW.timestamp::text ||
         NEW.actor_id::text ||
         NEW.action ||
         COALESCE(NEW.old_values::text, '') ||
         COALESCE(NEW.new_values::text, '') ||
         COALESCE(NEW.previous_checksum, ''))::bytea
    ), 'hex');

    SELECT checksum INTO NEW.previous_checksum
    FROM audit_logs
    ORDER BY timestamp DESC
    LIMIT 1;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER audit_log_checksum
BEFORE INSERT ON audit_logs
FOR EACH ROW EXECUTE FUNCTION calculate_audit_checksum();
```

---

## 7. Vulnerability Management

### 7.1 Security Scanning Pipeline

```
┌────────────────────────────────────────────────────────────────────────────┐
│                   SECURITY SCANNING PIPELINE                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CODE COMMIT                                                               │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────┐                                                       │
│  │  SAST           │  Static Application Security Testing                  │
│  │  (Semgrep)      │  • Custom rules for MindWeave patterns               │
│  │                 │  • OWASP rules                                        │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │  SCA            │  Software Composition Analysis                        │
│  │  (Snyk)         │  • Dependency vulnerabilities                        │
│  │                 │  • License compliance                                 │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │  Secrets Scan   │  Prevent credential leaks                             │
│  │  (TruffleHog)   │  • API keys, passwords                               │
│  │                 │  • Private keys                                       │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  BUILD                                                                     │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────┐                                                       │
│  │  Container Scan │  Container image security                             │
│  │  (Trivy)        │  • OS vulnerabilities                                │
│  │                 │  • Application vulnerabilities                        │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  DEPLOY TO STAGING                                                         │
│      │                                                                      │
│      ▼                                                                      │
│  ┌─────────────────┐                                                       │
│  │  DAST           │  Dynamic Application Security Testing                 │
│  │  (OWASP ZAP)    │  • Runtime vulnerability scanning                    │
│  │                 │  • API security testing                               │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  DEPLOY TO PRODUCTION (if all checks pass)                                │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  ONGOING:                                                                  │
│  • Weekly infrastructure scans (AWS Inspector)                            │
│  • Monthly penetration testing                                            │
│  • Quarterly third-party security audit                                   │
│  • Continuous bug bounty program                                          │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 7.2 Vulnerability Classification

| Severity | Response Time | Example |
|----------|--------------|---------|
| **Critical** | 24 hours | RCE, Authentication bypass |
| **High** | 7 days | SQL injection, Privilege escalation |
| **Medium** | 30 days | XSS, Information disclosure |
| **Low** | 90 days | Missing headers, Minor config issues |

---

## 8. Incident Response

### 8.1 Incident Response Plan

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      INCIDENT RESPONSE PLAN                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PHASE 1: DETECTION & IDENTIFICATION                                       │
│  ────────────────────────────────────                                      │
│  • Automated alerting (PagerDuty)                                         │
│  • Security team triage                                                   │
│  • Severity classification                                                │
│  • Initial scope assessment                                               │
│                                                                             │
│  PHASE 2: CONTAINMENT                                                      │
│  ─────────────────────                                                     │
│  • Isolate affected systems                                               │
│  • Preserve evidence                                                      │
│  • Block malicious actors                                                 │
│  • Temporary mitigations                                                  │
│                                                                             │
│  PHASE 3: ERADICATION                                                      │
│  ─────────────────────                                                     │
│  • Root cause analysis                                                    │
│  • Remove malicious artifacts                                             │
│  • Patch vulnerabilities                                                  │
│  • Verify complete removal                                                │
│                                                                             │
│  PHASE 4: RECOVERY                                                         │
│  ─────────────────                                                         │
│  • Restore systems                                                        │
│  • Validate integrity                                                     │
│  • Monitor for recurrence                                                 │
│  • Gradual service restoration                                            │
│                                                                             │
│  PHASE 5: LESSONS LEARNED                                                  │
│  ─────────────────────────                                                 │
│  • Post-incident review                                                   │
│  • Documentation                                                          │
│  • Process improvements                                                   │
│  • Communication to stakeholders                                          │
│                                                                             │
│  COMMUNICATION:                                                            │
│  ──────────────                                                            │
│  • Internal: Slack #security-incidents                                    │
│  • Customers: status.mindweave.ai                                        │
│  • Regulators: Within 72 hours (if breach)                               │
│                                                                             │
│  CONTACTS:                                                                 │
│  ─────────                                                                 │
│  • Security Lead: security@mindweave.ai                                  │
│  • On-call: PagerDuty rotation                                           │
│  • Legal: legal@mindweave.ai                                             │
│  • PR: communications@mindweave.ai                                       │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [AUTHENTICATION-AUTHORIZATION.md](./AUTHENTICATION-AUTHORIZATION.md) | Auth design |
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System design |
| [DEPLOYMENT-STRATEGY.md](./DEPLOYMENT-STRATEGY.md) | Deployment |
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Monitoring |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial security architecture |
