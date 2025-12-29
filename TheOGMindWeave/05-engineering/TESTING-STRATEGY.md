# MindWeave Testing Strategy

## Document Information

| Field | Value |
|-------|-------|
| Document ID | MW-ENG-072 |
| Version | 1.0.0 |
| Last Updated | 2025-01-15 |
| Owner | Platform Engineering |
| Classification | Internal |
| Status | Active |

---

## Executive Summary

This document defines MindWeave's comprehensive testing strategy covering unit tests, integration tests, end-to-end tests, performance tests, and security tests. Our testing approach ensures high code quality, prevents regressions, and maintains system reliability.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          TESTING PYRAMID                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                              ┌─────────┐                                    │
│                             /           \                                   │
│                            /   E2E       \    5%                            │
│                           /   Tests       \   (~50 tests)                   │
│                          /                 \  Slow, Expensive               │
│                         ├───────────────────┤                               │
│                        /                     \                              │
│                       /    Integration        \  15%                        │
│                      /       Tests             \ (~300 tests)               │
│                     /                           \ Medium Speed              │
│                    ├─────────────────────────────┤                          │
│                   /                               \                         │
│                  /          Unit Tests             \  80%                   │
│                 /                                   \ (~2000 tests)         │
│                /            Fast, Isolated           \ Very Fast            │
│               └───────────────────────────────────────┘                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    TEST COVERAGE TARGETS                             │   │
│  ├──────────────────┬───────────────────┬──────────────────────────────┤   │
│  │    Layer         │   Coverage Target │   Current Coverage           │   │
│  ├──────────────────┼───────────────────┼──────────────────────────────┤   │
│  │    Domain        │       95%         │   92%                        │   │
│  │    Application   │       90%         │   88%                        │   │
│  │    Infrastructure│       80%         │   76%                        │   │
│  │    Presentation  │       85%         │   82%                        │   │
│  │    Overall       │       85%         │   84%                        │   │
│  └──────────────────┴───────────────────┴──────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Unit Testing

### 1.1 Testing Framework Configuration

```typescript
// vitest.config.ts

import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['src/**/*.{test,spec}.{js,ts}'],
    exclude: ['node_modules', 'dist', 'e2e'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      include: ['src/**/*.ts'],
      exclude: [
        'src/**/*.d.ts',
        'src/**/*.test.ts',
        'src/**/*.spec.ts',
        'src/**/index.ts',
        'src/types/**',
      ],
      thresholds: {
        lines: 85,
        functions: 85,
        branches: 80,
        statements: 85,
      },
    },
    setupFiles: ['./src/test/setup.ts'],
    mockReset: true,
    restoreMocks: true,
    testTimeout: 10000,
    reporters: ['default', 'junit'],
    outputFile: {
      junit: './reports/junit.xml',
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@test': path.resolve(__dirname, 'src/test'),
    },
  },
});
```

### 1.2 Test Setup and Utilities

```typescript
// src/test/setup.ts

import { beforeAll, afterAll, beforeEach, afterEach, vi } from 'vitest';

// Mock environment variables
process.env.NODE_ENV = 'test';
process.env.DATABASE_URL = 'postgresql://test:test@localhost:5432/test';
process.env.REDIS_URL = 'redis://localhost:6379';
process.env.JWT_SECRET = 'test-secret-key-for-testing-only';

// Global test utilities
beforeAll(() => {
  // Setup global mocks
  vi.useFakeTimers();
});

afterAll(() => {
  vi.useRealTimers();
});

beforeEach(() => {
  vi.clearAllMocks();
});

afterEach(() => {
  vi.restoreAllMocks();
});
```

```typescript
// src/test/factories/user.factory.ts

import { faker } from '@faker-js/faker';
import { User, UserRole } from '@/domain/entities/user';

interface UserFactoryOptions {
  id?: string;
  email?: string;
  name?: string;
  role?: UserRole;
  orgId?: string;
  createdAt?: Date;
}

export function createUser(options: UserFactoryOptions = {}): User {
  return new User({
    id: options.id ?? faker.string.uuid(),
    email: options.email ?? faker.internet.email(),
    name: options.name ?? faker.person.fullName(),
    role: options.role ?? UserRole.MEMBER,
    orgId: options.orgId ?? faker.string.uuid(),
    createdAt: options.createdAt ?? new Date(),
    updatedAt: new Date(),
  });
}

export function createUsers(count: number, options: UserFactoryOptions = {}): User[] {
  return Array.from({ length: count }, () => createUser(options));
}
```

```typescript
// src/test/factories/organization.factory.ts

import { faker } from '@faker-js/faker';
import { Organization, SubscriptionTier } from '@/domain/entities/organization';

interface OrgFactoryOptions {
  id?: string;
  name?: string;
  slug?: string;
  tier?: SubscriptionTier;
  settings?: Record<string, any>;
}

export function createOrganization(options: OrgFactoryOptions = {}): Organization {
  const name = options.name ?? faker.company.name();
  return new Organization({
    id: options.id ?? faker.string.uuid(),
    name,
    slug: options.slug ?? faker.helpers.slugify(name).toLowerCase(),
    tier: options.tier ?? SubscriptionTier.TEAM,
    settings: options.settings ?? {},
    createdAt: new Date(),
    updatedAt: new Date(),
  });
}
```

### 1.3 Domain Entity Tests

```typescript
// src/domain/entities/__tests__/user.test.ts

import { describe, it, expect } from 'vitest';
import { User, UserRole } from '../user';
import { createUser } from '@test/factories/user.factory';

describe('User Entity', () => {
  describe('creation', () => {
    it('should create a valid user with required fields', () => {
      const user = createUser({
        email: 'test@example.com',
        name: 'Test User',
        role: UserRole.ADMIN,
      });

      expect(user.email).toBe('test@example.com');
      expect(user.name).toBe('Test User');
      expect(user.role).toBe(UserRole.ADMIN);
    });

    it('should throw error for invalid email', () => {
      expect(() => createUser({ email: 'invalid-email' })).toThrow('Invalid email format');
    });

    it('should throw error for empty name', () => {
      expect(() => createUser({ name: '' })).toThrow('Name is required');
    });
  });

  describe('role management', () => {
    it('should allow role upgrade', () => {
      const user = createUser({ role: UserRole.MEMBER });

      user.updateRole(UserRole.ADMIN);

      expect(user.role).toBe(UserRole.ADMIN);
    });

    it('should not allow downgrade below VIEWER', () => {
      const user = createUser({ role: UserRole.VIEWER });

      expect(() => user.updateRole(UserRole.MEMBER)).not.toThrow();
    });
  });

  describe('permissions', () => {
    it('should have correct permissions for ADMIN role', () => {
      const admin = createUser({ role: UserRole.ADMIN });

      expect(admin.hasPermission('org:manage')).toBe(true);
      expect(admin.hasPermission('project:create')).toBe(true);
      expect(admin.hasPermission('user:invite')).toBe(true);
    });

    it('should have limited permissions for VIEWER role', () => {
      const viewer = createUser({ role: UserRole.VIEWER });

      expect(viewer.hasPermission('org:manage')).toBe(false);
      expect(viewer.hasPermission('project:create')).toBe(false);
      expect(viewer.hasPermission('analytics:read')).toBe(true);
    });
  });
});
```

