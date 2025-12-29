# MindWeave Incident Response

## Document Information

| Field | Value |
|-------|-------|
| Document ID | MW-ENG-074 |
| Version | 1.0.0 |
| Last Updated | 2025-01-15 |
| Owner | Platform Engineering |
| Classification | Internal |
| Status | Active |

---

## Executive Summary

This document defines MindWeave's incident response procedures, covering incident classification, escalation paths, communication protocols, and post-incident review processes. Our approach ensures rapid detection, coordinated response, and continuous improvement.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INCIDENT RESPONSE LIFECYCLE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐        │
│   │ Detection │───►│  Triage   │───►│ Response  │───►│ Recovery  │        │
│   │           │    │           │    │           │    │           │        │
│   │ • Alerts  │    │ • Classify│    │ • Mitigate│    │ • Restore │        │
│   │ • Reports │    │ • Assign  │    │ • Contain │    │ • Verify  │        │
│   │ • Monitor │    │ • Notify  │    │ • Resolve │    │ • Close   │        │
│   └───────────┘    └───────────┘    └───────────┘    └───────────┘        │
│         │                                                   │               │
│         │                                                   │               │
│         └───────────────────────────────────────────────────┘               │
│                               │                                             │
│                               ▼                                             │
│                        ┌───────────┐                                       │
│                        │  Review   │                                       │
│                        │           │                                       │
│                        │ • Analyze │                                       │
│                        │ • Learn   │                                       │
│                        │ • Improve │                                       │
│                        └───────────┘                                       │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                    INCIDENT SEVERITY LEVELS                          │  │
│   ├──────────┬──────────────────────┬───────────────┬───────────────────┤  │
│   │ Severity │ Description          │ Response Time │ Resolution Target │  │
│   ├──────────┼──────────────────────┼───────────────┼───────────────────┤  │
│   │   SEV-1  │ Critical - Service   │ 5 minutes     │ 1 hour            │  │
│   │          │ down/data breach     │               │                   │  │
│   ├──────────┼──────────────────────┼───────────────┼───────────────────┤  │
│   │   SEV-2  │ Major - Significant  │ 15 minutes    │ 4 hours           │  │
│   │          │ degradation          │               │                   │  │
│   ├──────────┼──────────────────────┼───────────────┼───────────────────┤  │
│   │   SEV-3  │ Moderate - Limited   │ 1 hour        │ 24 hours          │  │
│   │          │ impact               │               │                   │  │
│   ├──────────┼──────────────────────┼───────────────┼───────────────────┤  │
│   │   SEV-4  │ Low - Minor issue    │ 4 hours       │ 72 hours          │  │
│   │          │ no customer impact   │               │                   │  │
│   └──────────┴──────────────────────┴───────────────┴───────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Incident Classification

### 1.1 Severity Definitions

| Severity | Impact | Examples | Initial Response |
|----------|--------|----------|------------------|
| **SEV-1** | Critical - Complete service outage or security breach affecting all customers | Total platform outage, data breach, payment processing failure, complete API unavailability | Page on-call immediately, all-hands response |
| **SEV-2** | Major - Significant degradation affecting many customers | Major feature broken, >50% error rate, significant latency (>10x normal), partial outage | Page on-call, escalate to team leads |
| **SEV-3** | Moderate - Limited impact affecting some customers | Feature degradation, elevated error rates (<50%), minor data inconsistency | Notify on-call, respond during business hours |
| **SEV-4** | Low - Minor issue with no customer-facing impact | Internal tool issues, non-critical bugs, documentation errors | Queue for regular sprint work |

