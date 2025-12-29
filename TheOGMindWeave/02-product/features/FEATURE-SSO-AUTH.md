# Feature Specification: SSO Authentication

> Complete specification for the Single Sign-On Authentication feature

---

## Overview

### Feature Summary

| Field | Value |
|-------|-------|
| **Feature Name** | SSO Authentication |
| **Priority** | P0 (MVP) |
| **Target Version** | v0.1 (MVP) |
| **Effort Estimate** | 4 weeks |
| **Owner** | Engineering |

### Description

SSO Authentication provides enterprise-grade identity management through integration with major identity providers (Okta, Azure AD, Google Workspace). It enables organizations to manage MindWeave access using their existing identity infrastructure, enforcing their security policies consistently.

### Problem Statement

Enterprise deployments require integration with existing identity systems:
- Users can't use their corporate credentials
- Security teams can't enforce access policies
- No automatic provisioning/deprovisioning
- Compliance requires centralized identity management
- Password fatigue leads to security risks

### Success Metrics

| Metric | Target |
|--------|--------|
| SSO Adoption | 95% of enterprise users via SSO |
| Login Success Rate | 99.9% |
| Provisioning Accuracy | 99.5% |
| Time to First Login | <60 seconds |

---

## User Experience

### Entry Points

1. **Login Page:** "Sign in with SSO" button
2. **Admin Settings:** "Identity & Access" configuration
3. **Invitation Email:** SSO login link
4. **Direct URL:** Deep link with IdP redirect

### Primary Screen: Login

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│                           ┌────────────────────┐                        │
│                           │   ◇ MindWeave      │                        │
│                           │   Enterprise AI    │                        │
│                           │   Governance       │                        │
│                           └────────────────────┘                        │
│                                                                          │
│                    ┌────────────────────────────────────┐               │
│                    │                                    │               │
│                    │   Welcome Back                     │               │
│                    │                                    │               │
│                    │   ┌────────────────────────────┐  │               │
│                    │   │  Work Email               │  │               │
│                    │   │  you@company.com          │  │               │
│                    │   └────────────────────────────┘  │               │
│                    │                                    │               │
│                    │   ┌────────────────────────────┐  │               │
│                    │   │       Continue with SSO    │  │               │
│                    │   └────────────────────────────┘  │               │
│                    │                                    │               │
│                    │   ─────────── or ───────────      │               │
│                    │                                    │               │
│                    │   ┌──────┐ ┌──────┐ ┌──────┐     │               │
│                    │   │Okta │ │Azure │ │Google│     │               │
│                    │   │ ◇   │ │  ◇   │ │  G   │     │               │
│                    │   └──────┘ └──────┘ └──────┘     │               │
│                    │                                    │               │
│                    │   By continuing, you agree to our │               │
│                    │   Terms of Service and Privacy    │               │
│                    │   Policy.                         │               │
│                    │                                    │               │
│                    └────────────────────────────────────┘               │
│                                                                          │
│                    Don't have an account? Contact Admin                 │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### SSO Configuration (Admin)