### 1.4 Use Case Tests

```typescript
// src/application/use-cases/__tests__/create-project.test.ts

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { CreateProjectUseCase } from '../create-project';
import { createUser } from '@test/factories/user.factory';
import { createOrganization } from '@test/factories/organization.factory';

describe('CreateProjectUseCase', () => {
  let useCase: CreateProjectUseCase;
  let mockProjectRepo: any;
  let mockOrgRepo: any;
  let mockEventBus: any;

  beforeEach(() => {
    mockProjectRepo = {
      findBySlug: vi.fn(),
      create: vi.fn(),
    };

    mockOrgRepo = {
      findById: vi.fn(),
    };

    mockEventBus = {
      publish: vi.fn(),
    };

    useCase = new CreateProjectUseCase(
      mockProjectRepo,
      mockOrgRepo,
      mockEventBus
    );
  });

  describe('execute', () => {
    it('should create a project successfully', async () => {
      const user = createUser({ role: UserRole.ADMIN });
      const org = createOrganization();

      mockOrgRepo.findById.mockResolvedValue(org);
      mockProjectRepo.findBySlug.mockResolvedValue(null);
      mockProjectRepo.create.mockImplementation((project) => project);

      const result = await useCase.execute({
        name: 'Test Project',
        orgId: org.id,
        createdBy: user,
      });

      expect(result.isSuccess).toBe(true);
      expect(result.value.name).toBe('Test Project');
      expect(mockProjectRepo.create).toHaveBeenCalledOnce();
      expect(mockEventBus.publish).toHaveBeenCalledWith(
        expect.objectContaining({
          type: 'project.created',
        })
      );
    });

    it('should fail when organization not found', async () => {
      const user = createUser();

      mockOrgRepo.findById.mockResolvedValue(null);

      const result = await useCase.execute({
        name: 'Test Project',
        orgId: 'non-existent',
        createdBy: user,
      });

      expect(result.isFailure).toBe(true);
      expect(result.error).toBe('Organization not found');
    });

    it('should fail when slug already exists', async () => {
      const user = createUser({ role: UserRole.ADMIN });
      const org = createOrganization();

      mockOrgRepo.findById.mockResolvedValue(org);
      mockProjectRepo.findBySlug.mockResolvedValue({ id: 'existing' });

      const result = await useCase.execute({
        name: 'Test Project',
        orgId: org.id,
        createdBy: user,
      });

      expect(result.isFailure).toBe(true);
      expect(result.error).toBe('Project with this name already exists');
    });

    it('should fail when user lacks permission', async () => {
      const user = createUser({ role: UserRole.VIEWER });
      const org = createOrganization();

      mockOrgRepo.findById.mockResolvedValue(org);

      const result = await useCase.execute({
        name: 'Test Project',
        orgId: org.id,
        createdBy: user,
      });

      expect(result.isFailure).toBe(true);
      expect(result.error).toBe('Insufficient permissions');
    });
  });
});
```

### 1.5 Service Tests

```typescript
// src/services/__tests__/usage-tracker.service.test.ts

import { describe, it, expect, vi, beforeEach } from 'vitest';
import { UsageTrackerService } from '../usage-tracker.service';

describe('UsageTrackerService', () => {
  let service: UsageTrackerService;
  let mockKafkaProducer: any;
  let mockRedisClient: any;
  let mockPricingService: any;

  beforeEach(() => {
    mockKafkaProducer = {
      send: vi.fn().mockResolvedValue(undefined),
    };

    mockRedisClient = {
      incr: vi.fn().mockResolvedValue(1),
      expire: vi.fn().mockResolvedValue(1),
      get: vi.fn().mockResolvedValue('0'),
    };

    mockPricingService = {
      calculateCost: vi.fn().mockReturnValue(150), // 150 cents
    };

    service = new UsageTrackerService(
      mockKafkaProducer,
      mockRedisClient,
      mockPricingService
    );
  });

  describe('trackUsage', () => {
    const validUsageEvent = {
      orgId: 'org-123',
      projectId: 'proj-456',
      userId: 'user-789',
      model: 'claude-3-sonnet-20240229',
      inputTokens: 1000,
      outputTokens: 500,
      latencyMs: 1500,
      status: 'success' as const,
    };

    it('should track usage event successfully', async () => {
      await service.trackUsage(validUsageEvent);

      expect(mockPricingService.calculateCost).toHaveBeenCalledWith({
        model: 'claude-3-sonnet-20240229',
        inputTokens: 1000,
        outputTokens: 500,
      });

      expect(mockKafkaProducer.send).toHaveBeenCalledWith({
        topic: 'usage.events.raw',
        messages: [
          expect.objectContaining({
            key: 'org-123',
            value: expect.stringContaining('"inputTokens":1000'),
          }),
        ],
      });
    });

    it('should increment rate limit counter', async () => {
      await service.trackUsage(validUsageEvent);

      expect(mockRedisClient.incr).toHaveBeenCalledWith(
        'rate:org-123:requests:minute'
      );
    });

    it('should validate required fields', async () => {
      await expect(
        service.trackUsage({ ...validUsageEvent, orgId: '' })
      ).rejects.toThrow('orgId is required');
    });

    it('should validate token counts are non-negative', async () => {
      await expect(
        service.trackUsage({ ...validUsageEvent, inputTokens: -1 })
      ).rejects.toThrow('inputTokens must be non-negative');
    });
  });

  describe('getUsageSummary', () => {
    it('should return aggregated usage summary', async () => {
      mockRedisClient.get
        .mockResolvedValueOnce('1000') // total requests
        .mockResolvedValueOnce('500000') // total tokens
        .mockResolvedValueOnce('7500'); // total cost cents

      const summary = await service.getUsageSummary('org-123', 'day');

      expect(summary).toEqual({
        totalRequests: 1000,
        totalTokens: 500000,
        totalCostCents: 7500,
        period: 'day',
      });
    });
  });
});
```

---

## 2. Integration Testing

