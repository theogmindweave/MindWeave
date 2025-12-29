# MindWeave Authentication & Authorization Architecture

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-007 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's authentication and authorization system, including identity management, session handling, API key management, SSO integration, and role-based access control (RBAC). Security is a foundational requirement for enterprise AI governance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  AUTHENTICATION & AUTHORIZATION ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     AUTHENTICATION METHODS                           │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │ Email/Pass │  │   OAuth    │  │    SSO     │  │  API Keys  │    │   │
│  │  │            │  │            │  │            │  │            │    │   │
│  │  │ • Login    │  │ • Google   │  │ • SAML 2.0 │  │ • Project  │    │   │
│  │  │ • Register │  │ • GitHub   │  │ • OIDC     │  │ • Scoped   │    │   │
│  │  │ • Reset    │  │ • Microsoft│  │ • Custom   │  │ • Rotating │    │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                        │                                    │
│                                        ▼                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        TOKEN MANAGEMENT                              │   │
│  │                                                                      │   │
│  │  ┌─────────────────────┐        ┌─────────────────────────────────┐│   │
│  │  │    Access Token     │        │       Refresh Token             ││   │
│  │  │                     │        │                                 ││   │
│  │  │  • JWT (15 min)     │        │  • Opaque (7 days)              ││   │
│  │  │  • Stateless        │        │  • Stored in Redis             ││   │
│  │  │  • Contains claims  │        │  • Single use rotation         ││   │
│  │  └─────────────────────┘        └─────────────────────────────────┘│   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                        │                                    │
│                                        ▼                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        AUTHORIZATION                                 │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │    RBAC    │  │    ABAC    │  │  Resource  │  │   Policy   │    │   │
│  │  │            │  │            │  │   Based    │  │   Engine   │    │   │
│  │  │ • Roles    │  │ • Attrs    │  │            │  │            │    │   │
│  │  │ • Perms    │  │ • Context  │  │ • Ownership│  │ • OPA      │    │   │
│  │  │ • Inherit  │  │ • Dynamic  │  │ • Sharing  │  │ • Custom   │    │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Authentication Methods

### 1.1 Email/Password Authentication

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    EMAIL/PASSWORD AUTHENTICATION                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  REGISTRATION FLOW:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  ┌────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Client │───►│   API   │───►│  Create  │───►│  Send    │              │
│  │        │    │         │    │   User   │    │  Email   │              │
│  └────────┘    └─────────┘    └──────────┘    └──────────┘              │
│       │                            │                │                      │
│       │                            ▼                │                      │
│       │                     Hash password           │                      │
│       │                     (Argon2id)              │                      │
│       │                            │                │                      │
│       │                            ▼                │                      │
│       │                     Store user              ▼                      │
│       │                     (unverified)     Verification                  │
│       │                                      email sent                    │
│       │                                            │                       │
│       │                                            ▼                       │
│       │◄──────────────────────────────────────────────                    │
│       │         Return { user, requiresVerification }                     │
│                                                                             │
│  PASSWORD REQUIREMENTS:                                                    │
│  ──────────────────────                                                    │
│  • Minimum 10 characters                                                  │
│  • At least 1 uppercase, 1 lowercase, 1 number                           │
│  • Not in common password list (10K entries)                              │
│  • Not similar to email or name                                           │
│  • Entropy score >= 40 bits (zxcvbn)                                      │
│                                                                             │
│  HASHING:                                                                  │
│  ─────────                                                                 │
│  Algorithm: Argon2id                                                       │
│  Memory: 64 MB                                                             │
│  Iterations: 3                                                             │
│  Parallelism: 4                                                            │
│  Salt: 16 bytes (random)                                                   │
│  Hash length: 32 bytes                                                     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 OAuth 2.0 / Social Login

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        OAUTH 2.0 FLOW (PKCE)                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CLIENT              MINDWEAVE           OAUTH PROVIDER                    │
│     │                    │                     │                           │
│     │  1. Init OAuth     │                     │                           │
│     │───────────────────►│                     │                           │
│     │                    │                     │                           │
│     │  2. Generate PKCE  │                     │                           │
│     │      code_verifier │                     │                           │
│     │      code_challenge│                     │                           │
│     │                    │                     │                           │
│     │  3. Redirect URL   │                     │                           │
│     │◄───────────────────│                     │                           │
│     │                    │                     │                           │
│     │  4. Redirect to provider ───────────────►│                           │
│     │                    │                     │                           │
│     │  5. User authenticates ◄────────────────►│                           │
│     │                    │                     │                           │
│     │  6. Callback with code ◄─────────────────│                           │
│     │───────────────────►│                     │                           │
│     │                    │                     │                           │
│     │                    │  7. Exchange code   │                           │
│     │                    │     + code_verifier │                           │
│     │                    │────────────────────►│                           │
│     │                    │                     │                           │
│     │                    │  8. Access token    │                           │
│     │                    │◄────────────────────│                           │
│     │                    │                     │                           │
│     │                    │  9. Fetch user info │                           │
│     │                    │────────────────────►│                           │
│     │                    │◄────────────────────│                           │
│     │                    │                     │                           │
│     │  10. Create/link   │                     │                           │
│     │      user account  │                     │                           │
│     │                    │                     │                           │
│     │  11. Return tokens │                     │                           │
│     │◄───────────────────│                     │                           │
│                                                                             │
│  SUPPORTED PROVIDERS:                                                      │
│  ────────────────────                                                      │
│  • Google (OpenID Connect)                                                 │
│  • GitHub (OAuth 2.0)                                                      │
│  • Microsoft/Azure AD (OpenID Connect)                                     │
│  • GitLab (OAuth 2.0)                                                      │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Enterprise SSO (SAML 2.0)