### 1.2 Classification Decision Tree

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INCIDENT CLASSIFICATION FLOWCHART                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                        ┌────────────────┐                                   │
│                        │ Is there a     │                                   │
│                        │ security       │                                   │
│                        │ breach?        │                                   │
│                        └───────┬────────┘                                   │
│                                │                                            │
│                     ┌──────────┴──────────┐                                 │
│                     │                     │                                 │
│                    YES                   NO                                 │
│                     │                     │                                 │
│                     ▼                     ▼                                 │
│              ┌──────────┐        ┌────────────────┐                        │
│              │  SEV-1   │        │ Is the service │                        │
│              │ CRITICAL │        │ completely     │                        │
│              └──────────┘        │ unavailable?   │                        │
│                                  └───────┬────────┘                        │
│                                          │                                  │
│                               ┌──────────┴──────────┐                      │
│                               │                     │                      │
│                              YES                   NO                      │
│                               │                     │                      │
│                               ▼                     ▼                      │
│                        ┌──────────┐        ┌────────────────┐             │
│                        │  SEV-1   │        │ Is >50% of     │             │
│                        │ CRITICAL │        │ functionality  │             │
│                        └──────────┘        │ affected?      │             │
│                                            └───────┬────────┘             │
│                                                    │                       │
│                                         ┌──────────┴──────────┐           │
│                                         │                     │           │
│                                        YES                   NO           │
│                                         │                     │           │
│                                         ▼                     ▼           │
│                                  ┌──────────┐        ┌────────────────┐  │
│                                  │  SEV-2   │        │ Does it affect │  │
│                                  │  MAJOR   │        │ customers?     │  │
│                                  └──────────┘        └───────┬────────┘  │
│                                                              │            │
│                                                   ┌──────────┴──────────┐│
│                                                   │                     ││
│                                                  YES                   NO │
│                                                   │                     │ │
│                                                   ▼                     ▼ │
│                                            ┌──────────┐        ┌──────────┐│
│                                            │  SEV-3   │        │  SEV-4   ││
│                                            │ MODERATE │        │   LOW    ││
│                                            └──────────┘        └──────────┘│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. On-Call Structure

### 2.1 On-Call Rotation

```yaml
# pagerduty/on-call-schedules.yaml

schedules:
  - name: Primary On-Call
    description: First responders for all production incidents
    rotation:
      type: weekly
      start_time: "09:00"
      timezone: America/New_York
      handoff_day: monday
    escalation_timeout: 5m
    members:
      - platform-team
    coverage:
      - type: "24x7"

  - name: Secondary On-Call
    description: Backup responders and escalation path
    rotation:
      type: weekly
      start_time: "09:00"
      timezone: America/New_York
      handoff_day: monday
    escalation_timeout: 15m
    members:
      - platform-team-leads

  - name: Engineering Manager On-Call
    description: Management escalation for SEV-1 incidents
    rotation:
      type: weekly
      members:
        - engineering-managers
    escalation_timeout: 10m

escalation_policies:
  - name: Production Incidents
    rules:
      - level: 1
        schedule: Primary On-Call
        timeout: 5m
      - level: 2
        schedule: Secondary On-Call
        timeout: 10m
      - level: 3
        schedule: Engineering Manager On-Call
        timeout: 15m
      - level: 4
        users:
          - vp-engineering
        timeout: 30m
```

### 2.2 On-Call Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Acknowledge** | Acknowledge all pages within 5 minutes |
| **Triage** | Assess severity and impact of incidents |
| **Coordinate** | Lead incident response, coordinate responders |
| **Communicate** | Update status page, notify stakeholders |
| **Document** | Create incident ticket, maintain timeline |
| **Escalate** | Escalate to appropriate teams when needed |
| **Handoff** | Properly hand off to next on-call rotation |

### 2.3 On-Call Checklist

```markdown
## Daily On-Call Checklist

### Start of Shift
- [ ] Check PagerDuty app is working and notifications enabled
- [ ] Review any ongoing incidents from previous shift
- [ ] Check monitoring dashboards for anomalies
- [ ] Verify access to all critical systems
- [ ] Review recent deployments and changes

### During Shift
- [ ] Respond to all pages within 5 minutes
- [ ] Keep incident channels updated
- [ ] Document all actions taken
- [ ] Escalate if resolution is taking too long

### End of Shift
- [ ] Hand off any ongoing incidents to next on-call
- [ ] Document any unresolved issues
- [ ] Update on-call log with shift summary
- [ ] Ensure next on-call has acknowledged handoff
```

---

## 3. Incident Response Process

### 3.1 Phase 1: Detection

```yaml
# Detection Sources

automated_alerts:
  - source: DataDog
    types:
      - Error rate threshold exceeded
      - Latency P99 exceeded
      - Service health check failures
      - Resource utilization alerts
  - source: PagerDuty
    types:
      - Aggregated alerts from monitoring systems
  - source: AWS CloudWatch
    types:
      - Infrastructure alerts
      - RDS/ElastiCache/MSK alerts

manual_reports:
  - source: Customer Support
    channel: "#support-escalations"
  - source: Engineering Team
    channel: "#engineering"
  - source: Status Page Reports
    url: https://status.mindweave.io/report
```