```
┌─────────────────────────────────────────────────────────────────────────┐
│  ← Settings / Identity & Access                              Save       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Single Sign-On (SSO)                         Status: ✅ Active   │  │
│  │                                                                   │  │
│  │  Your organization uses SSO for authentication.                  │  │
│  │  Last verified: Dec 28, 2025 at 14:32                           │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Identity Provider                                                │  │
│  │                                                                   │  │
│  │  Provider: [Okta ▼]                                              │  │
│  │                                                                   │  │
│  │  ─────────────────────────────────────────────────────────────   │  │
│  │                                                                   │  │
│  │  SAML Configuration                                               │  │
│  │                                                                   │  │
│  │  IdP Entity ID:                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ http://www.okta.com/exk1234abcd                            │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  │  IdP SSO URL:                                                     │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ https://acme.okta.com/app/mindweave/sso/saml               │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  │  X.509 Certificate:                                               │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │ -----BEGIN CERTIFICATE-----                                │  │  │
│  │  │ MIIDpDCCAoygAwIBAgIGAXz...                                 │  │  │
│  │  │ -----END CERTIFICATE-----                   [Upload New]   │  │  │
│  │  └────────────────────────────────────────────────────────────┘  │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  MindWeave Service Provider Details                [Copy All]    │  │
│  │                                                                   │  │
│  │  SP Entity ID:      https://app.mindweave.ai/saml/metadata       │  │
│  │  SP ACS URL:        https://app.mindweave.ai/saml/acs            │  │
│  │  SP SLO URL:        https://app.mindweave.ai/saml/logout         │  │
│  │                                                                   │  │
│  │  [Download SP Metadata XML]                                      │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  User Provisioning (SCIM 2.0)                    Status: Active  │  │
│  │                                                                   │  │
│  │  SCIM Endpoint:   https://api.mindweave.ai/scim/v2               │  │
│  │  Bearer Token:    ••••••••••••••••••          [Regenerate]       │  │
│  │                                                                   │  │
│  │  Sync Status:     Last sync 5 minutes ago                        │  │
│  │  Users Synced:    487 active, 12 deactivated                     │  │
│  │                                                                   │  │
│  │  [Test Connection]  [View Sync Logs]                             │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Attribute Mapping                                                │  │
│  │                                                                   │  │
│  │  MindWeave          IdP Attribute                                 │  │
│  │  ───────────────────────────────────────────────────────────     │  │
│  │  email              user.email                                    │  │
│  │  firstName          user.firstName                                │  │
│  │  lastName           user.lastName                                 │  │
│  │  team               user.department                               │  │
│  │  role               user.role                                     │  │
│  │                                                                   │  │
│  │  [Add Mapping]                                                    │  │
│  │                                                                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### FR-1: SAML 2.0 Authentication

**Requirement:**
Support SAML 2.0 for SSO with major identity providers.

**Details:**
- SP-initiated and IdP-initiated flows
- Support Okta, Azure AD, Google Workspace, OneLogin, Ping
- SAML assertions signed and encrypted
- Single Logout (SLO) support

**Acceptance Criteria:**
- [ ] SP-initiated login works
- [ ] IdP-initiated login works
- [ ] SAML assertions validated
- [ ] Logout terminates session

---

### FR-2: OIDC Support

**Requirement:**
Support OpenID Connect as alternative to SAML.

**Details:**
- Authorization Code flow with PKCE
- Support standard claims
- Token refresh handling
- ID token validation

**Acceptance Criteria:**
- [ ] OIDC login works
- [ ] Tokens validated correctly
- [ ] Refresh tokens work
- [ ] Session management correct

---

### FR-3: Just-in-Time (JIT) Provisioning

**Requirement:**
Create user accounts automatically on first SSO login.

**Details:**
- User created from SAML/OIDC attributes
- Assign to default team (configurable)
- Assign default role (configurable)
- Send welcome notification

**Acceptance Criteria:**
- [ ] New users created on first login
- [ ] Attributes mapped correctly
- [ ] Default team assigned
- [ ] Welcome email sent

---

### FR-4: SCIM 2.0 Provisioning

**Requirement:**
Support automated user provisioning via SCIM 2.0.

**Details:**
- Full SCIM 2.0 compliance
- Create, update, delete users
- Group sync to teams
- Real-time and scheduled sync

**Acceptance Criteria:**
- [ ] SCIM endpoint accessible
- [ ] User CRUD operations work
- [ ] Group sync works
- [ ] Sync logs available

---

### FR-5: Multi-Domain Support

**Requirement:**
Support multiple email domains per organization.

**Details:**
- Configure multiple verified domains
- Domain verification via DNS (TXT record)
- Route to correct IdP by domain
- Prevent domain spoofing

**Acceptance Criteria:**
- [ ] Multiple domains configurable
- [ ] DNS verification works
- [ ] Correct IdP routing
- [ ] Spoofing prevented

---

### FR-6: Session Management

**Requirement:**
Manage user sessions securely.

**Details:**
- Configurable session timeout (default: 8 hours)
- Idle timeout (default: 30 minutes)
- Force re-authentication option
- Session revocation (admin)

**Acceptance Criteria:**
- [ ] Sessions expire correctly
- [ ] Idle timeout works
- [ ] Re-auth can be forced
- [ ] Admin can revoke sessions

---

### FR-7: MFA Enforcement

**Requirement:**
Enforce MFA policies from IdP.

**Details:**
- Honor MFA claims from IdP
- Block access if MFA not satisfied
- Step-up authentication for sensitive actions
- MFA bypass for service accounts (configurable)

**Acceptance Criteria:**
- [ ] MFA claims respected
- [ ] Non-MFA users blocked (if required)
- [ ] Step-up auth works
- [ ] Service accounts handled

---

### FR-8: SSO Bypass (Break Glass)

**Requirement:**
Provide emergency access when SSO is unavailable.

**Details:**
- Designated break-glass accounts
- Password-based login (disabled by default)
- Audit log for break-glass access
- Alert on break-glass usage

**Acceptance Criteria:**
- [ ] Break-glass accounts work
- [ ] Disabled by default
- [ ] All access logged
- [ ] Alerts sent

---

### FR-9: Attribute Mapping

**Requirement:**
Map IdP attributes to MindWeave user fields.

**Details:**
- Configurable attribute mapping
- Transform rules (e.g., lowercase email)
- Default values
- Required vs. optional attributes

**Acceptance Criteria:**
- [ ] Mapping UI works
- [ ] Transforms applied
- [ ] Defaults used when missing
- [ ] Required fields validated

---

### FR-10: Group to Team Mapping

**Requirement:**
Map IdP groups to MindWeave teams.

**Details:**
- Configure group-to-team mappings
- Nested group support
- Auto-assign on login
- Remove from team when removed from group

**Acceptance Criteria:**
- [ ] Group mapping configurable
- [ ] Nested groups work
- [ ] Team assignment on login
- [ ] Removal works correctly

---

## Non-Functional Requirements

### NFR-1: Performance

| Metric | Requirement |
|--------|-------------|
| Login latency | <2 seconds (excluding IdP) |
| SCIM sync | <1 minute for 1000 users |
| Session validation | <50ms |
| Token refresh | <500ms |

### NFR-2: Security

| Requirement | Implementation |
|-------------|----------------|
| SAML signatures | RSA-SHA256 minimum |
| Encryption | AES-256 for assertions |
| Token storage | Encrypted at rest |
| Certificate rotation | Support without downtime |

### NFR-3: Availability

| Metric | Requirement |
|--------|-------------|
| SSO availability | 99.99% |
| Graceful degradation | Cache sessions on IdP failure |
| Failover | Multi-region IdP config |

---

## Data Model

```sql
-- SSO configurations table
CREATE TABLE sso_configs (
  id UUID PRIMARY KEY,
  org_id UUID REFERENCES orgs(id) UNIQUE,
  provider VARCHAR(50) NOT NULL,
  protocol VARCHAR(20) DEFAULT 'saml',

  -- SAML settings
  idp_entity_id VARCHAR(500),
  idp_sso_url VARCHAR(500),
  idp_slo_url VARCHAR(500),
  idp_certificate TEXT,

  -- OIDC settings
  oidc_issuer VARCHAR(500),
  oidc_client_id VARCHAR(255),
  oidc_client_secret_encrypted TEXT,

  -- SCIM settings
  scim_enabled BOOLEAN DEFAULT false,
  scim_token_hash VARCHAR(64),
  scim_last_sync TIMESTAMP,

  -- Configuration
  jit_enabled BOOLEAN DEFAULT true,
  default_team_id UUID REFERENCES teams(id),
  default_role VARCHAR(50) DEFAULT 'member',
  session_timeout_minutes INTEGER DEFAULT 480,
  idle_timeout_minutes INTEGER DEFAULT 30,
  mfa_required BOOLEAN DEFAULT false,

  -- Status
  status VARCHAR(50) DEFAULT 'pending',
  verified_at TIMESTAMP,

  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Email domains for SSO routing
CREATE TABLE sso_domains (
  id UUID PRIMARY KEY,
  org_id UUID REFERENCES orgs(id),
  domain VARCHAR(255) NOT NULL,
  verified BOOLEAN DEFAULT false,
  verification_token VARCHAR(64),
  verified_at TIMESTAMP,

  UNIQUE(domain)
);

-- Attribute mappings
CREATE TABLE sso_attribute_mappings (
  id UUID PRIMARY KEY,
  sso_config_id UUID REFERENCES sso_configs(id),
  mindweave_field VARCHAR(100) NOT NULL,
  idp_attribute VARCHAR(255) NOT NULL,
  transform VARCHAR(50),
  default_value VARCHAR(255),
  required BOOLEAN DEFAULT false
);

-- Group to team mappings
CREATE TABLE sso_group_mappings (
  id UUID PRIMARY KEY,
  sso_config_id UUID REFERENCES sso_configs(id),
  idp_group_id VARCHAR(255) NOT NULL,
  idp_group_name VARCHAR(255),
  team_id UUID REFERENCES teams(id),

  UNIQUE(sso_config_id, idp_group_id)
);

-- User sessions
CREATE TABLE user_sessions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  session_token_hash VARCHAR(64) UNIQUE,
  idp_session_id VARCHAR(255),
  ip_address INET,
  user_agent VARCHAR(500),
  created_at TIMESTAMP DEFAULT NOW(),
  last_activity TIMESTAMP DEFAULT NOW(),
  expires_at TIMESTAMP NOT NULL,
  revoked_at TIMESTAMP,
  revoked_by UUID REFERENCES users(id)
);