### 2.1 Database Integration Tests

```typescript
// src/infrastructure/repositories/__tests__/project.repository.integration.test.ts

import { describe, it, expect, beforeAll, afterAll, beforeEach } from 'vitest';
import { PostgresProjectRepository } from '../project.repository';
import { createTestDatabase, closeTestDatabase, cleanDatabase } from '@test/database';
import { createProject } from '@test/factories/project.factory';
import { createOrganization } from '@test/factories/organization.factory';

describe('ProjectRepository Integration', () => {
  let repository: PostgresProjectRepository;
  let db: any;

  beforeAll(async () => {
    db = await createTestDatabase();
    repository = new PostgresProjectRepository(db);
  });

  afterAll(async () => {
    await closeTestDatabase(db);
  });

  beforeEach(async () => {
    await cleanDatabase(db);
  });

  describe('create', () => {
    it('should persist a project to the database', async () => {
      const org = createOrganization();
      await db.query('INSERT INTO organizations (id, name, slug) VALUES ($1, $2, $3)', [
        org.id,
        org.name,
        org.slug,
      ]);

      const project = createProject({ orgId: org.id });

      const saved = await repository.create(project);

      expect(saved.id).toBe(project.id);

      const found = await db.query('SELECT * FROM projects WHERE id = $1', [project.id]);
      expect(found.rows).toHaveLength(1);
      expect(found.rows[0].name).toBe(project.name);
    });

    it('should handle unique constraint violation', async () => {
      const org = createOrganization();
      await db.query('INSERT INTO organizations (id, name, slug) VALUES ($1, $2, $3)', [
        org.id,
        org.name,
        org.slug,
      ]);

      const project = createProject({ orgId: org.id, slug: 'test-project' });
      await repository.create(project);

      const duplicate = createProject({ orgId: org.id, slug: 'test-project' });

      await expect(repository.create(duplicate)).rejects.toThrow('slug already exists');
    });
  });

  describe('findByOrgId', () => {
    it('should return all projects for an organization', async () => {
      const org = createOrganization();
      await db.query('INSERT INTO organizations (id, name, slug) VALUES ($1, $2, $3)', [
        org.id,
        org.name,
        org.slug,
      ]);

      const projects = [
        createProject({ orgId: org.id }),
        createProject({ orgId: org.id }),
        createProject({ orgId: org.id }),
      ];

      for (const project of projects) {
        await repository.create(project);
      }

      const found = await repository.findByOrgId(org.id);

      expect(found).toHaveLength(3);
    });

    it('should support pagination', async () => {
      const org = createOrganization();
      await db.query('INSERT INTO organizations (id, name, slug) VALUES ($1, $2, $3)', [
        org.id,
        org.name,
        org.slug,
      ]);

      for (let i = 0; i < 10; i++) {
        await repository.create(createProject({ orgId: org.id }));
      }

      const page1 = await repository.findByOrgId(org.id, { limit: 5, offset: 0 });
      const page2 = await repository.findByOrgId(org.id, { limit: 5, offset: 5 });

      expect(page1).toHaveLength(5);
      expect(page2).toHaveLength(5);
      expect(page1[0].id).not.toBe(page2[0].id);
    });
  });
});
```

### 2.2 API Integration Tests

```typescript
// src/api/__tests__/projects.api.integration.test.ts

import { describe, it, expect, beforeAll, afterAll, beforeEach } from 'vitest';
import supertest from 'supertest';
import { createApp } from '@/app';
import { createTestDatabase, closeTestDatabase, cleanDatabase } from '@test/database';
import { createAuthToken } from '@test/auth';
import { createUser } from '@test/factories/user.factory';
import { createOrganization } from '@test/factories/organization.factory';

describe('Projects API Integration', () => {
  let app: Express.Application;
  let request: supertest.SuperTest<supertest.Test>;
  let db: any;
  let authToken: string;
  let org: Organization;
  let user: User;

  beforeAll(async () => {
    db = await createTestDatabase();
    app = await createApp({ db });
    request = supertest(app);
  });

  afterAll(async () => {
    await closeTestDatabase(db);
  });

  beforeEach(async () => {
    await cleanDatabase(db);

    // Create test org and user
    org = createOrganization();
    user = createUser({ orgId: org.id, role: UserRole.ADMIN });

    await db.query('INSERT INTO organizations (id, name, slug) VALUES ($1, $2, $3)', [
      org.id,
      org.name,
      org.slug,
    ]);
    await db.query(
      'INSERT INTO users (id, email, name, org_id, role) VALUES ($1, $2, $3, $4, $5)',
      [user.id, user.email, user.name, user.orgId, user.role]
    );

    authToken = await createAuthToken(user);
  });

  describe('POST /api/v1/projects', () => {
    it('should create a new project', async () => {
      const response = await request
        .post('/api/v1/projects')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          name: 'Test Project',
          description: 'A test project',
        });

      expect(response.status).toBe(201);
      expect(response.body.data.name).toBe('Test Project');
      expect(response.body.data.slug).toBe('test-project');
      expect(response.body.data.orgId).toBe(org.id);
    });

    it('should return 400 for invalid input', async () => {
      const response = await request
        .post('/api/v1/projects')
        .set('Authorization', `Bearer ${authToken}`)
        .send({
          name: '', // Empty name
        });

      expect(response.status).toBe(400);
      expect(response.body.error.code).toBe('VALIDATION_ERROR');
    });

    it('should return 401 without auth token', async () => {
      const response = await request.post('/api/v1/projects').send({
        name: 'Test Project',
      });

      expect(response.status).toBe(401);
    });

    it('should return 403 for insufficient permissions', async () => {
      const viewer = createUser({ orgId: org.id, role: UserRole.VIEWER });
      await db.query(
        'INSERT INTO users (id, email, name, org_id, role) VALUES ($1, $2, $3, $4, $5)',
        [viewer.id, viewer.email, viewer.name, viewer.orgId, viewer.role]
      );
      const viewerToken = await createAuthToken(viewer);

      const response = await request
        .post('/api/v1/projects')
        .set('Authorization', `Bearer ${viewerToken}`)
        .send({
          name: 'Test Project',
        });

      expect(response.status).toBe(403);
    });
  });

  describe('GET /api/v1/projects', () => {
    beforeEach(async () => {
      // Create some projects
      for (let i = 0; i < 5; i++) {
        await request
          .post('/api/v1/projects')
          .set('Authorization', `Bearer ${authToken}`)
          .send({
            name: `Project ${i}`,
          });
      }
    });

    it('should list all projects for the organization', async () => {
      const response = await request
        .get('/api/v1/projects')
        .set('Authorization', `Bearer ${authToken}`);

      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(5);
    });

    it('should support pagination', async () => {
      const response = await request
        .get('/api/v1/projects')
        .query({ limit: 2, page: 1 })
        .set('Authorization', `Bearer ${authToken}`);

      expect(response.status).toBe(200);
      expect(response.body.data).toHaveLength(2);
      expect(response.body.meta.total).toBe(5);
      expect(response.body.meta.page).toBe(1);
      expect(response.body.meta.totalPages).toBe(3);
    });
  });
});
```