### 3.2 Phase 2: Triage

```markdown
## Triage Runbook

### Step 1: Acknowledge the Alert
1. Acknowledge in PagerDuty
2. Join #incident-response Slack channel
3. Create incident ticket if not auto-created

### Step 2: Initial Assessment (5 minutes)
1. What service/component is affected?
2. What is the customer impact?
3. When did the issue start?
4. Are there any recent deployments or changes?

### Step 3: Classify Severity
- Use the classification decision tree
- Update incident severity in PagerDuty
- Notify appropriate stakeholders

### Step 4: Assemble Response Team
- For SEV-1/SEV-2: Page additional responders
- Assign roles:
  - Incident Commander (IC)
  - Technical Lead
  - Communications Lead

### Step 5: Begin Response
- Create incident channel: #inc-YYYYMMDD-brief-description
- Post initial status update
- Begin investigation
```

### 3.3 Phase 3: Response

```yaml
# Incident Response Roles

incident_commander:
  responsibilities:
    - Coordinate overall response
    - Make decisions on actions
    - Manage communication
    - Track timeline
    - Approve production changes
  actions:
    - "Declare incident severity"
    - "Assign roles to team members"
    - "Coordinate investigation"
    - "Approve mitigation actions"
    - "Communicate with stakeholders"

technical_lead:
  responsibilities:
    - Lead technical investigation
    - Propose mitigation strategies
    - Execute fixes
    - Verify resolution
  actions:
    - "Analyze logs and metrics"
    - "Identify root cause"
    - "Implement fixes"
    - "Verify service restoration"

communications_lead:
  responsibilities:
    - Update status page
    - Communicate with customers
    - Send internal updates
    - Manage external inquiries
  actions:
    - "Update status.mindweave.io"
    - "Send customer notifications"
    - "Post updates to #incidents"
    - "Coordinate with support team"
```

### 3.4 Phase 4: Recovery

```markdown
## Recovery Checklist

### Service Restoration
- [ ] Implement fix/rollback
- [ ] Verify fix in staging (if time permits)
- [ ] Deploy fix to production
- [ ] Monitor for 15 minutes after fix
- [ ] Verify all health checks passing
- [ ] Confirm customer-facing functionality

### Verification Steps
- [ ] All services showing healthy
- [ ] Error rates returned to baseline
- [ ] Latency returned to normal
- [ ] No new alerts triggered
- [ ] Customer reports resolved

### Incident Closure
- [ ] Update status page to "Resolved"
- [ ] Send final customer communication
- [ ] Update incident ticket with resolution
- [ ] Schedule post-incident review
- [ ] Archive incident channel
```

### 3.5 Phase 5: Post-Incident Review

```markdown
## Post-Incident Review Template

### Incident Summary
- **Incident ID**: INC-YYYY-NNNN
- **Severity**: SEV-X
- **Duration**: HH:MM
- **Impact**: [Description of customer/business impact]

### Timeline
| Time (UTC) | Event |
|------------|-------|
| HH:MM | Alert triggered |
| HH:MM | Incident acknowledged |
| HH:MM | IC assigned |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | Service restored |
| HH:MM | Incident closed |

### Root Cause Analysis
**What happened?**
[Detailed description of the failure]

**Why did it happen?**
[5 Whys analysis]
1. Why?
2. Why?
3. Why?
4. Why?
5. Why? (Root cause)

### Contributing Factors
- [ ] Code change
- [ ] Configuration change
- [ ] Infrastructure issue
- [ ] Third-party dependency
- [ ] Capacity/scaling
- [ ] Human error
- [ ] Process gap

### Impact Assessment
- **Customers affected**: N
- **Revenue impact**: $X
- **SLA impact**: X minutes of downtime

### Action Items
| Priority | Action | Owner | Due Date |
|----------|--------|-------|----------|
| P0 | [Immediate fix] | @owner | [date] |
| P1 | [Short-term improvement] | @owner | [date] |
| P2 | [Long-term improvement] | @owner | [date] |

### Lessons Learned
**What went well?**
-

**What could be improved?**
-

### Prevention Measures
- [ ] Add monitoring for [condition]
- [ ] Update runbook for [scenario]
- [ ] Implement [safeguard]
```

---