```
┌────────────────────────────────────────────────────────────────────────────┐
│                          SAML 2.0 SSO FLOW                                  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SP-INITIATED SSO (Most Common):                                           │
│  ─────────────────────────────────                                         │
│                                                                             │
│  USER           SERVICE PROVIDER       IDENTITY PROVIDER                   │
│   │              (MindWeave)            (Okta/Azure AD)                    │
│   │                   │                       │                            │
│   │  1. Access app    │                       │                            │
│   │──────────────────►│                       │                            │
│   │                   │                       │                            │
│   │                   │  2. Generate SAML     │                            │
│   │                   │     AuthnRequest      │                            │
│   │                   │                       │                            │
│   │  3. Redirect to IdP with AuthnRequest    │                            │
│   │◄──────────────────│                       │                            │
│   │───────────────────────────────────────────►                            │
│   │                   │                       │                            │
│   │                   │     4. User           │                            │
│   │◄──────────────────────────────────────────►                            │
│   │                   │     authenticates     │                            │
│   │                   │                       │                            │
│   │  5. POST SAMLResponse to ACS endpoint    │                            │
│   │◄──────────────────────────────────────────│                            │
│   │──────────────────►│                       │                            │
│   │                   │                       │                            │
│   │                   │  6. Validate:         │                            │
│   │                   │  • Signature          │                            │
│   │                   │  • Conditions         │                            │
│   │                   │  • NotBefore/After    │                            │
│   │                   │  • Audience           │                            │
│   │                   │                       │                            │
│   │                   │  7. Extract claims    │                            │
│   │                   │  • email              │                            │
│   │                   │  • name               │                            │
│   │                   │  • groups             │                            │
│   │                   │                       │                            │
│   │                   │  8. Create session    │                            │
│   │                   │  (JIT provisioning)   │                            │
│   │                   │                       │                            │
│   │  9. Redirect to   │                       │                            │
│   │     app + tokens  │                       │                            │
│   │◄──────────────────│                       │                            │
│                                                                             │
│  SSO CONFIGURATION:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  MindWeave (SP) Metadata:                                                  │
│  • Entity ID: https://api.mindweave.ai/saml/metadata                      │
│  • ACS URL: https://api.mindweave.ai/saml/acs                             │
│  • SLO URL: https://api.mindweave.ai/saml/slo                             │
│  • Certificate: RSA 2048-bit for signing                                  │
│                                                                             │
│  Required IdP Attributes:                                                  │
│  • email (required)                                                        │
│  • firstName (optional)                                                    │
│  • lastName (optional)                                                     │
│  • groups (optional, for role mapping)                                    │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 1.4 API Key Authentication

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        API KEY AUTHENTICATION                               │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  KEY FORMAT:                                                               │
│  ───────────                                                               │
│                                                                             │
│  mw_sk_live_a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                      │
│  │  │  │    │                                                              │
│  │  │  │    └── Random bytes (base58, 40 chars)                           │
│  │  │  └── Environment (live/test)                                        │
│  │  └── Key type (sk=secret, pk=public)                                   │
│  └── Prefix (mindweave)                                                   │
│                                                                             │
│  KEY TYPES:                                                                │
│  ──────────                                                                │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐    │
│  │  Secret Key     │  │  Public Key     │  │  Restricted Key         │    │
│  │  (mw_sk_*)      │  │  (mw_pk_*)      │  │  (mw_rk_*)              │    │
│  │                 │  │                 │  │                         │    │
│  │  • Full access  │  │  • Read-only    │  │  • Custom scopes        │    │
│  │  • Server-side  │  │  • Client-safe  │  │  • IP allowlist         │    │
│  │  • All scopes   │  │  • Limited ops  │  │  • Expiration           │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────┘    │
│                                                                             │
│  STORAGE:                                                                  │
│  ────────                                                                  │
│                                                                             │
│  • Only store SHA-256 hash of key                                         │
│  • Store prefix for lookup (first 12 chars)                               │
│  • Never log full key                                                      │
│  • Key visible only once at creation                                       │
│                                                                             │
│  VALIDATION FLOW:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  1. Extract key from Authorization header                                  │
│  2. Parse prefix and environment                                           │
│  3. Lookup by prefix hash                                                  │
│  4. Verify full key hash matches                                           │
│  5. Check expiration                                                       │
│  6. Check IP allowlist (if configured)                                     │
│  7. Load project/org context                                               │
│  8. Check scopes against requested operation                               │
│                                                                             │
│  SCOPES:                                                                   │
│  ───────                                                                   │
│                                                                             │
│  • read:usage        - Read usage data                                    │
│  • write:usage       - Submit usage events                                │
│  • read:projects     - Read project config                                │
│  • write:projects    - Modify project config                              │
│  • read:mcp          - Read MCP registry                                  │
│  • write:mcp         - Modify MCP registry                                │
│  • read:policies     - Read policies                                      │
│  • write:policies    - Modify policies                                    │
│  • admin             - Full administrative access                         │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Token Management

### 2.1 JWT Access Token

```typescript
// JWT Access Token Structure
interface JWTPayload {
  // Standard claims
  iss: string;        // "https://api.mindweave.ai"
  sub: string;        // User ID
  aud: string[];      // ["https://api.mindweave.ai"]
  exp: number;        // Expiration (15 minutes)
  iat: number;        // Issued at
  jti: string;        // Unique token ID