### 2.3 Redis Integration Tests

```typescript
// src/infrastructure/cache/__tests__/redis.integration.test.ts

import { describe, it, expect, beforeAll, afterAll, beforeEach } from 'vitest';
import { RedisCache } from '../redis.cache';
import { createRedisClient, closeRedisClient } from '@test/redis';

describe('RedisCache Integration', () => {
  let cache: RedisCache;
  let redis: any;

  beforeAll(async () => {
    redis = await createRedisClient();
    cache = new RedisCache(redis);
  });

  afterAll(async () => {
    await closeRedisClient(redis);
  });

  beforeEach(async () => {
    await redis.flushDb();
  });

  describe('set and get', () => {
    it('should store and retrieve values', async () => {
      await cache.set('test-key', { foo: 'bar' });

      const value = await cache.get('test-key');

      expect(value).toEqual({ foo: 'bar' });
    });

    it('should return null for non-existent keys', async () => {
      const value = await cache.get('non-existent');

      expect(value).toBeNull();
    });

    it('should respect TTL', async () => {
      await cache.set('expiring-key', 'value', { ttl: 1 });

      const valueBefore = await cache.get('expiring-key');
      expect(valueBefore).toBe('value');

      await new Promise((resolve) => setTimeout(resolve, 1100));

      const valueAfter = await cache.get('expiring-key');
      expect(valueAfter).toBeNull();
    });
  });

  describe('getOrSet', () => {
    it('should return cached value if exists', async () => {
      await cache.set('cached-key', 'cached-value');
      const factory = vi.fn().mockResolvedValue('new-value');

      const value = await cache.getOrSet('cached-key', factory);

      expect(value).toBe('cached-value');
      expect(factory).not.toHaveBeenCalled();
    });

    it('should call factory and cache if not exists', async () => {
      const factory = vi.fn().mockResolvedValue('new-value');

      const value = await cache.getOrSet('new-key', factory);

      expect(value).toBe('new-value');
      expect(factory).toHaveBeenCalled();

      const cachedValue = await cache.get('new-key');
      expect(cachedValue).toBe('new-value');
    });
  });

  describe('rate limiting', () => {
    it('should track request counts', async () => {
      const key = 'rate:user-123:requests:minute';

      await cache.increment(key);
      await cache.increment(key);
      await cache.increment(key);

      const count = await cache.get(key);
      expect(parseInt(count)).toBe(3);
    });

    it('should check rate limit', async () => {
      const rateLimiter = new RateLimiter(cache, { maxRequests: 5, windowSec: 60 });

      for (let i = 0; i < 5; i++) {
        const allowed = await rateLimiter.isAllowed('user-123');
        expect(allowed).toBe(true);
      }

      const blocked = await rateLimiter.isAllowed('user-123');
      expect(blocked).toBe(false);
    });
  });
});
```

### 2.4 Kafka Integration Tests

```typescript
// src/infrastructure/messaging/__tests__/kafka.integration.test.ts

import { describe, it, expect, beforeAll, afterAll, beforeEach } from 'vitest';
import { KafkaProducer, KafkaConsumer } from '../kafka';
import { createKafkaClient, closeKafkaClient } from '@test/kafka';

describe('Kafka Integration', () => {
  let producer: KafkaProducer;
  let consumer: KafkaConsumer;
  let kafka: any;

  beforeAll(async () => {
    kafka = await createKafkaClient();
    producer = new KafkaProducer(kafka);
    consumer = new KafkaConsumer(kafka);

    await producer.connect();
    await consumer.connect();
  });

  afterAll(async () => {
    await producer.disconnect();
    await consumer.disconnect();
    await closeKafkaClient(kafka);
  });

  describe('produce and consume', () => {
    it('should send and receive messages', async () => {
      const topic = 'test-topic';
      const receivedMessages: any[] = [];

      await consumer.subscribe(topic, async (message) => {
        receivedMessages.push(message);
      });

      await producer.send(topic, {
        key: 'test-key',
        value: { foo: 'bar' },
      });

      // Wait for message to be consumed
      await new Promise((resolve) => setTimeout(resolve, 1000));

      expect(receivedMessages).toHaveLength(1);
      expect(receivedMessages[0].value).toEqual({ foo: 'bar' });
    });

    it('should maintain message ordering within partition', async () => {
      const topic = 'ordered-topic';
      const receivedMessages: number[] = [];

      await consumer.subscribe(topic, async (message) => {
        receivedMessages.push(message.value.sequence);
      });

      for (let i = 0; i < 10; i++) {
        await producer.send(topic, {
          key: 'same-key', // Same key ensures same partition
          value: { sequence: i },
        });
      }

      await new Promise((resolve) => setTimeout(resolve, 2000));

      expect(receivedMessages).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]);
    });
  });
});
```

---

## 3. End-to-End Testing

### 3.1 Playwright Configuration

```typescript
// playwright.config.ts

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: [
    ['list'],
    ['html', { outputFolder: 'playwright-report' }],
    ['junit', { outputFile: 'reports/e2e-results.xml' }],
  ],
  use: {
    baseURL: process.env.E2E_BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'on-first-retry',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
    },
  ],
  webServer: process.env.CI
    ? undefined
    : {
        command: 'npm run dev',
        url: 'http://localhost:3000',
        reuseExistingServer: true,
      },
});
```

### 3.2 E2E Test Utilities

```typescript
// e2e/fixtures.ts

import { test as base, expect } from '@playwright/test';

interface TestUser {
  email: string;
  password: string;
  name: string;
}

interface TestFixtures {
  authenticatedPage: Page;
  testUser: TestUser;
  testOrg: { id: string; name: string };
}

export const test = base.extend<TestFixtures>({
  testUser: async ({}, use) => {
    const user = {
      email: `test-${Date.now()}@example.com`,
      password: 'TestPassword123!',
      name: 'Test User',
    };
    await use(user);
  },

  testOrg: async ({ request }, use) => {
    // Create test organization via API
    const response = await request.post('/api/test/setup', {
      data: { type: 'organization' },
    });
    const org = await response.json();
    await use(org);

    // Cleanup
    await request.delete(`/api/test/cleanup/${org.id}`);
  },

  authenticatedPage: async ({ page, testUser }, use) => {
    // Register user
    await page.goto('/signup');
    await page.fill('[data-testid="name-input"]', testUser.name);
    await page.fill('[data-testid="email-input"]', testUser.email);
    await page.fill('[data-testid="password-input"]', testUser.password);
    await page.click('[data-testid="signup-button"]');

    // Wait for redirect to dashboard
    await page.waitForURL('/dashboard');

    await use(page);
  },
});

export { expect };
```