-- Indexes
CREATE INDEX idx_sso_domain ON sso_domains(domain);
CREATE INDEX idx_session_user ON user_sessions(user_id);
CREATE INDEX idx_session_expires ON user_sessions(expires_at);
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/sso/login` | POST | Initiate SSO login |
| `/auth/sso/callback` | POST | Handle IdP callback |
| `/auth/sso/logout` | POST | SSO logout |
| `/auth/sso/metadata` | GET | SP metadata XML |
| `/api/sso/config` | GET | Get SSO configuration |
| `/api/sso/config` | PUT | Update SSO configuration |
| `/api/sso/domains` | GET | List verified domains |
| `/api/sso/domains` | POST | Add domain |
| `/api/sso/domains/:id/verify` | POST | Verify domain |
| `/api/sso/mappings` | GET | Get attribute mappings |
| `/api/sso/mappings` | PUT | Update attribute mappings |
| `/api/sso/groups` | GET | Get group mappings |
| `/api/sso/groups` | PUT | Update group mappings |
| `/api/sso/test` | POST | Test SSO configuration |
| `/scim/v2/Users` | GET | SCIM list users |
| `/scim/v2/Users` | POST | SCIM create user |
| `/scim/v2/Users/:id` | GET | SCIM get user |
| `/scim/v2/Users/:id` | PUT | SCIM update user |
| `/scim/v2/Users/:id` | DELETE | SCIM delete user |
| `/scim/v2/Groups` | GET | SCIM list groups |
| `/scim/v2/Groups` | POST | SCIM create group |

---

## Authentication Flows

### SP-Initiated SAML Flow

```
┌──────────┐     ┌──────────────┐     ┌───────────┐
│  User    │     │  MindWeave   │     │   IdP     │
└────┬─────┘     └──────┬───────┘     └─────┬─────┘
     │                  │                   │
     │ 1. Access App    │                   │
     │─────────────────>│                   │
     │                  │                   │
     │                  │ 2. Redirect to IdP│
     │                  │   (AuthnRequest)  │
     │<─────────────────┼──────────────────>│
     │                  │                   │
     │                  │                   │
     │                  │  3. Authenticate  │
     │                  │<──────────────────│
     │                  │                   │
     │  4. Login Form   │                   │
     │<─────────────────────────────────────│
     │                  │                   │
     │  5. Credentials  │                   │
     │─────────────────────────────────────>│
     │                  │                   │
     │                  │                   │
     │                  │ 6. SAML Response  │
     │                  │   (Assertion)     │
     │<─────────────────┼───────────────────│
     │                  │                   │
     │  7. Session      │                   │
     │   Created        │                   │
     │<─────────────────│                   │
     │                  │                   │