  // Custom claims
  email: string;
  orgId: string;
  orgSlug: string;
  role: string;
  permissions: string[];
  sessionId: string;
}

// Token configuration
const tokenConfig = {
  algorithm: 'RS256',  // RSA signature
  accessTokenExpiry: '15m',
  refreshTokenExpiry: '7d',
  issuer: 'https://api.mindweave.ai',
  audience: ['https://api.mindweave.ai'],
};
```

### 2.2 Refresh Token Strategy

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      REFRESH TOKEN ROTATION                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ROTATION FLOW:                                                            │
│  ──────────────                                                            │
│                                                                             │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │    Client                    Server                                 │    │
│  │       │                         │                                   │    │
│  │       │  1. POST /auth/refresh  │                                   │    │
│  │       │  { refreshToken: RT1 }  │                                   │    │
│  │       │─────────────────────────►                                   │    │
│  │       │                         │                                   │    │
│  │       │                         │  2. Validate RT1:                 │    │
│  │       │                         │  • Exists in Redis                │    │
│  │       │                         │  • Not expired                    │    │
│  │       │                         │  • Not revoked                    │    │
│  │       │                         │                                   │    │
│  │       │                         │  3. Generate new tokens:          │    │
│  │       │                         │  • New access token (AT2)         │    │
│  │       │                         │  • New refresh token (RT2)        │    │
│  │       │                         │                                   │    │
│  │       │                         │  4. Invalidate RT1                │    │
│  │       │                         │  (single-use rotation)            │    │
│  │       │                         │                                   │    │
│  │       │  5. { accessToken: AT2, │                                   │    │
│  │       │       refreshToken: RT2 }                                   │    │
│  │       │◄─────────────────────────                                   │    │
│  │       │                         │                                   │    │
│  │                                                                     │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
│  REDIS STORAGE:                                                            │
│  ──────────────                                                            │
│                                                                             │
│  Key: refresh_token:{token_hash}                                           │
│  Value: {                                                                  │
│    userId: "user_123",                                                     │
│    sessionId: "sess_456",                                                  │
│    createdAt: "2024-01-15T10:00:00Z",                                     │
│    expiresAt: "2024-01-22T10:00:00Z",                                     │
│    family: "fam_789",  // Token family for rotation detection             │
│    generation: 3       // Rotation count                                   │
│  }                                                                         │
│  TTL: 7 days                                                               │
│                                                                             │
│  REUSE DETECTION:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  If a refresh token is used twice:                                         │
│  1. Detect via missing token or wrong generation                          │
│  2. Invalidate entire token family                                        │
│  3. Force user re-authentication                                          │
│  4. Alert security team (potential token theft)                           │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Multi-Factor Authentication

### 3.1 MFA Methods

```
┌────────────────────────────────────────────────────────────────────────────┐
│                     MULTI-FACTOR AUTHENTICATION                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SUPPORTED METHODS:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────┐    │
│  │     TOTP        │  │    WebAuthn     │  │    Backup Codes         │    │
│  │                 │  │                 │  │                         │    │
│  │  • Google Auth  │  │  • YubiKey      │  │  • 10 single-use        │    │
│  │  • Authy        │  │  • Touch ID     │  │  • Recovery option      │    │
│  │  • 1Password    │  │  • Windows Hello│  │  • Regeneratable        │    │
│  │                 │  │                 │  │                         │    │
│  │  RFC 6238       │  │  FIDO2/W3C      │  │  Cryptographic random   │    │
│  └─────────────────┘  └─────────────────┘  └─────────────────────────┘    │
│                                                                             │
│  TOTP SETUP FLOW:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  1. Generate 160-bit secret (base32 encoded)                              │
│  2. Create provisioning URI:                                               │
│     otpauth://totp/MindWeave:{email}?secret={secret}&issuer=MindWeave     │
│  3. Display QR code to user                                                │
│  4. User scans with authenticator app                                      │
│  5. User enters verification code                                          │
│  6. Server validates code                                                  │
│  7. Store encrypted secret                                                 │
│  8. Generate and display backup codes                                      │
│                                                                             │
│  TOTP CONFIGURATION:                                                       │
│  ───────────────────                                                       │
│  • Algorithm: SHA-1                                                        │
│  • Digits: 6                                                               │
│  • Period: 30 seconds                                                      │
│  • Window: ±1 period (clock drift tolerance)                              │
│                                                                             │
│  MFA ENFORCEMENT:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  Level           Requirement                When Enforced           │  │
│  ├─────────────────────────────────────────────────────────────────────┤  │
│  │  Optional        User choice               Personal preference      │  │
│  │  Recommended     Prompted to enable        After signup             │  │
│  │  Required        Must enable               Org policy               │  │
│  │  Required+       Specific methods          Enterprise tier          │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 MFA Implementation