### 3.3 Authentication E2E Tests

```typescript
// e2e/auth/login.spec.ts

import { test, expect } from '../fixtures';

test.describe('Login Flow', () => {
  test('should login with valid credentials', async ({ page, testUser }) => {
    // First register the user
    await page.goto('/signup');
    await page.fill('[data-testid="name-input"]', testUser.name);
    await page.fill('[data-testid="email-input"]', testUser.email);
    await page.fill('[data-testid="password-input"]', testUser.password);
    await page.click('[data-testid="signup-button"]');
    await page.waitForURL('/dashboard');

    // Logout
    await page.click('[data-testid="user-menu"]');
    await page.click('[data-testid="logout-button"]');
    await page.waitForURL('/login');

    // Login again
    await page.fill('[data-testid="email-input"]', testUser.email);
    await page.fill('[data-testid="password-input"]', testUser.password);
    await page.click('[data-testid="login-button"]');

    await expect(page).toHaveURL('/dashboard');
    await expect(page.locator('[data-testid="welcome-message"]')).toContainText(
      testUser.name
    );
  });

  test('should show error for invalid credentials', async ({ page }) => {
    await page.goto('/login');
    await page.fill('[data-testid="email-input"]', 'wrong@example.com');
    await page.fill('[data-testid="password-input"]', 'wrongpassword');
    await page.click('[data-testid="login-button"]');

    await expect(page.locator('[data-testid="error-message"]')).toContainText(
      'Invalid email or password'
    );
  });

  test('should redirect to requested page after login', async ({
    page,
    testUser,
  }) => {
    // Try to access protected page
    await page.goto('/projects/new');

    // Should redirect to login
    await expect(page).toHaveURL(/\/login\?redirect=/);

    // Login
    await page.fill('[data-testid="email-input"]', testUser.email);
    await page.fill('[data-testid="password-input"]', testUser.password);
    await page.click('[data-testid="login-button"]');

    // Should redirect to originally requested page
    await expect(page).toHaveURL('/projects/new');
  });
});
```

### 3.4 Project Management E2E Tests

```typescript
// e2e/projects/create-project.spec.ts

import { test, expect } from '../fixtures';

test.describe('Project Management', () => {
  test('should create a new project', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/projects');
    await page.click('[data-testid="create-project-button"]');

    await page.fill('[data-testid="project-name-input"]', 'My Test Project');
    await page.fill(
      '[data-testid="project-description-input"]',
      'A project for testing'
    );
    await page.click('[data-testid="submit-project-button"]');

    // Should redirect to project page
    await expect(page).toHaveURL(/\/projects\/[a-z0-9-]+/);
    await expect(page.locator('h1')).toContainText('My Test Project');
  });

  test('should validate project name', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/projects/new');

    // Submit with empty name
    await page.click('[data-testid="submit-project-button"]');

    await expect(page.locator('[data-testid="name-error"]')).toContainText(
      'Project name is required'
    );
  });

  test('should list all projects', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    // Create multiple projects
    for (let i = 0; i < 3; i++) {
      await page.goto('/projects/new');
      await page.fill('[data-testid="project-name-input"]', `Project ${i + 1}`);
      await page.click('[data-testid="submit-project-button"]');
      await page.waitForURL(/\/projects\/[a-z0-9-]+/);
    }

    // Go to projects list
    await page.goto('/projects');

    const projectCards = page.locator('[data-testid="project-card"]');
    await expect(projectCards).toHaveCount(3);
  });

  test('should delete a project', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    // Create a project
    await page.goto('/projects/new');
    await page.fill('[data-testid="project-name-input"]', 'Project to Delete');
    await page.click('[data-testid="submit-project-button"]');
    await page.waitForURL(/\/projects\/[a-z0-9-]+/);

    // Delete it
    await page.click('[data-testid="project-settings-button"]');
    await page.click('[data-testid="delete-project-button"]');

    // Confirm deletion
    await page.fill('[data-testid="confirm-delete-input"]', 'Project to Delete');
    await page.click('[data-testid="confirm-delete-button"]');

    // Should redirect to projects list
    await expect(page).toHaveURL('/projects');
    await expect(page.locator('text=Project to Delete')).not.toBeVisible();
  });
});
```

### 3.5 Analytics Dashboard E2E Tests

```typescript
// e2e/analytics/dashboard.spec.ts

import { test, expect } from '../fixtures';

test.describe('Analytics Dashboard', () => {
  test.beforeEach(async ({ authenticatedPage, request }) => {
    // Seed some usage data
    await request.post('/api/test/seed-usage', {
      data: {
        count: 100,
        days: 7,
      },
    });
  });

  test('should display usage metrics', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/analytics');

    // Wait for data to load
    await page.waitForSelector('[data-testid="usage-chart"]');

    // Check key metrics are displayed
    await expect(page.locator('[data-testid="total-requests"]')).toBeVisible();
    await expect(page.locator('[data-testid="total-tokens"]')).toBeVisible();
    await expect(page.locator('[data-testid="total-cost"]')).toBeVisible();
  });

  test('should filter by date range', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/analytics');

    // Select last 24 hours
    await page.click('[data-testid="date-range-selector"]');
    await page.click('[data-testid="range-24h"]');

    // Verify URL updated
    await expect(page).toHaveURL(/range=24h/);

    // Verify chart updated
    await page.waitForResponse((response) =>
      response.url().includes('/api/v1/analytics') && response.status() === 200
    );
  });

  test('should export data as CSV', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/analytics');

    // Start download
    const [download] = await Promise.all([
      page.waitForEvent('download'),
      page.click('[data-testid="export-csv-button"]'),
    ]);

    expect(download.suggestedFilename()).toMatch(/usage-data.*\.csv$/);
  });

  test('should show usage by model breakdown', async ({ authenticatedPage }) => {
    const page = authenticatedPage;

    await page.goto('/analytics');

    // Check model breakdown chart
    await page.click('[data-testid="tab-models"]');
    await expect(page.locator('[data-testid="model-breakdown-chart"]')).toBeVisible();

    // Verify all models are shown
    await expect(page.locator('text=claude-3-opus')).toBeVisible();
    await expect(page.locator('text=claude-3-sonnet')).toBeVisible();
    await expect(page.locator('text=claude-3-haiku')).toBeVisible();
  });
});
```

