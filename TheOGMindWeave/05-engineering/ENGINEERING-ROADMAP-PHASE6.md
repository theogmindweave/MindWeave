# 🛠️ MindWeave Engineering Roadmap: Mock-First MVP Architecture
**Iteration 2, Phase 6 Deliverable**
**Created:** December 29, 2025
**Version:** 1.0 - Engineering Strategy

---

## EXECUTIVE SUMMARY

**Tech Stack:** Next.js 15 (frontend) + NestJS (backend) + PostgreSQL + Vercel/Railway
**Architecture Approach:** Mock-first (design + mock → validate → code)
**MVP Timeline:** 2 weeks to functional product (Week 1-2 post-kickoff)
**Team Size:** 5 engineers (frontend × 2, backend × 2, infrastructure × 1)
**Success Metric:** Launch Week 2, zero critical bugs, 90% uptime

**Philosophy:** Speed + simplicity over complexity. Every feature exists because customers directly asked for it.

---

## 1️⃣ MOCK-FIRST ARCHITECTURE: WHY & HOW

### The Mock-First Approach

**Traditional Waterfall:** Design → Code Backend → Code Frontend → Integration → Testing (slow)
**Mock-First:** Design → Mock UI → Code Frontend in parallel → Code Backend → Integration (fast)

**Why We Use It:**
1. **Validation:** See the product before building it
2. **Parallelization:** Frontend team can work while backend figures out API
3. **Design clarity:** Mocks make requirements crystal clear
4. **Customer feedback:** Design partners see UI early (Week 1)
5. **Speed:** Actual build time 50% faster

### Phase 1: Design + Mock (Days 1-3)

**Deliverable:** Interactive mockup (Figma)
**Team:** 1 designer + product manager
**Work:**
- [ ] Dashboard design (4 screens)
- [ ] Cost attribution design (3 screens)
- [ ] MCP registry design (3 screens)
- [ ] Settings/permissions design (2 screens)
- [ ] Export/reporting design (1 screen)
- [ ] Interactive prototype (clickable)

**Design Principles:**
- ✅ Minimal visual complexity (enterprise, not consumer)
- ✅ Clear information hierarchy (most important data first)
- ✅ Accessibility (WCAG 2.1 AA)
- ✅ Mobile-responsive (but desktop-first)

**Day 4-5:** Share with design partners → collect feedback

---

### Phase 2: API Definition (Days 1-4)

**Deliverable:** OpenAPI spec + GraphQL schema
**Team:** Product manager + backend lead
**Work:**
- [ ] Define endpoints (20-30 endpoints for MVP)
- [ ] Define request/response schemas
- [ ] Define error handling
- [ ] Define auth/authorization
- [ ] Define rate limiting

**Example Endpoints:**
```
GET /api/v1/usage - Get dashboard data
POST /api/v1/teams - Create team
GET /api/v1/teams/{id}/permissions - Get team permissions
POST /api/v1/teams/{id}/permissions - Update permissions
GET /api/v1/mcps - List all MCPs
GET /api/v1/mcps/duplicates - Get duplicate detection
GET /api/v1/audit-logs - Get compliance logs
POST /api/v1/export/csv - Export data
```

**Documentation:** Swagger/OpenAPI spec (shared with frontend team)

---

### Phase 3: Frontend Development (Days 3-10)

**Team:** 2 frontend engineers
**Tech Stack:** Next.js 15 + React 19 + TailwindCSS + TypeScript
**Deliverable:** Functional UI (connected to mocks, not real backend)

**Week 1:**
- [ ] Set up Next.js project (routing, auth)
- [ ] Build dashboard component (usage, costs, trends)
- [ ] Build cost attribution component
- [ ] Build MCP registry component
- [ ] Connect to mock data (JSON file or Mirage.js)
- [ ] Style with TailwindCSS

**Week 2:**
- [ ] Build settings/permissions component
- [ ] Build export functionality (CSV download)
- [ ] Add user authentication (Clerk SSO)
- [ ] Add error states + loading states
- [ ] Performance optimization (lighthouse 90+)
- [ ] Accessibility audit (WCAG)

**Frontend Checklist:**
- ✅ All MVP features implemented
- ✅ Mobile responsive (tested on iPhone + tablet)
- ✅ Dark mode support
- ✅ Error states documented
- ✅ Loading states (skeleton screens)
- ✅ Unit tests for critical flows (80%+ coverage)

---

### Phase 4: Backend Development (Days 5-10)

**Team:** 2 backend engineers
**Tech Stack:** NestJS + TypeScript + PostgreSQL (Prisma ORM) + Redis (caching)