```typescript
// src/application/services/mfa.service.ts
import { authenticator } from 'otplib';
import crypto from 'crypto';

export class MFAService {
  private readonly issuer = 'MindWeave';

  generateSecret(): { secret: string; uri: string; qrCode: string } {
    const secret = authenticator.generateSecret(20); // 160 bits

    const uri = authenticator.keyuri(
      '', // Will be set with email
      this.issuer,
      secret
    );

    return { secret, uri, qrCode: '' }; // QR code generated client-side
  }

  generateURI(email: string, secret: string): string {
    return authenticator.keyuri(email, this.issuer, secret);
  }

  verify(secret: string, token: string): boolean {
    // Allows ±1 time window for clock drift
    return authenticator.verify({
      token,
      secret,
      window: 1,
    });
  }

  generateBackupCodes(count: number = 10): string[] {
    const codes: string[] = [];
    for (let i = 0; i < count; i++) {
      // Generate 8-character alphanumeric codes
      const code = crypto
        .randomBytes(4)
        .toString('hex')
        .toUpperCase();
      codes.push(`${code.slice(0, 4)}-${code.slice(4)}`);
    }
    return codes;
  }

  hashBackupCode(code: string): string {
    // Normalize and hash
    const normalized = code.replace(/-/g, '').toUpperCase();
    return crypto
      .createHash('sha256')
      .update(normalized)
      .digest('hex');
  }

  verifyBackupCode(code: string, hashedCodes: string[]): number {
    const hash = this.hashBackupCode(code);
    const index = hashedCodes.indexOf(hash);
    return index; // Returns -1 if not found, index if found
  }
}
```