```

### SCIM Provisioning Flow

```
┌──────────┐     ┌───────────┐     ┌──────────────┐
│   IdP    │     │   SCIM    │     │  MindWeave   │
│  Admin   │     │  Gateway  │     │   Database   │
└────┬─────┘     └─────┬─────┘     └──────┬───────┘
     │                 │                  │
     │ 1. Create User  │                  │
     │────────────────>│                  │
     │                 │ 2. POST /Users   │
     │                 │─────────────────>│
     │                 │                  │
     │                 │ 3. Validate &    │
     │                 │    Create        │
     │                 │<─────────────────│
     │ 4. 201 Created  │                  │
     │<────────────────│                  │
     │                 │                  │
     │ 5. Add to Group │                  │
     │────────────────>│                  │
     │                 │ 6. PATCH /Groups │
     │                 │─────────────────>│
     │                 │                  │
     │                 │ 7. Update Team   │
     │                 │   Membership     │
     │                 │<─────────────────│
     │ 8. 200 OK       │                  │
     │<────────────────│                  │
     │                 │                  │
```

---

## IdP-Specific Configuration

### Okta

| Setting | Value |
|---------|-------|
| App Type | SAML 2.0 |
| SSO URL | `https://app.mindweave.ai/auth/sso/callback` |
| Audience URI | `https://app.mindweave.ai` |
| Name ID | Email |
| SCIM | Enabled |