## 4. Runbooks

### 4.1 Service Down Runbook

```markdown
# Runbook: Service Unavailable

## Symptoms
- Health check failures
- 5xx errors from API
- Alerts: "ServiceDown", "HealthCheckFailed"

## Quick Diagnosis

### Step 1: Check Pod Status
```bash
kubectl get pods -n mindweave-services -l app=api-gateway
kubectl describe pod <pod-name> -n mindweave-services
```

### Step 2: Check Recent Events
```bash
kubectl get events -n mindweave-services --sort-by='.lastTimestamp' | head -20
```

### Step 3: Check Logs
```bash
kubectl logs -n mindweave-services -l app=api-gateway --tail=100 --since=5m
```

### Step 4: Check Dependencies
- [ ] Database connectivity
- [ ] Redis connectivity
- [ ] Kafka connectivity

## Common Causes & Resolutions

### 1. Pod OOMKilled
**Symptoms**: Pod status shows OOMKilled
**Resolution**:
```bash
# Increase memory limits
kubectl patch deployment api-gateway -n mindweave-services \
  -p '{"spec":{"template":{"spec":{"containers":[{"name":"api-gateway","resources":{"limits":{"memory":"2Gi"}}}]}}}}'
```

### 2. Failed Deployment
**Symptoms**: New pods not starting, old pods terminated
**Resolution**:
```bash
# Rollback to previous version
kubectl rollout undo deployment/api-gateway -n mindweave-services
kubectl rollout status deployment/api-gateway -n mindweave-services
```

### 3. Database Connection Issues
**Symptoms**: Connection refused/timeout errors in logs
**Resolution**:
```bash
# Check database status
aws rds describe-db-instances --db-instance-identifier mindweave-production

# Check security groups
aws ec2 describe-security-groups --group-ids <sg-id>
```

### 4. Certificate Expiry
**Symptoms**: TLS handshake errors
**Resolution**:
```bash
# Check certificate expiry
kubectl get certificate -n mindweave-services
kubectl describe certificate mindweave-tls -n mindweave-services

# Force certificate renewal
kubectl delete certificate mindweave-tls -n mindweave-services
```

## Escalation
If issue persists after 15 minutes:
- Escalate to Secondary On-Call
- Page Database team if DB-related
- Page Infrastructure team if cloud-related
```

### 4.2 High Error Rate Runbook

```markdown
# Runbook: High Error Rate

## Symptoms
- Error rate > 5%
- Alerts: "HighErrorRate", "HTTP5xxSpike"

## Quick Diagnosis

### Step 1: Identify Error Types
```bash
# Query error breakdown
kubectl exec -n mindweave-monitoring prometheus-0 -- \
  promtool query instant \
  'sum(rate(http_requests_total{status_code=~"5.."}[5m])) by (status_code, path)'
```

### Step 2: Check Application Logs
```bash
# Get error logs
kubectl logs -n mindweave-services -l app=api-gateway --since=10m | grep -i error | head -50
```

### Step 3: Check Recent Deployments
```bash
kubectl rollout history deployment/api-gateway -n mindweave-services
```

### Step 4: Check External Dependencies
```bash
# Test database
kubectl exec -n mindweave-services deployment/api-gateway -- \
  pg_isready -h $DATABASE_HOST -p 5432

# Test Redis
kubectl exec -n mindweave-services deployment/api-gateway -- \
  redis-cli -h $REDIS_HOST ping

# Test external APIs
curl -s https://api.anthropic.com/health
```

## Common Causes & Resolutions

### 1. Bad Deployment
**Indicators**: Errors started after deployment
**Resolution**:
```bash
# Check deployment time vs error spike
kubectl rollout history deployment/api-gateway -n mindweave-services

# Rollback
kubectl rollout undo deployment/api-gateway -n mindweave-services
```

### 2. Database Connection Pool Exhaustion
**Indicators**: "connection pool exhausted" in logs
**Resolution**:
```bash
# Scale down to reduce connections
kubectl scale deployment/api-gateway -n mindweave-services --replicas=2

# Check and terminate idle connections
psql -h $DATABASE_HOST -U $DATABASE_USER -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'idle' AND query_start < NOW() - INTERVAL '10 minutes';"
```

### 3. Rate Limiting by External API
**Indicators**: 429 errors from external services
**Resolution**:
- Check rate limit headers in responses
- Implement backoff in calling code
- Contact API provider if limits too low

### 4. Memory Pressure
**Indicators**: Node memory high, pods evicted
**Resolution**:
```bash
# Check node resources
kubectl top nodes