---

## 4. Role-Based Access Control (RBAC)

### 4.1 Role Hierarchy

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         ROLE HIERARCHY                                      │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    ┌─────────────────────┐                                 │
│                    │       OWNER         │                                 │
│                    │                     │                                 │
│                    │  • Full org control │                                 │
│                    │  • Delete org       │                                 │
│                    │  • Billing mgmt     │                                 │
│                    │  • Transfer owner   │                                 │
│                    └──────────┬──────────┘                                 │
│                               │                                             │
│                               │ inherits                                   │
│                               ▼                                             │
│                    ┌─────────────────────┐                                 │
│                    │       ADMIN         │                                 │
│                    │                     │                                 │
│                    │  • Manage members   │                                 │
│                    │  • Manage projects  │                                 │
│                    │  • Manage policies  │                                 │
│                    │  • View audit logs  │                                 │
│                    └──────────┬──────────┘                                 │
│                               │                                             │
│                               │ inherits                                   │
│                               ▼                                             │
│                    ┌─────────────────────┐                                 │
│                    │       MEMBER        │                                 │
│                    │                     │                                 │
│                    │  • Access projects  │                                 │
│                    │  • View analytics   │                                 │
│                    │  • Create API keys  │                                 │
│                    │  • Manage MCP       │                                 │
│                    └──────────┬──────────┘                                 │
│                               │                                             │
│                               │ inherits                                   │
│                               ▼                                             │
│                    ┌─────────────────────┐                                 │
│                    │       VIEWER        │                                 │
│                    │                     │                                 │
│                    │  • Read-only access │                                 │
│                    │  • View dashboard   │                                 │
│                    │  • View analytics   │                                 │
│                    │  • No modifications │                                 │
│                    └─────────────────────┘                                 │
│                                                                             │
│  PROJECT-LEVEL ROLES (Within assigned projects):                          │
│  ──────────────────────────────────────────────                           │
│                                                                             │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐              │
│  │  Project Lead  │  │   Developer    │  │    Analyst     │              │
│  │                │  │                │  │                │              │
│  │ • Full control │  │ • Write access │  │ • Read analytics│             │
│  │ • Manage team  │  │ • MCP config   │  │ • Export data  │              │
│  │ • Delete proj  │  │ • API keys     │  │ • No changes   │              │
│  └────────────────┘  └────────────────┘  └────────────────┘              │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Permission Matrix

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        PERMISSION MATRIX                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PERMISSION                 OWNER  ADMIN  MEMBER  VIEWER  LEAD  DEV  ANLST│
│  ───────────────────────────────────────────────────────────────────────  │
│                                                                             │
│  ORGANIZATION                                                              │
│  org:read                     ✓      ✓      ✓       ✓      ─     ─     ─  │
│  org:update                   ✓      ✓      ─       ─      ─     ─     ─  │
│  org:delete                   ✓      ─      ─       ─      ─     ─     ─  │
│  org:billing                  ✓      ─      ─       ─      ─     ─     ─  │
│  org:members:read             ✓      ✓      ✓       ✓      ─     ─     ─  │
│  org:members:invite           ✓      ✓      ─       ─      ─     ─     ─  │
│  org:members:remove           ✓      ✓      ─       ─      ─     ─     ─  │
│  org:members:role             ✓      ✓      ─       ─      ─     ─     ─  │
│                                                                             │
│  PROJECTS                                                                  │
│  project:create               ✓      ✓      ✓       ─      ─     ─     ─  │
│  project:read                 ✓      ✓      ✓       ✓      ✓     ✓     ✓  │
│  project:update               ✓      ✓      ─       ─      ✓     ─     ─  │
│  project:delete               ✓      ✓      ─       ─      ✓     ─     ─  │
│  project:members              ✓      ✓      ─       ─      ✓     ─     ─  │
│                                                                             │
│  API KEYS                                                                  │
│  apikey:create                ✓      ✓      ✓       ─      ✓     ✓     ─  │
│  apikey:read                  ✓      ✓      ✓       ✓      ✓     ✓     ✓  │
│  apikey:revoke                ✓      ✓      ✓       ─      ✓     ✓     ─  │
│                                                                             │
│  MCP REGISTRY                                                              │
│  mcp:read                     ✓      ✓      ✓       ✓      ✓     ✓     ✓  │
│  mcp:register                 ✓      ✓      ✓       ─      ✓     ✓     ─  │
│  mcp:approve                  ✓      ✓      ─       ─      ✓     ─     ─  │
│  mcp:delete                   ✓      ✓      ─       ─      ✓     ─     ─  │
│                                                                             │
│  POLICIES                                                                  │
│  policy:read                  ✓      ✓      ✓       ✓      ✓     ✓     ✓  │
│  policy:create                ✓      ✓      ─       ─      ✓     ─     ─  │
│  policy:update                ✓      ✓      ─       ─      ✓     ─     ─  │
│  policy:delete                ✓      ✓      ─       ─      ✓     ─     ─  │
│                                                                             │
│  ANALYTICS                                                                 │
│  analytics:read               ✓      ✓      ✓       ✓      ✓     ✓     ✓  │
│  analytics:export             ✓      ✓      ✓       ─      ✓     ✓     ✓  │
│                                                                             │
│  AUDIT                                                                     │
│  audit:read                   ✓      ✓      ─       ─      ✓     ─     ─  │
│  audit:export                 ✓      ✓      ─       ─      ─     ─     ─  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 RBAC Implementation