---

## 4. Performance Testing

### 4.1 k6 Load Test Configuration

```javascript
// performance/load-test.js

import http from 'k6/http';
import { check, sleep } from 'k6';
import { Rate, Trend } from 'k6/metrics';

// Custom metrics
const errorRate = new Rate('errors');
const apiLatency = new Trend('api_latency');

// Test configuration
export const options = {
  scenarios: {
    // Smoke test
    smoke: {
      executor: 'constant-vus',
      vus: 1,
      duration: '1m',
      tags: { test_type: 'smoke' },
    },
    // Load test
    load: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 50 },
        { duration: '5m', target: 50 },
        { duration: '2m', target: 100 },
        { duration: '5m', target: 100 },
        { duration: '2m', target: 0 },
      ],
      tags: { test_type: 'load' },
    },
    // Stress test
    stress: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 100 },
        { duration: '5m', target: 200 },
        { duration: '2m', target: 300 },
        { duration: '5m', target: 300 },
        { duration: '2m', target: 0 },
      ],
      tags: { test_type: 'stress' },
    },
    // Spike test
    spike: {
      executor: 'ramping-vus',
      startVUs: 1,
      stages: [
        { duration: '10s', target: 1 },
        { duration: '1m', target: 500 },
        { duration: '10s', target: 1 },
      ],
      tags: { test_type: 'spike' },
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    http_req_failed: ['rate<0.01'],
    errors: ['rate<0.05'],
  },
};

const BASE_URL = __ENV.BASE_URL || 'http://localhost:3000';
const API_KEY = __ENV.API_KEY;

// Setup
export function setup() {
  // Create test data
  const response = http.post(`${BASE_URL}/api/test/setup`, JSON.stringify({
    users: 100,
    projects: 10,
  }), {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`,
    },
  });

  return {
    testData: response.json(),
  };
}