**Week 1:**
- [ ] Set up NestJS project (structure, modules)
- [ ] Implement authentication (JWT, SSO with Clerk)
- [ ] Implement database schema (users, teams, MCPs, audit logs)
- [ ] Implement API endpoints (20-30 endpoints)
- [ ] Implement API mocking (for frontend integration testing)
- [ ] Error handling + validation

**Week 2:**
- [ ] Connect to Claude API (token counting)
- [ ] Implement cost calculation logic
- [ ] Implement MCP duplicate detection (ML model)
- [ ] Implement audit logging (every action logged)
- [ ] Implement permission enforcement
- [ ] Performance optimization (query caching, indexing)
- [ ] Rate limiting

**Backend Checklist:**
- ✅ All endpoints implemented
- ✅ Database migrations created
- ✅ Authentication working (Clerk SSO)
- ✅ Audit logs capturing all actions
- ✅ Error handling comprehensive
- ✅ Unit + integration tests (80%+ coverage)
- ✅ Load testing done (1K req/sec target)

---

### Phase 5: Integration (Days 8-10)

**Team:** All engineers
**Work:**
- [ ] Connect frontend to real backend APIs
- [ ] End-to-end testing
- [ ] Bug fixing (P0/P1 priority)
- [ ] Performance testing
- [ ] Security testing (OWASP)
- [ ] Accessibility final audit

**Integration Checklist:**
- ✅ All APIs connected + working
- ✅ Data flowing correctly
- ✅ No console errors
- ✅ No unhandled promises
- ✅ Authentication working end-to-end
- ✅ Audit logs working
- ✅ Performance acceptable (dashboard <3sec load)

---

## 2️⃣ TECH STACK RATIONALE

### Frontend: Next.js 15 + React 19
**Why Next.js:**
- ✅ Server-side rendering (SEO + performance)
- ✅ API routes (no need for separate backend initially)
- ✅ Built-in optimization (image, code splitting)
- ✅ File-based routing (simple + scalable)
- ✅ Vercel deployment (zero-config)

**Alternatives Considered:**
- ❌ React SPA: No SSR, slower initial load, worse SEO
- ❌ Vue: Less ecosystem, smaller community
- ✅ Next.js wins for MVP speed

### Backend: NestJS
**Why NestJS:**
- ✅ TypeScript (type safety)
- ✅ Modular architecture (scalable)
- ✅ Built-in DI + testing support
- ✅ Active community + ecosystem
- ✅ Enterprise-ready

**Alternatives Considered:**
- 🟡 Node.js Express: Simple but less structured for scaling
- 🟡 FastAPI: Great but requires Python (different from frontend team)
- ✅ NestJS wins for structure + scale

### Database: PostgreSQL + Prisma
**Why PostgreSQL:**
- ✅ Relational model (users, teams, MCPs, logs)
- ✅ ACID compliance (data integrity)
- ✅ Mature + stable
- ✅ Great for analytics queries (cost attribution)

**Why Prisma ORM:**
- ✅ Type-safe queries (no SQL strings)
- ✅ Migrations built-in
- ✅ Query builder is intuitive
- ✅ Auto-generated types match schema

### Infrastructure: Vercel + Railway
**Why Vercel for Frontend:**
- ✅ Next.js native support
- ✅ Zero-config deployment
- ✅ Automatic scaling
- ✅ Built-in CDN

**Why Railway for Backend:**
- ✅ Docker-based (flexible)
- ✅ Simple scaling
- ✅ Good pricing
- ✅ PostgreSQL managed service

---

## 3️⃣ MVP FEATURE BREAKDOWN

### Feature 1: Real-Time Dashboard
**Complexity:** Medium
**Time Estimate:** 5 days (frontend 3, backend 2)
**Components:**
- Usage trends (line chart)
- Top engineers (table)
- Top projects (table)
- Cost summary (metric cards)

**Data Model:**
```
users → tokens_consumed
projects → tokens_consumed
teams → total_tokens
```

---

### Feature 2: Cost Attribution
**Complexity:** Medium
**Time Estimate:** 4 days (frontend 2, backend 2)
**Components:**
- Team selector
- Cost breakdown table
- Export to CSV
- Time period filter

**Data Model:**
```
teams → users → tokens
teams → projects → tokens
cost_attribution = tokens × $per_token
```

---

### Feature 3: MCP Registry
**Complexity:** Medium-High
**Time Estimate:** 5 days (frontend 2, backend 3)
**Components:**
- MCP list (table)
- MCP details (modal)
- Owner assignment
- Permission controls

**Data Model:**
```
mcps → name, owner_team, created_at
mcp_permissions → team, permission_level
```

---

### Feature 4: Hivemind Duplicate Detection
**Complexity:** High
**Time Estimate:** 4 days (backend 3, frontend 1)
**Algorithm:**
- ML-based function similarity (embedding)
- Confidence scoring (80%+)
- Suggest to user