```typescript
// src/domain/authorization/rbac.ts

// Role definitions
export const ROLES = {
  OWNER: 'owner',
  ADMIN: 'admin',
  MEMBER: 'member',
  VIEWER: 'viewer',
} as const;

export const PROJECT_ROLES = {
  LEAD: 'lead',
  DEVELOPER: 'developer',
  ANALYST: 'analyst',
} as const;

// Permission definitions
export const PERMISSIONS = {
  // Organization
  ORG_READ: 'org:read',
  ORG_UPDATE: 'org:update',
  ORG_DELETE: 'org:delete',
  ORG_BILLING: 'org:billing',
  ORG_MEMBERS_READ: 'org:members:read',
  ORG_MEMBERS_INVITE: 'org:members:invite',
  ORG_MEMBERS_REMOVE: 'org:members:remove',
  ORG_MEMBERS_ROLE: 'org:members:role',

  // Projects
  PROJECT_CREATE: 'project:create',
  PROJECT_READ: 'project:read',
  PROJECT_UPDATE: 'project:update',
  PROJECT_DELETE: 'project:delete',
  PROJECT_MEMBERS: 'project:members',

  // API Keys
  APIKEY_CREATE: 'apikey:create',
  APIKEY_READ: 'apikey:read',
  APIKEY_REVOKE: 'apikey:revoke',

  // MCP
  MCP_READ: 'mcp:read',
  MCP_REGISTER: 'mcp:register',
  MCP_APPROVE: 'mcp:approve',
  MCP_DELETE: 'mcp:delete',

  // Policies
  POLICY_READ: 'policy:read',
  POLICY_CREATE: 'policy:create',
  POLICY_UPDATE: 'policy:update',
  POLICY_DELETE: 'policy:delete',

  // Analytics
  ANALYTICS_READ: 'analytics:read',
  ANALYTICS_EXPORT: 'analytics:export',

  // Audit
  AUDIT_READ: 'audit:read',
  AUDIT_EXPORT: 'audit:export',
} as const;

// Role-Permission mapping
export const ROLE_PERMISSIONS: Record<string, string[]> = {
  [ROLES.OWNER]: Object.values(PERMISSIONS),

  [ROLES.ADMIN]: [
    PERMISSIONS.ORG_READ,
    PERMISSIONS.ORG_UPDATE,
    PERMISSIONS.ORG_MEMBERS_READ,
    PERMISSIONS.ORG_MEMBERS_INVITE,
    PERMISSIONS.ORG_MEMBERS_REMOVE,
    PERMISSIONS.ORG_MEMBERS_ROLE,
    PERMISSIONS.PROJECT_CREATE,
    PERMISSIONS.PROJECT_READ,
    PERMISSIONS.PROJECT_UPDATE,
    PERMISSIONS.PROJECT_DELETE,
    PERMISSIONS.PROJECT_MEMBERS,
    PERMISSIONS.APIKEY_CREATE,
    PERMISSIONS.APIKEY_READ,
    PERMISSIONS.APIKEY_REVOKE,
    PERMISSIONS.MCP_READ,
    PERMISSIONS.MCP_REGISTER,
    PERMISSIONS.MCP_APPROVE,
    PERMISSIONS.MCP_DELETE,
    PERMISSIONS.POLICY_READ,
    PERMISSIONS.POLICY_CREATE,
    PERMISSIONS.POLICY_UPDATE,
    PERMISSIONS.POLICY_DELETE,
    PERMISSIONS.ANALYTICS_READ,
    PERMISSIONS.ANALYTICS_EXPORT,
    PERMISSIONS.AUDIT_READ,
    PERMISSIONS.AUDIT_EXPORT,
  ],

  [ROLES.MEMBER]: [
    PERMISSIONS.ORG_READ,
    PERMISSIONS.ORG_MEMBERS_READ,
    PERMISSIONS.PROJECT_CREATE,
    PERMISSIONS.PROJECT_READ,
    PERMISSIONS.APIKEY_CREATE,
    PERMISSIONS.APIKEY_READ,
    PERMISSIONS.APIKEY_REVOKE,
    PERMISSIONS.MCP_READ,
    PERMISSIONS.MCP_REGISTER,
    PERMISSIONS.POLICY_READ,
    PERMISSIONS.ANALYTICS_READ,
    PERMISSIONS.ANALYTICS_EXPORT,
  ],

  [ROLES.VIEWER]: [
    PERMISSIONS.ORG_READ,
    PERMISSIONS.ORG_MEMBERS_READ,
    PERMISSIONS.PROJECT_READ,
    PERMISSIONS.APIKEY_READ,
    PERMISSIONS.MCP_READ,
    PERMISSIONS.POLICY_READ,
    PERMISSIONS.ANALYTICS_READ,
  ],
};

// Authorization service
export class AuthorizationService {
  hasPermission(userRole: string, permission: string): boolean {
    const permissions = ROLE_PERMISSIONS[userRole] || [];
    return permissions.includes(permission);
  }

  hasAnyPermission(userRole: string, permissions: string[]): boolean {
    return permissions.some((p) => this.hasPermission(userRole, p));
  }

  hasAllPermissions(userRole: string, permissions: string[]): boolean {
    return permissions.every((p) => this.hasPermission(userRole, p));
  }

  getRolePermissions(role: string): string[] {
    return ROLE_PERMISSIONS[role] || [];
  }

  // Resource-based authorization
  async canAccessProject(
    userId: string,
    projectId: string,
    permission: string
  ): Promise<boolean> {
    // Check org-level role first
    const orgMember = await this.getOrgMembership(userId, projectId);
    if (orgMember && this.hasPermission(orgMember.role, permission)) {
      return true;
    }

    // Check project-level role
    const projectMember = await this.getProjectMembership(userId, projectId);
    if (projectMember) {
      const projectPermissions = PROJECT_ROLE_PERMISSIONS[projectMember.role];
      return projectPermissions?.includes(permission) ?? false;
    }

    return false;
  }
}
```