# Cordon affected node
kubectl cordon <node-name>

# Scale horizontally
kubectl scale deployment/api-gateway -n mindweave-services --replicas=5
```

## Escalation
- If error rate > 50%: Escalate to SEV-1
- If caused by external service: Contact vendor support
- If database-related: Page DBA on-call
```

### 4.3 Database Issues Runbook

```markdown
# Runbook: Database Issues

## Symptoms
- Connection timeouts
- Slow queries
- Replication lag
- Alerts: "DatabaseConnectionFailed", "HighReplicationLag", "SlowQueries"

## Quick Diagnosis

### Step 1: Check RDS Status
```bash
aws rds describe-db-instances \
  --db-instance-identifier mindweave-production \
  --query 'DBInstances[0].{Status:DBInstanceStatus,CPU:PerformanceInsightsEnabled}'
```

### Step 2: Check Active Connections
```sql
SELECT
  count(*) as total,
  state,
  usename
FROM pg_stat_activity
GROUP BY state, usename
ORDER BY total DESC;
```

### Step 3: Check Long-Running Queries
```sql
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes'
ORDER BY duration DESC;
```

### Step 4: Check Replication Status
```sql
SELECT
  client_addr,
  state,
  sent_lsn,
  replay_lsn,
  pg_wal_lsn_diff(sent_lsn, replay_lsn) as replication_lag
FROM pg_stat_replication;
```

## Common Causes & Resolutions

### 1. Connection Pool Exhaustion
**Resolution**:
```sql
-- Kill idle connections
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state = 'idle'
  AND query_start < NOW() - INTERVAL '5 minutes'
  AND usename != 'rdsadmin';
```

### 2. Long-Running Queries
**Resolution**:
```sql
-- Kill specific query
SELECT pg_terminate_backend(<pid>);

-- Kill all queries longer than 10 minutes
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE duration > interval '10 minutes'
  AND state != 'idle';
```

### 3. Table Lock Contention
**Resolution**:
```sql
-- Identify blocking queries
SELECT
  blocked_locks.pid AS blocked_pid,
  blocked_activity.usename AS blocked_user,
  blocking_locks.pid AS blocking_pid,
  blocking_activity.usename AS blocking_user,
  blocked_activity.query AS blocked_statement
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity
  ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks
  ON blocking_locks.locktype = blocked_locks.locktype
  AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
  AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
  AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
  AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
  AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
  AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
  AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
  AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
  AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
  AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity
  ON blocking_activity.pid = blocking_locks.pid
WHERE NOT blocked_locks.granted;
```

### 4. Disk Space Low
**Resolution**:
```bash
# Check disk usage
aws cloudwatch get-metric-statistics \
  --namespace AWS/RDS \
  --metric-name FreeStorageSpace \
  --dimensions Name=DBInstanceIdentifier,Value=mindweave-production \
  --start-time $(date -u -d '1 hour ago' +%Y-%m-%dT%H:%M:%SZ) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%SZ) \
  --period 300 \
  --statistics Average

# Increase storage (if auto-scaling not enabled)
aws rds modify-db-instance \
  --db-instance-identifier mindweave-production \
  --allocated-storage 1000 \
  --apply-immediately
```

## Escalation
- If database unresponsive: Page DBA on-call immediately
- If data corruption suspected: Escalate to SEV-1, engage AWS support
- If replica lag > 5 minutes: Consider promoting replica
```

---

## 5. Communication Templates

### 5.1 Status Page Updates

```markdown
## Status Page Update Templates

### Investigating
**Title**: Investigating issues with [Service Name]
**Body**:
We are currently investigating reports of [brief description of issue].
Our team is working to identify the cause and we will provide updates as we learn more.

---

### Identified
**Title**: Issue identified with [Service Name]
**Body**:
We have identified the cause of the [issue type] affecting [Service Name].
Our team is implementing a fix. We expect to have this resolved within [timeframe].

**Impact**: [Description of customer impact]
**Workaround**: [If applicable]

---

### Monitoring
**Title**: Fix implemented, monitoring [Service Name]
**Body**:
We have implemented a fix for the [issue type] affecting [Service Name].
We are currently monitoring the service to ensure stability.

---

### Resolved
**Title**: Resolved - [Service Name] issue
**Body**:
The issue affecting [Service Name] has been resolved.
All systems are operating normally.

**Duration**: [Start time] - [End time] ([total duration])
**Impact**: [Summary of impact]
**Root Cause**: [Brief explanation]

We apologize for any inconvenience this may have caused.
```