**Data Model:**
```
mcp_duplicates → mcp1_id, mcp2_id, confidence
```

---

### Feature 5: Audit Logs
**Complexity:** Medium
**Time Estimate:** 3 days (backend 2, frontend 1)
**Components:**
- Audit log table
- Filter by action/user/date
- Export functionality

**Logged Events:**
```
user_login, user_logout, mcp_accessed, mcp_created, permission_changed,
export_created, etc.
```

---

### Feature 6: Team-Based Permissions
**Complexity:** Medium
**Time Estimate:** 4 days (backend 2, frontend 2)
**Components:**
- Permission matrix (team × role)
- Role selector
- Enforcement logic

**Roles:**
- Owner (full access)
- Member (use MCPs, see usage)
- View-Only (read usage only)

---

## 4️⃣ DEPLOYMENT PIPELINE

### Development (Local)
```
git clone → npm install → npm run dev
```

### CI/CD (GitHub Actions)
```
On every push:
1. Run tests (unit + integration)
2. Build + lint
3. Deploy to staging (if main branch)
4. Run e2e tests
5. Deploy to production (if approved)
```

### Environments
- **Development:** Local machine
- **Staging:** Railway staging environment
- **Production:** Vercel (frontend) + Railway (backend)

### Database Migrations
```
1. Create migration file
2. Write SQL/Prisma migration
3. Test locally
4. Deploy to staging
5. Deploy to production (during low traffic)
```

---

## 5️⃣ TESTING STRATEGY

### Unit Tests (80%+ coverage)
**Frontend:**
- Component rendering
- User interactions
- Form validation
- Data transformation

**Backend:**
- Business logic
- Data validation
- Error handling
- Permission checks

### Integration Tests
- API endpoint testing
- Database integration
- Authentication flow
- Permission enforcement

### E2E Tests
- Complete user journeys
- Dashboard → export flow
- Permission changes
- Audit log verification

### Performance Testing
- Dashboard load time target: <3 sec
- API response target: <200ms
- Database query target: <100ms

---

## 6️⃣ SECURITY CHECKLIST

**Authentication:**
- [ ] Clerk SSO integration (no passwords)
- [ ] JWT token validation
- [ ] CORS properly configured
- [ ] Rate limiting (100 req/min per user)

**Authorization:**
- [ ] Team-based access control
- [ ] Permission checks on every endpoint
- [ ] No direct object references (IDOR test)

**Data Protection:**
- [ ] All data encrypted in transit (TLS 1.3)
- [ ] Passwords never logged
- [ ] API keys stored securely (environment variables)
- [ ] Database backups encrypted

**Compliance:**
- [ ] OWASP Top 10 checklist
- [ ] SQL injection testing
- [ ] XSS testing
- [ ] CSRF protection

---

## 7️⃣ LAUNCH READINESS CHECKLIST

**Week 2 Pre-Launch (Day 10-12):**
- [ ] All MVP features working
- [ ] 0 critical bugs (P0)
- [ ] <5 high bugs (P1)
- [ ] Unit test coverage 80%+
- [ ] Load testing passed (1K req/sec)
- [ ] Security audit passed
- [ ] Performance optimization done
- [ ] Documentation written (API, deployment)
- [ ] Monitoring set up (error tracking, analytics)
- [ ] Backup strategy tested
- [ ] Rollback procedure documented

**Week 2 Launch Day:**
- [ ] Marketing assets ready (screenshots, GIFs)
- [ ] Email notifications sent to waitlist
- [ ] Support ticket system ready
- [ ] Analytics tracking enabled
- [ ] Customer onboarding docs ready

---

## ✅ PHASE 6 ENGINEERING ROADMAP COMPLETE

**Deliverables Completed:**
1. ✅ ENGINEERING-ROADMAP-PHASE6.md - Mock-first architecture, 2-week timeline, tech stack rationale
2. ✅ Feature breakdown (6 core features, complexity estimates)
3. ✅ Deployment pipeline + CI/CD
4. ✅ Testing + security strategy
5. ✅ Launch readiness checklist

**Ready for Council Review:**
- ✅ Engineering Lead (architecture, timeline, feasibility)
- ✅ Product Architect (feature spec, integration approach)

**Next Phase:** Phase 7 - Compliance & Regulatory Roadmap (Iteration 3)

---

**Document Version:** 1.0
**Phase:** Iteration 2, Phase 6
**Status:** ✅ Ready for Council Review
**Council Reviewers:** Engineering Lead + Product Architect
**Next:** Phase 7 Compliance & Regulatory Roadmap

Iteration 2 COMPLETE (Phase 4-6): Product → GTM → Engineering
Foundation phase complete. Ready to move to Iteration 3: Compliance → Finance → Execution → Launch (Phase 7-10)