---

## 5. Session Management

### 5.1 Session Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        SESSION MANAGEMENT                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SESSION STORAGE:                                                          │
│  ────────────────                                                          │
│                                                                             │
│  Redis Key: session:{session_id}                                           │
│  Value: {                                                                  │
│    userId: "user_123",                                                     │
│    orgId: "org_456",                                                       │
│    createdAt: "2024-01-15T10:00:00Z",                                     │
│    lastActiveAt: "2024-01-15T14:30:00Z",                                  │
│    expiresAt: "2024-01-22T10:00:00Z",                                     │
│    deviceInfo: {                                                           │
│      userAgent: "Mozilla/5.0...",                                         │
│      ip: "192.168.1.1",                                                   │
│      location: "San Francisco, CA"                                        │
│    },                                                                      │
│    mfaVerified: true,                                                      │
│    impersonatedBy: null  // For admin impersonation                       │
│  }                                                                         │
│  TTL: 7 days (sliding)                                                     │
│                                                                             │
│  SESSION LIFECYCLE:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐            │
│  │ Created  │───►│  Active  │───►│ Inactive │───►│ Expired  │            │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘            │
│       │               │               │               │                    │
│       │               │               │               │                    │
│   On login        On activity    30 min idle      TTL reached             │
│                   (extend TTL)   (warning)        (auto-logout)           │
│                                                                             │
│  CONCURRENT SESSION LIMITS:                                                │
│  ──────────────────────────                                                │
│                                                                             │
│  • Free tier: 2 sessions                                                  │
│  • Team tier: 5 sessions                                                  │
│  • Pro tier: 10 sessions                                                  │
│  • Enterprise: Configurable                                               │
│                                                                             │
│  DEVICE MANAGEMENT:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  Users can:                                                                │
│  • View all active sessions                                               │
│  • See device info and last activity                                      │
│  • Revoke individual sessions                                             │
│  • "Log out everywhere" option                                            │
│                                                                             │
│  SECURITY FEATURES:                                                        │
│  ──────────────────                                                        │
│                                                                             │
│  • IP change detection (prompt re-auth)                                   │
│  • Device fingerprint tracking                                            │
│  • Suspicious activity detection                                          │
│  • Session fixation prevention                                            │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. Security Measures