### 5.2 Customer Communication

```markdown
## Customer Email Templates

### Initial Notification
**Subject**: [MindWeave] Service Disruption - We're On It

Dear Customer,

We are currently experiencing an issue with [affected service/feature] that may be impacting your experience with MindWeave.

**What's happening:**
[Brief description of the issue]

**What we're doing:**
Our engineering team has been alerted and is actively investigating this issue.

**What you can do:**
[Any workarounds or alternative steps]

We will provide updates every [30 minutes/1 hour] until this issue is resolved.

Thank you for your patience.

The MindWeave Team

---

### Resolution Notification
**Subject**: [MindWeave] Service Restored - Issue Resolved

Dear Customer,

We are pleased to inform you that the issue affecting [affected service/feature] has been resolved.

**What happened:**
[Brief explanation of the root cause]

**Impact duration:**
[Start time] to [End time] ([total duration])

**What we're doing to prevent this:**
[Brief description of preventive measures]

We apologize for any inconvenience this may have caused. If you continue to experience any issues, please contact our support team at support@mindweave.io.

Thank you for your patience and understanding.

The MindWeave Team
```

### 5.3 Internal Updates

```markdown
## Slack Update Templates

### Incident Declared
🚨 **INCIDENT DECLARED**

**Severity**: SEV-[X]
**Service**: [Affected service]
**Impact**: [Customer impact description]
**IC**: @[name]
**Channel**: #inc-[date]-[brief-description]

Please join the incident channel if you can assist.

---

### Status Update (Every 30 min for SEV-1/2)
📊 **STATUS UPDATE** - [Time]

**Current Status**: [Investigating/Identified/Implementing Fix/Monitoring]
**Progress**: [What's been done]
**Next Steps**: [What's planned]
**ETA**: [Estimated resolution time]

---

### Incident Resolved
✅ **INCIDENT RESOLVED**

**Duration**: [X hours Y minutes]
**Root Cause**: [Brief description]
**Fix Applied**: [What fixed it]
**Post-Mortem**: Scheduled for [date/time]

Thank you to everyone who helped!
```

---

## 6. Incident Tools

### 6.1 Incident Command Center

```typescript
// tools/incident-commander.ts

interface Incident {
  id: string;
  severity: 'SEV-1' | 'SEV-2' | 'SEV-3' | 'SEV-4';
  title: string;
  description: string;
  status: 'declared' | 'investigating' | 'identified' | 'fixing' | 'monitoring' | 'resolved';
  commander: string;
  technicalLead?: string;
  communicationsLead?: string;
  startTime: Date;
  endTime?: Date;
  timeline: TimelineEntry[];
  affectedServices: string[];
  customerImpact: string;
  slackChannel: string;
  statusPageIncidentId?: string;
}

interface TimelineEntry {
  timestamp: Date;
  author: string;
  action: string;
  details: string;
}

class IncidentCommander {
  async declareIncident(params: {
    severity: string;
    title: string;
    description: string;
    commander: string;
  }): Promise<Incident> {
    // Create incident record
    const incident = await this.createIncidentRecord(params);

    // Create Slack channel
    const channel = await this.createSlackChannel(incident);

    // Page appropriate responders
    await this.pageResponders(incident);

    // Create status page incident
    await this.createStatusPageIncident(incident);

    // Post initial update
    await this.postUpdate(incident, {
      action: 'incident_declared',
      details: `Incident declared by ${params.commander}`,
    });

    return incident;
  }

  async updateSeverity(incidentId: string, newSeverity: string): Promise<void> {
    const incident = await this.getIncident(incidentId);

    await this.postUpdate(incident, {
      action: 'severity_changed',
      details: `Severity changed from ${incident.severity} to ${newSeverity}`,
    });

    // Re-page if escalated
    if (this.isEscalation(incident.severity, newSeverity)) {
      await this.pageResponders({ ...incident, severity: newSeverity as any });
    }

    await this.updateIncidentRecord(incidentId, { severity: newSeverity });
  }

  async resolveIncident(incidentId: string, resolution: string): Promise<void> {
    const incident = await this.getIncident(incidentId);

    await this.postUpdate(incident, {
      action: 'incident_resolved',
      details: resolution,
    });

    // Update status page
    await this.updateStatusPageIncident(incident.statusPageIncidentId, 'resolved');

    // Send resolution notification
    await this.sendResolutionNotification(incident);

    // Archive Slack channel
    await this.archiveSlackChannel(incident.slackChannel);

    // Schedule post-mortem
    await this.schedulePostMortem(incident);

    await this.updateIncidentRecord(incidentId, {
      status: 'resolved',
      endTime: new Date(),
    });
  }

  async generateReport(incidentId: string): Promise<string> {
    const incident = await this.getIncident(incidentId);

    return `