### Azure AD

| Setting | Value |
|---------|-------|
| App Type | Enterprise Application |
| SSO Mode | SAML-based |
| Identifier | `https://app.mindweave.ai` |
| Reply URL | `https://app.mindweave.ai/auth/sso/callback` |
| Provisioning | SCIM 2.0 |

### Google Workspace

| Setting | Value |
|---------|-------|
| App Type | SAML App |
| ACS URL | `https://app.mindweave.ai/auth/sso/callback` |
| Entity ID | `https://app.mindweave.ai` |
| Start URL | `https://app.mindweave.ai` |
| Provisioning | SCIM (via connector) |

---

## Error Handling

| Error | User Message | Resolution |
|-------|--------------|------------|
| Invalid SAML Response | "Authentication failed. Please try again." | Check IdP configuration |
| Certificate Mismatch | "Security verification failed." | Upload correct certificate |
| Session Expired | "Your session has expired. Please log in again." | Re-authenticate |
| IdP Unreachable | "Unable to reach identity provider." | Check IdP status |
| User Not Provisioned | "Your account is not set up. Contact your admin." | Enable JIT or SCIM |
| MFA Required | "Multi-factor authentication required." | Complete MFA on IdP |

---

## Compliance Mapping

### SOC 2 Controls

| Control | Implementation |
|---------|----------------|
| CC6.1 (Logical Access) | SSO enforces centralized access |
| CC6.2 (Authentication) | SAML/OIDC authentication |
| CC6.3 (Authorization) | Role-based access from IdP |

### GDPR

| Article | Implementation |
|---------|----------------|
| Art. 32 (Security) | Encrypted authentication |
| Art. 25 (Privacy by Design) | Minimal data collection |

---

## Related Documents

- [PRD-MVP.md](../PRD-MVP.md) - MVP requirements
- [FEATURE-TEAM-MANAGEMENT.md](./FEATURE-TEAM-MANAGEMENT.md) - Team integration
- [../wireframes/WIREFRAME-LOGIN.md](../wireframes/WIREFRAME-LOGIN.md) - Login wireframes

---

*Last Updated: December 2025*
*Owner: Engineering Lead*