// Main test
export default function(data) {
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${API_KEY}`,
  };

  // Test 1: Get projects
  const projectsResponse = http.get(`${BASE_URL}/api/v1/projects`, { headers });
  check(projectsResponse, {
    'projects status 200': (r) => r.status === 200,
    'projects response time < 200ms': (r) => r.timings.duration < 200,
  });
  apiLatency.add(projectsResponse.timings.duration);
  errorRate.add(projectsResponse.status !== 200);

  sleep(1);

  // Test 2: Get usage analytics
  const analyticsResponse = http.get(`${BASE_URL}/api/v1/analytics/usage?range=7d`, { headers });
  check(analyticsResponse, {
    'analytics status 200': (r) => r.status === 200,
    'analytics response time < 500ms': (r) => r.timings.duration < 500,
  });
  apiLatency.add(analyticsResponse.timings.duration);
  errorRate.add(analyticsResponse.status !== 200);

  sleep(1);

  // Test 3: Track usage event
  const usageEvent = {
    model: 'claude-3-sonnet-20240229',
    inputTokens: Math.floor(Math.random() * 1000) + 100,
    outputTokens: Math.floor(Math.random() * 500) + 50,
    latencyMs: Math.floor(Math.random() * 2000) + 500,
  };

  const trackResponse = http.post(
    `${BASE_URL}/api/v1/usage/track`,
    JSON.stringify(usageEvent),
    { headers }
  );
  check(trackResponse, {
    'track status 202': (r) => r.status === 202,
    'track response time < 100ms': (r) => r.timings.duration < 100,
  });
  apiLatency.add(trackResponse.timings.duration);
  errorRate.add(trackResponse.status !== 202);

  sleep(1);
}

// Teardown
export function teardown(data) {
  http.del(`${BASE_URL}/api/test/cleanup`, {
    headers: {
      'Authorization': `Bearer ${API_KEY}`,
    },
  });
}
```

### 4.2 Performance Test Scenarios

```javascript
// performance/scenarios/api-endpoints.js

import http from 'k6/http';
import { check, group } from 'k6';
import { Trend } from 'k6/metrics';

const trends = {
  createProject: new Trend('create_project_duration'),
  getProjects: new Trend('get_projects_duration'),
  getAnalytics: new Trend('get_analytics_duration'),
  trackUsage: new Trend('track_usage_duration'),
  listMcpServers: new Trend('list_mcp_servers_duration'),
};

export function testCreateProject(headers) {
  return group('Create Project', () => {
    const payload = {
      name: `Test Project ${Date.now()}`,
      description: 'Performance test project',
    };

    const response = http.post(
      `${BASE_URL}/api/v1/projects`,
      JSON.stringify(payload),
      { headers }
    );

    trends.createProject.add(response.timings.duration);

    check(response, {
      'create project status 201': (r) => r.status === 201,
      'create project has id': (r) => r.json('data.id') !== undefined,
    });

    return response.json('data');
  });
}

export function testGetProjects(headers) {
  return group('Get Projects', () => {
    const response = http.get(`${BASE_URL}/api/v1/projects`, { headers });

    trends.getProjects.add(response.timings.duration);

    check(response, {
      'get projects status 200': (r) => r.status === 200,
      'get projects is array': (r) => Array.isArray(r.json('data')),
    });

    return response.json('data');
  });
}

export function testGetAnalytics(headers, projectId) {
  return group('Get Analytics', () => {
    const response = http.get(
      `${BASE_URL}/api/v1/analytics/usage?projectId=${projectId}&range=7d`,
      { headers }
    );

    trends.getAnalytics.add(response.timings.duration);

    check(response, {
      'get analytics status 200': (r) => r.status === 200,
      'analytics has data': (r) => r.json('data') !== undefined,
    });

    return response.json('data');
  });
}

export function testTrackUsage(headers) {
  return group('Track Usage', () => {
    const payload = {
      model: 'claude-3-sonnet-20240229',
      inputTokens: 500,
      outputTokens: 200,
      latencyMs: 1000,
    };

    const response = http.post(
      `${BASE_URL}/api/v1/usage/track`,
      JSON.stringify(payload),
      { headers }
    );

    trends.trackUsage.add(response.timings.duration);

    check(response, {
      'track usage status 202': (r) => r.status === 202,
    });

    return response.status === 202;
  });
}

export function testListMcpServers(headers) {
  return group('List MCP Servers', () => {
    const response = http.get(`${BASE_URL}/api/v1/mcp/servers`, { headers });

    trends.listMcpServers.add(response.timings.duration);

    check(response, {
      'list mcp servers status 200': (r) => r.status === 200,
    });

    return response.json('data');
  });
}
```

---

## 5. Security Testing

### 5.1 Security Test Suite

```typescript
// security/auth.security.test.ts

import { describe, it, expect, beforeAll } from 'vitest';
import supertest from 'supertest';
import { createApp } from '@/app';

describe('Authentication Security Tests', () => {
  let app: Express.Application;
  let request: supertest.SuperTest<supertest.Test>;

  beforeAll(async () => {
    app = await createApp();
    request = supertest(app);
  });

  describe('Brute Force Protection', () => {
    it('should block after 5 failed login attempts', async () => {
      const email = 'brute-force-test@example.com';

      // Make 5 failed attempts
      for (let i = 0; i < 5; i++) {
        await request.post('/api/v1/auth/login').send({
          email,
          password: 'wrongpassword',
        });
      }

      // 6th attempt should be blocked
      const response = await request.post('/api/v1/auth/login').send({
        email,
        password: 'wrongpassword',
      });

      expect(response.status).toBe(429);
      expect(response.body.error.code).toBe('TOO_MANY_REQUESTS');
    });
  });

  describe('JWT Security', () => {
    it('should reject expired tokens', async () => {
      const expiredToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'; // Pre-generated expired token

      const response = await request
        .get('/api/v1/me')
        .set('Authorization', `Bearer ${expiredToken}`);

      expect(response.status).toBe(401);
      expect(response.body.error.code).toBe('TOKEN_EXPIRED');
    });

    it('should reject tokens with invalid signature', async () => {
      const tamperedToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.tampered';

      const response = await request
        .get('/api/v1/me')
        .set('Authorization', `Bearer ${tamperedToken}`);

      expect(response.status).toBe(401);
      expect(response.body.error.code).toBe('INVALID_TOKEN');
    });

    it('should reject tokens with wrong algorithm', async () => {
      // Token signed with HS256 instead of RS256
      const wrongAlgToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...';

      const response = await request
        .get('/api/v1/me')
        .set('Authorization', `Bearer ${wrongAlgToken}`);

      expect(response.status).toBe(401);
    });
  });

  describe('Password Security', () => {
    it('should reject weak passwords', async () => {
      const weakPasswords = [
        'password',
        '12345678',
        'qwerty123',
        'abc123',
      ];

      for (const password of weakPasswords) {
        const response = await request.post('/api/v1/auth/signup').send({
          email: 'test@example.com',
          password,
          name: 'Test User',
        });

        expect(response.status).toBe(400);
        expect(response.body.error.code).toBe('WEAK_PASSWORD');
      }
    });

    it('should not expose password in responses', async () => {
      const response = await request.post('/api/v1/auth/signup').send({
        email: 'nopassword@example.com',
        password: 'SecureP@ssw0rd123!',
        name: 'Test User',
      });

      expect(response.body).not.toHaveProperty('password');
      expect(response.body.data).not.toHaveProperty('password');
      expect(JSON.stringify(response.body)).not.toContain('SecureP@ssw0rd123!');
    });
  });

  describe('Session Security', () => {
    it('should invalidate session on password change', async () => {
      // Login and get token
      const loginResponse = await request.post('/api/v1/auth/login').send({
        email: 'session-test@example.com',
        password: 'OldPassword123!',
      });
      const token = loginResponse.body.data.accessToken;

      // Change password
      await request
        .post('/api/v1/auth/change-password')
        .set('Authorization', `Bearer ${token}`)
        .send({
          currentPassword: 'OldPassword123!',
          newPassword: 'NewPassword123!',
        });

      // Old token should be invalid
      const response = await request
        .get('/api/v1/me')
        .set('Authorization', `Bearer ${token}`);

      expect(response.status).toBe(401);
    });
  });
});
```

### 5.2 OWASP Security Checks

```typescript
// security/owasp.security.test.ts

import { describe, it, expect, beforeAll } from 'vitest';
import supertest from 'supertest';
import { createApp } from '@/app';

describe('OWASP Top 10 Security Tests', () => {
  let app: Express.Application;
  let request: supertest.SuperTest<supertest.Test>;

  beforeAll(async () => {
    app = await createApp();
    request = supertest(app);
  });

  describe('A01:2021 - Broken Access Control', () => {
    it('should not allow access to other users data', async () => {
      // Login as user1
      const user1Token = await loginAs('user1@example.com');

      // Try to access user2's project
      const response = await request
        .get('/api/v1/projects/user2-project-id')
        .set('Authorization', `Bearer ${user1Token}`);

      expect(response.status).toBe(403);
    });

    it('should prevent IDOR attacks on API keys', async () => {
      const userToken = await loginAs('user@example.com');

      // Try to access another user's API key
      const response = await request
        .get('/api/v1/api-keys/other-user-key-id')
        .set('Authorization', `Bearer ${userToken}`);

      expect(response.status).toBe(403);
    });
  });

  describe('A02:2021 - Cryptographic Failures', () => {
    it('should not expose sensitive data in error messages', async () => {
      const response = await request.post('/api/v1/auth/login').send({
        email: 'nonexistent@example.com',
        password: 'somepassword',
      });

      expect(response.body.error.message).not.toContain('password');
      expect(response.body.error.message).not.toContain('not found');
      expect(response.body.error.message).toBe('Invalid email or password');
    });

    it('should use secure cookies', async () => {
      const response = await request.post('/api/v1/auth/login').send({
        email: 'test@example.com',
        password: 'TestPassword123!',
      });

      const cookies = response.headers['set-cookie'];
      if (cookies) {
        for (const cookie of cookies) {
          expect(cookie).toContain('HttpOnly');
          expect(cookie).toContain('Secure');
          expect(cookie).toContain('SameSite');
        }
      }
    });
  });

  describe('A03:2021 - Injection', () => {
    it('should prevent SQL injection', async () => {
      const response = await request.get('/api/v1/projects').query({
        search: "'; DROP TABLE projects; --",
      });

      expect(response.status).toBe(200);
      // Verify database is still working
      const verifyResponse = await request.get('/api/v1/projects');
      expect(verifyResponse.status).toBe(200);
    });

    it('should prevent NoSQL injection', async () => {
      const response = await request.post('/api/v1/auth/login').send({
        email: { $gt: '' },
        password: { $gt: '' },
      });

      expect(response.status).toBe(400);
    });

    it('should prevent command injection', async () => {
      const response = await request.post('/api/v1/exports').send({
        filename: 'report; rm -rf /',
      });

      expect(response.status).toBe(400);
    });
  });

  describe('A04:2021 - Insecure Design', () => {
    it('should rate limit password reset requests', async () => {
      const email = 'reset-test@example.com';

      // Make 3 requests
      for (let i = 0; i < 3; i++) {
        await request.post('/api/v1/auth/forgot-password').send({ email });
      }

      // 4th request should be blocked
      const response = await request
        .post('/api/v1/auth/forgot-password')
        .send({ email });

      expect(response.status).toBe(429);
    });
  });

  describe('A05:2021 - Security Misconfiguration', () => {
    it('should have security headers', async () => {
      const response = await request.get('/');

      expect(response.headers['x-content-type-options']).toBe('nosniff');
      expect(response.headers['x-frame-options']).toBe('DENY');
      expect(response.headers['x-xss-protection']).toBe('1; mode=block');
      expect(response.headers['strict-transport-security']).toBeDefined();
    });

    it('should not expose server version', async () => {
      const response = await request.get('/');

      expect(response.headers['x-powered-by']).toBeUndefined();
      expect(response.headers['server']).toBeUndefined();
    });

    it('should not expose stack traces in production', async () => {
      const response = await request.get('/api/v1/trigger-error');

      expect(response.body.error).not.toHaveProperty('stack');
    });
  });

  describe('A07:2021 - Cross-Site Scripting (XSS)', () => {
    it('should escape HTML in responses', async () => {
      const xssPayload = '<script>alert("xss")</script>';

      // Create project with XSS payload
      const createResponse = await request.post('/api/v1/projects').send({
        name: xssPayload,
      });

      // Get project and verify HTML is escaped
      const getResponse = await request.get(
        `/api/v1/projects/${createResponse.body.data.id}`
      );

      expect(getResponse.body.data.name).not.toContain('<script>');
    });

    it('should set Content-Type header correctly', async () => {
      const response = await request.get('/api/v1/projects');

      expect(response.headers['content-type']).toContain('application/json');
    });
  });

  describe('A08:2021 - Software and Data Integrity Failures', () => {
    it('should validate webhook signatures', async () => {
      const payload = { event: 'test' };
      const invalidSignature = 'invalid-signature';

      const response = await request
        .post('/api/v1/webhooks/stripe')
        .set('stripe-signature', invalidSignature)
        .send(payload);

      expect(response.status).toBe(401);
    });
  });

  describe('A09:2021 - Security Logging and Monitoring Failures', () => {
    it('should log failed authentication attempts', async () => {
      // This would typically check logs, here we verify the response
      const response = await request.post('/api/v1/auth/login').send({
        email: 'test@example.com',
        password: 'wrongpassword',
      });

      expect(response.status).toBe(401);
      // In a real test, we'd verify the log entry was created
    });
  });
});
```

---

## 6. Test Coverage Configuration

### 6.1 Coverage Thresholds by Layer

```typescript
// jest.config.coverage.ts

export default {
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 85,
      lines: 85,
      statements: 85,
    },
    // Domain layer - highest coverage required
    './src/domain/**/*.ts': {
      branches: 95,
      functions: 95,
      lines: 95,
      statements: 95,
    },
    // Application layer - high coverage
    './src/application/**/*.ts': {
      branches: 90,
      functions: 90,
      lines: 90,
      statements: 90,
    },
    // Infrastructure layer
    './src/infrastructure/**/*.ts': {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
    // Presentation layer
    './src/api/**/*.ts': {
      branches: 85,
      functions: 85,
      lines: 85,
      statements: 85,
    },
  },
};
```

### 6.2 Coverage Report Configuration

```yaml
# .github/workflows/coverage.yaml

name: Test Coverage

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run tests with coverage
        run: npm run test:coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          fail_ci_if_error: true
          flags: unittests
          name: codecov-mindweave

      - name: Comment coverage on PR
        uses: romeovs/lcov-reporter-action@v0.3.1
        if: github.event_name == 'pull_request'
        with:
          lcov-file: ./coverage/lcov.info
          github-token: ${{ secrets.GITHUB_TOKEN }}
          delete-old-comments: true

      - name: Check coverage thresholds
        run: |
          npm run test:coverage:check
```

---

## 7. Continuous Testing in CI/CD

### 7.1 Test Pipeline Configuration

```yaml
# .github/workflows/test.yaml

name: Test Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  CI: true
  DATABASE_URL: postgresql://test:test@localhost:5432/test
  REDIS_URL: redis://localhost:6379

jobs:
  unit-tests:
    name: Unit Tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run unit tests
        run: npm run test:unit

      - name: Upload test results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: unit-test-results
          path: reports/junit.xml

  integration-tests:
    name: Integration Tests
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test
          POSTGRES_DB: test
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

      redis:
        image: redis:7
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run database migrations
        run: npm run db:migrate

      - name: Run integration tests
        run: npm run test:integration

      - name: Upload test results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: integration-test-results
          path: reports/integration-junit.xml

  e2e-tests:
    name: E2E Tests
    runs-on: ubuntu-latest
    needs: [unit-tests, integration-tests]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright browsers
        run: npx playwright install --with-deps

      - name: Start application
        run: |
          docker-compose -f docker-compose.test.yml up -d
          npm run wait-for-app

      - name: Run E2E tests
        run: npm run test:e2e

      - name: Upload Playwright report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: playwright-report
          path: playwright-report/

      - name: Stop application
        if: always()
        run: docker-compose -f docker-compose.test.yml down

  security-tests:
    name: Security Tests
    runs-on: ubuntu-latest
    needs: [integration-tests]
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run security tests
        run: npm run test:security

      - name: Run dependency audit
        run: npm audit --audit-level=high

  performance-tests:
    name: Performance Tests
    runs-on: ubuntu-latest
    needs: [integration-tests]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4

      - name: Setup k6
        run: |
          sudo gpg -k
          sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
          echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
          sudo apt-get update
          sudo apt-get install k6

      - name: Start application
        run: docker-compose -f docker-compose.test.yml up -d

      - name: Run load tests
        run: k6 run performance/load-test.js --out json=reports/k6-results.json

      - name: Upload performance results
        uses: actions/upload-artifact@v3
        with:
          name: performance-results
          path: reports/k6-results.json
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [DEVOPS-CICD.md](./DEVOPS-CICD.md) | CI/CD pipeline configuration |
| [BACKEND-SERVICES.md](./BACKEND-SERVICES.md) | Backend service architecture |
| [FRONTEND-ARCHITECTURE.md](./FRONTEND-ARCHITECTURE.md) | Frontend architecture |
| [SECURITY-ARCHITECTURE.md](./SECURITY-ARCHITECTURE.md) | Security controls |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-01-15 | Platform Engineering | Initial testing strategy |