### 6.1 Security Controls

| Control | Implementation | Purpose |
|---------|----------------|---------|
| Rate limiting | Token bucket per IP/user | Brute force prevention |
| Account lockout | 5 failed attempts → 15 min lock | Brute force prevention |
| Password history | Last 5 passwords blocked | Reuse prevention |
| Session binding | IP + User-Agent hash | Session hijacking prevention |
| CSRF protection | Double-submit cookie | CSRF prevention |
| XSS protection | CSP headers, sanitization | XSS prevention |
| SQL injection | Parameterized queries | Injection prevention |

### 6.2 Audit Logging

```typescript
// Authentication audit events
interface AuthAuditEvent {
  type:
    | 'login.success'
    | 'login.failed'
    | 'login.mfa_required'
    | 'login.mfa_success'
    | 'login.mfa_failed'
    | 'logout'
    | 'password.change'
    | 'password.reset'
    | 'mfa.enabled'
    | 'mfa.disabled'
    | 'session.created'
    | 'session.revoked'
    | 'apikey.created'
    | 'apikey.revoked';

  userId: string;
  timestamp: Date;
  ip: string;
  userAgent: string;
  success: boolean;
  failureReason?: string;
  metadata?: Record<string, unknown>;
}
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security design |
| [API-SPECIFICATIONS.md](./API-SPECIFICATIONS.md) | API security |
| [BACKEND-SERVICES.md](./BACKEND-SERVICES.md) | Service implementation |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial auth architecture |