# Incident Report: ${incident.id}

## Summary
- **Title**: ${incident.title}
- **Severity**: ${incident.severity}
- **Duration**: ${this.calculateDuration(incident)}
- **Impact**: ${incident.customerImpact}

## Timeline
${incident.timeline
  .map((entry) => `- **${entry.timestamp.toISOString()}** [${entry.author}]: ${entry.action} - ${entry.details}`)
  .join('\n')}

## Affected Services
${incident.affectedServices.map((s) => `- ${s}`).join('\n')}

## Resolution
${incident.timeline.find((t) => t.action === 'incident_resolved')?.details || 'N/A'}
    `;
  }
}
```

### 6.2 Automated Response Actions

```yaml
# automation/incident-automation.yaml

automations:
  - name: auto-scale-on-high-load
    trigger:
      alert: HighCPUUsage
      threshold: 85%
      duration: 5m
    action:
      type: scale_deployment
      deployment: api-gateway
      namespace: mindweave-services
      scale_up_by: 2
      max_replicas: 20
    notification:
      channel: "#platform-alerts"
      message: "Auto-scaled api-gateway due to high CPU"

  - name: auto-restart-failed-pod
    trigger:
      alert: PodCrashLoopBackOff
      max_restarts: 3
    action:
      type: delete_pod
      selector: "app={{ .Labels.app }}"
      namespace: "{{ .Labels.namespace }}"
    notification:
      channel: "#platform-alerts"
      message: "Deleted crash-looping pod: {{ .Labels.pod }}"

  - name: auto-failover-database
    trigger:
      alert: DatabasePrimaryUnreachable
      duration: 2m
    action:
      type: promote_replica
      instance: mindweave-replica
    notification:
      channel: "#incidents"
      message: "Initiated database failover to replica"
      severity: critical

  - name: auto-block-suspicious-ip
    trigger:
      alert: SuspiciousTrafficPattern
      type: rate_limit_exceeded
    action:
      type: waf_block_ip
      duration: 1h
    notification:
      channel: "#security-alerts"
      message: "Blocked suspicious IP: {{ .Labels.source_ip }}"
```

---

## 7. Metrics and KPIs

### 7.1 Incident Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| **MTTA** (Mean Time to Acknowledge) | < 5 min (SEV-1) | Time from alert to acknowledgment |
| **MTTI** (Mean Time to Identify) | < 15 min (SEV-1) | Time from alert to root cause identified |
| **MTTR** (Mean Time to Resolve) | < 1 hour (SEV-1) | Time from alert to resolution |
| **Incident Volume** | < 5/month (SEV-1/2) | Number of significant incidents |
| **Repeat Incident Rate** | < 10% | Same root cause occurring again |
| **Post-Mortem Completion** | 100% | PIR completed within 5 business days |

### 7.2 SLA Compliance

| Severity | Response Time SLA | Resolution Time SLA |
|----------|-------------------|---------------------|
| SEV-1 | 5 minutes | 1 hour |
| SEV-2 | 15 minutes | 4 hours |
| SEV-3 | 1 hour | 24 hours |
| SEV-4 | 4 hours | 72 hours |

---

## Related Documents

| Document | Description |
|----------|-------------|
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Monitoring and alerting |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security controls |
| [DEPLOYMENT-STRATEGY.md](./DEPLOYMENT-STRATEGY.md) | Deployment procedures |
| [DEVOPS-CICD.md](./DEVOPS-CICD.md) | CI/CD pipeline |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Platform Engineering | Initial incident response documentation |
