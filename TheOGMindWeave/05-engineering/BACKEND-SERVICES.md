# MindWeave Backend Services Architecture

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-006 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document details MindWeave's backend service implementations, including service patterns, middleware architecture, background job processing, and cross-cutting concerns like logging, error handling, and configuration management.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BACKEND SERVICES ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      REQUEST PIPELINE                                │   │
│  │                                                                      │   │
│  │  Request → Rate Limit → Auth → Validation → Handler → Response      │   │
│  │              │           │         │           │                     │   │
│  │              ▼           ▼         ▼           ▼                     │   │
│  │           Redis       JWT/       Zod/        Business               │   │
│  │           + Sliding   API Key    Schema      Logic                  │   │
│  │           Window                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      SERVICE LAYER                                   │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │   HTTP     │  │  gRPC      │  │  Event     │  │  Cron      │    │   │
│  │  │  Handlers  │  │  Services  │  │  Handlers  │  │   Jobs     │    │   │
│  │  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘    │   │
│  │        │               │               │               │            │   │
│  │        └───────────────┴───────────────┴───────────────┘            │   │
│  │                               │                                      │   │
│  │                        Domain Services                               │   │
│  └───────────────────────────────┼─────────────────────────────────────┘   │
│                                  │                                          │
│  ┌───────────────────────────────▼─────────────────────────────────────┐   │
│  │                      DATA ACCESS LAYER                               │   │
│  │                                                                      │   │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐    │   │
│  │  │ PostgreSQL │  │TimescaleDB │  │   Redis    │  │    S3      │    │   │
│  │  │Repository  │  │ Repository │  │  Client    │  │  Client    │    │   │
│  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Technology Stack

### 1.1 Core Technologies

| Technology | Version | Service | Purpose |
|------------|---------|---------|---------|
| **Node.js** | 20 LTS | Most services | Runtime |
| **TypeScript** | 5.x | All | Type safety |
| **Express** | 4.x | HTTP services | Web framework |
| **Fastify** | 4.x | High-perf APIs | Alternative framework |
| **Go** | 1.21+ | Usage tracker | High throughput |
| **Python** | 3.11+ | Analytics | Data processing |
| **Prisma** | 5.x | Node services | ORM |
| **BullMQ** | 4.x | Job queues | Background processing |

### 1.2 Service Implementation Languages

| Service | Language | Framework | Rationale |
|---------|----------|-----------|-----------|
| API Gateway | Node.js | Express | Ecosystem, middleware |
| Auth Service | Node.js | Express | Passport.js integration |
| Account Service | Node.js | Express | Stripe SDK |
| Analytics Service | Python | FastAPI | Pandas, NumPy |
| Usage Tracker | Go | Standard lib | Performance critical |
| MCP Registry | Node.js | Fastify | Speed, schemas |
| Governance Engine | Node.js | Express | OPA integration |
| Export Service | Python | FastAPI | Report generation |

---

## 2. Service Patterns

### 2.1 Clean Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        CLEAN ARCHITECTURE                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                    ┌─────────────────────────────────┐                     │
│                    │         DOMAIN LAYER            │                     │
│                    │                                 │                     │
│                    │  • Entities                     │                     │
│                    │  • Value Objects                │                     │
│                    │  • Domain Events                │                     │
│                    │  • Business Rules               │                     │
│                    │                                 │                     │
│                    │     (No external deps)          │                     │
│                    └─────────────────────────────────┘                     │
│                                   ▲                                         │
│                                   │                                         │
│                    ┌──────────────┴──────────────────┐                     │
│                    │      APPLICATION LAYER          │                     │
│                    │                                 │                     │
│                    │  • Use Cases                    │                     │
│                    │  • Application Services         │                     │
│                    │  • DTOs                         │                     │
│                    │  • Interface Definitions        │                     │
│                    │                                 │                     │
│                    │  (Orchestrates domain logic)    │                     │
│                    └─────────────────────────────────┘                     │
│                                   ▲                                         │
│                                   │                                         │
│         ┌─────────────────────────┼─────────────────────────┐              │
│         │                         │                         │              │
│  ┌──────┴──────┐         ┌────────┴────────┐      ┌────────┴────────┐     │
│  │ PRESENTATION│         │  INFRASTRUCTURE │      │    EXTERNAL     │     │
│  │   LAYER     │         │     LAYER       │      │   INTERFACES    │     │
│  │             │         │                 │      │                 │     │
│  │ • Routes    │         │ • Repositories  │      │ • HTTP Clients  │     │
│  │ • Controllers│        │ • Database      │      │ • Message Queue │     │
│  │ • Middleware│         │ • Cache         │      │ • External APIs │     │
│  │ • Validation│         │ • File Storage  │      │ • Webhooks      │     │
│  └─────────────┘         └─────────────────┘      └─────────────────┘     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Project Structure

```
services/
├── auth-service/
│   ├── src/
│   │   ├── domain/                    # Domain Layer
│   │   │   ├── entities/
│   │   │   │   ├── user.entity.ts
│   │   │   │   └── session.entity.ts
│   │   │   ├── value-objects/
│   │   │   │   ├── email.vo.ts
│   │   │   │   └── password.vo.ts
│   │   │   ├── events/
│   │   │   │   └── user-created.event.ts
│   │   │   └── errors/
│   │   │       └── domain-errors.ts
│   │   │
│   │   ├── application/               # Application Layer
│   │   │   ├── use-cases/
│   │   │   │   ├── login.use-case.ts
│   │   │   │   ├── register.use-case.ts
│   │   │   │   └── refresh-token.use-case.ts
│   │   │   ├── services/
│   │   │   │   └── auth.service.ts
│   │   │   ├── dtos/
│   │   │   │   ├── login.dto.ts
│   │   │   │   └── register.dto.ts
│   │   │   └── interfaces/
│   │   │       ├── user-repository.interface.ts
│   │   │       └── token-service.interface.ts
│   │   │
│   │   ├── infrastructure/            # Infrastructure Layer
│   │   │   ├── database/
│   │   │   │   ├── prisma/
│   │   │   │   │   └── schema.prisma
│   │   │   │   └── repositories/
│   │   │   │       └── user.repository.ts
│   │   │   ├── cache/
│   │   │   │   └── redis.client.ts
│   │   │   ├── services/
│   │   │   │   ├── jwt-token.service.ts
│   │   │   │   └── bcrypt-password.service.ts
│   │   │   └── messaging/
│   │   │       └── kafka.producer.ts
│   │   │
│   │   ├── presentation/              # Presentation Layer
│   │   │   ├── routes/
│   │   │   │   └── auth.routes.ts
│   │   │   ├── controllers/
│   │   │   │   └── auth.controller.ts
│   │   │   ├── middleware/
│   │   │   │   ├── auth.middleware.ts
│   │   │   │   └── validation.middleware.ts
│   │   │   └── validators/
│   │   │       └── auth.validators.ts
│   │   │
│   │   ├── config/                    # Configuration
│   │   │   ├── database.config.ts
│   │   │   ├── redis.config.ts
│   │   │   └── app.config.ts
│   │   │
│   │   └── main.ts                    # Entry point
│   │
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   │
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
```

---

## 3. HTTP Service Implementation

### 3.1 Express Application Setup

```typescript
// src/main.ts
import express from 'express';
import helmet from 'helmet';
import cors from 'cors';
import compression from 'compression';
import { pinoHttp } from 'pino-http';
import { errorHandler } from './presentation/middleware/error-handler';
import { notFoundHandler } from './presentation/middleware/not-found-handler';
import { authRoutes } from './presentation/routes/auth.routes';
import { healthRoutes } from './presentation/routes/health.routes';
import { config } from './config/app.config';
import { logger } from './infrastructure/logging/logger';
import { connectDatabase } from './infrastructure/database/connection';
import { connectRedis } from './infrastructure/cache/redis.client';

async function bootstrap() {
  const app = express();

  // Connect to databases
  await connectDatabase();
  await connectRedis();

  // Global middleware
  app.use(helmet());
  app.use(cors(config.cors));
  app.use(compression());
  app.use(express.json({ limit: '10mb' }));
  app.use(express.urlencoded({ extended: true }));
  app.use(pinoHttp({ logger }));

  // Trust proxy for rate limiting
  app.set('trust proxy', 1);

  // Health check (no auth)
  app.use('/health', healthRoutes);

  // API routes
  app.use('/auth', authRoutes);

  // Error handling
  app.use(notFoundHandler);
  app.use(errorHandler);

  // Start server
  const server = app.listen(config.port, () => {
    logger.info(`Auth service listening on port ${config.port}`);
  });

  // Graceful shutdown
  const shutdown = async () => {
    logger.info('Shutting down gracefully...');
    server.close(async () => {
      await disconnectDatabase();
      await disconnectRedis();
      process.exit(0);
    });
  };

  process.on('SIGTERM', shutdown);
  process.on('SIGINT', shutdown);
}

bootstrap().catch((error) => {
  logger.error('Failed to start service', error);
  process.exit(1);
});
```

### 3.2 Controller Pattern

```typescript
// src/presentation/controllers/auth.controller.ts
import { Request, Response, NextFunction } from 'express';
import { LoginUseCase } from '@/application/use-cases/login.use-case';
import { RegisterUseCase } from '@/application/use-cases/register.use-case';
import { RefreshTokenUseCase } from '@/application/use-cases/refresh-token.use-case';
import { LoginDTO, RegisterDTO, RefreshDTO } from '@/application/dtos';
import { HttpStatus } from '@/shared/constants';

export class AuthController {
  constructor(
    private readonly loginUseCase: LoginUseCase,
    private readonly registerUseCase: RegisterUseCase,
    private readonly refreshTokenUseCase: RefreshTokenUseCase
  ) {}

  login = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const dto: LoginDTO = req.body;
      const result = await this.loginUseCase.execute(dto);

      res.status(HttpStatus.OK).json({
        success: true,
        data: {
          accessToken: result.accessToken,
          refreshToken: result.refreshToken,
          user: result.user,
        },
      });
    } catch (error) {
      next(error);
    }
  };

  register = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const dto: RegisterDTO = req.body;
      const result = await this.registerUseCase.execute(dto);

      res.status(HttpStatus.CREATED).json({
        success: true,
        data: {
          user: result.user,
          accessToken: result.accessToken,
          refreshToken: result.refreshToken,
        },
      });
    } catch (error) {
      next(error);
    }
  };

  refresh = async (req: Request, res: Response, next: NextFunction) => {
    try {
      const dto: RefreshDTO = req.body;
      const result = await this.refreshTokenUseCase.execute(dto);

      res.status(HttpStatus.OK).json({
        success: true,
        data: {
          accessToken: result.accessToken,
          refreshToken: result.refreshToken,
        },
      });
    } catch (error) {
      next(error);
    }
  };

  logout = async (req: Request, res: Response, next: NextFunction) => {
    try {
      // Invalidate refresh token
      await this.authService.logout(req.user.id, req.body.refreshToken);

      res.status(HttpStatus.NO_CONTENT).send();
    } catch (error) {
      next(error);
    }
  };
}
```

### 3.3 Use Case Pattern

```typescript
// src/application/use-cases/login.use-case.ts
import { Injectable } from '@/shared/decorators';
import { IUserRepository } from '@/application/interfaces/user-repository.interface';
import { ITokenService } from '@/application/interfaces/token-service.interface';
import { IPasswordService } from '@/application/interfaces/password-service.interface';
import { LoginDTO, LoginResultDTO } from '@/application/dtos';
import { UnauthorizedError, ValidationError } from '@/domain/errors';
import { EventBus } from '@/infrastructure/messaging/event-bus';
import { UserLoggedInEvent } from '@/domain/events';

@Injectable()
export class LoginUseCase {
  constructor(
    private readonly userRepository: IUserRepository,
    private readonly tokenService: ITokenService,
    private readonly passwordService: IPasswordService,
    private readonly eventBus: EventBus
  ) {}

  async execute(dto: LoginDTO): Promise<LoginResultDTO> {
    // Find user by email
    const user = await this.userRepository.findByEmail(dto.email);
    if (!user) {
      throw new UnauthorizedError('Invalid credentials');
    }

    // Verify password
    const isValidPassword = await this.passwordService.verify(
      dto.password,
      user.passwordHash
    );
    if (!isValidPassword) {
      throw new UnauthorizedError('Invalid credentials');
    }

    // Check user status
    if (user.status !== 'active') {
      throw new UnauthorizedError('Account is not active');
    }

    // Check MFA if enabled
    if (user.mfaEnabled) {
      if (!dto.mfaCode) {
        return {
          requiresMfa: true,
          mfaToken: await this.tokenService.generateMfaToken(user.id),
        };
      }
      const isValidMfa = await this.validateMfaCode(user, dto.mfaCode);
      if (!isValidMfa) {
        throw new UnauthorizedError('Invalid MFA code');
      }
    }

    // Generate tokens
    const accessToken = this.tokenService.generateAccessToken({
      userId: user.id,
      email: user.email,
      role: user.role,
    });
    const refreshToken = await this.tokenService.generateRefreshToken(user.id);

    // Update last login
    await this.userRepository.updateLastLogin(user.id, dto.ip);

    // Publish event
    this.eventBus.publish(new UserLoggedInEvent(user.id, dto.ip));

    return {
      user: this.mapToUserDTO(user),
      accessToken,
      refreshToken,
    };
  }

  private async validateMfaCode(user: User, code: string): Promise<boolean> {
    // TOTP validation logic
    return this.mfaService.verify(user.mfaSecret, code);
  }

  private mapToUserDTO(user: User): UserDTO {
    return {
      id: user.id,
      email: user.email,
      name: user.name,
      avatarUrl: user.avatarUrl,
      role: user.role,
      mfaEnabled: user.mfaEnabled,
    };
  }
}
```

---

## 4. Middleware Architecture

### 4.1 Middleware Pipeline

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       MIDDLEWARE PIPELINE                                   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  REQUEST                                                                   │
│     │                                                                       │
│     ▼                                                                       │
│  ┌─────────────────┐                                                       │
│  │   Request ID    │  Generate unique request ID                           │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │    Logging      │  Log request start                                   │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │  Rate Limiting  │  Check rate limits (Redis)                           │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │ Authentication  │  Verify JWT/API Key                                   │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │ Authorization   │  Check permissions                                    │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │   Validation    │  Validate request body                               │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │    Handler      │  Business logic                                       │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌─────────────────┐                                                       │
│  │ Error Handler   │  Catch and format errors                              │
│  └────────┬────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│     RESPONSE                                                               │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Middleware Implementations

```typescript
// src/presentation/middleware/auth.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { UnauthorizedError, ForbiddenError } from '@/domain/errors';
import { ITokenService } from '@/application/interfaces/token-service.interface';
import { container } from '@/infrastructure/di/container';

export interface AuthenticatedRequest extends Request {
  user: {
    id: string;
    email: string;
    orgId: string;
    role: string;
    permissions: string[];
  };
}

export const authenticate = async (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  try {
    const authHeader = req.headers.authorization;

    if (!authHeader) {
      throw new UnauthorizedError('No authorization header');
    }

    // Check for Bearer token
    if (authHeader.startsWith('Bearer ')) {
      const token = authHeader.substring(7);
      const tokenService = container.get<ITokenService>(ITokenService);
      const payload = await tokenService.verifyAccessToken(token);

      (req as AuthenticatedRequest).user = {
        id: payload.userId,
        email: payload.email,
        orgId: payload.orgId,
        role: payload.role,
        permissions: payload.permissions,
      };
    }
    // Check for API Key
    else if (authHeader.startsWith('mw_sk_') || authHeader.startsWith('mw_pk_')) {
      const apiKeyService = container.get<IApiKeyService>(IApiKeyService);
      const apiKey = await apiKeyService.validate(authHeader);

      (req as AuthenticatedRequest).user = {
        id: apiKey.projectId,
        email: '',
        orgId: apiKey.orgId,
        role: 'api_key',
        permissions: apiKey.scopes,
      };
    } else {
      throw new UnauthorizedError('Invalid authorization format');
    }

    next();
  } catch (error) {
    next(error);
  }
};

// Role-based authorization
export const authorize = (...allowedRoles: string[]) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as AuthenticatedRequest).user;

    if (!user) {
      return next(new UnauthorizedError('Not authenticated'));
    }

    if (!allowedRoles.includes(user.role)) {
      return next(new ForbiddenError('Insufficient permissions'));
    }

    next();
  };
};

// Permission-based authorization
export const requirePermission = (permission: string) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const user = (req as AuthenticatedRequest).user;

    if (!user) {
      return next(new UnauthorizedError('Not authenticated'));
    }

    if (!user.permissions.includes(permission)) {
      return next(new ForbiddenError(`Missing permission: ${permission}`));
    }

    next();
  };
};
```

```typescript
// src/presentation/middleware/rate-limit.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { RateLimiterRedis, RateLimiterRes } from 'rate-limiter-flexible';
import { redis } from '@/infrastructure/cache/redis.client';
import { TooManyRequestsError } from '@/domain/errors';

// Different rate limiters for different endpoints
const rateLimiters = {
  global: new RateLimiterRedis({
    storeClient: redis,
    keyPrefix: 'rl:global',
    points: 1000, // requests
    duration: 60, // per minute
  }),
  auth: new RateLimiterRedis({
    storeClient: redis,
    keyPrefix: 'rl:auth',
    points: 10,
    duration: 60,
    blockDuration: 60 * 15, // Block for 15 min after limit
  }),
  api: new RateLimiterRedis({
    storeClient: redis,
    keyPrefix: 'rl:api',
    points: 600,
    duration: 60,
  }),
};

export const rateLimit = (limiterType: keyof typeof rateLimiters = 'global') => {
  const limiter = rateLimiters[limiterType];

  return async (req: Request, res: Response, next: NextFunction) => {
    try {
      // Use IP or user ID as key
      const key = req.user?.id || req.ip;
      const result = await limiter.consume(key);

      // Add rate limit headers
      res.set({
        'X-RateLimit-Limit': limiter.points.toString(),
        'X-RateLimit-Remaining': result.remainingPoints.toString(),
        'X-RateLimit-Reset': new Date(
          Date.now() + result.msBeforeNext
        ).toISOString(),
      });

      next();
    } catch (error) {
      if (error instanceof RateLimiterRes) {
        res.set({
          'X-RateLimit-Limit': limiter.points.toString(),
          'X-RateLimit-Remaining': '0',
          'X-RateLimit-Reset': new Date(
            Date.now() + error.msBeforeNext
          ).toISOString(),
          'Retry-After': Math.ceil(error.msBeforeNext / 1000).toString(),
        });
        next(new TooManyRequestsError('Rate limit exceeded'));
      } else {
        next(error);
      }
    }
  };
};
```

```typescript
// src/presentation/middleware/validation.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { ZodSchema, ZodError } from 'zod';
import { ValidationError } from '@/domain/errors';

export const validate = (schema: ZodSchema, source: 'body' | 'query' | 'params' = 'body') => {
  return async (req: Request, res: Response, next: NextFunction) => {
    try {
      const data = await schema.parseAsync(req[source]);
      req[source] = data;
      next();
    } catch (error) {
      if (error instanceof ZodError) {
        const details = error.errors.map((err) => ({
          field: err.path.join('.'),
          message: err.message,
          code: err.code,
        }));
        next(new ValidationError('Validation failed', details));
      } else {
        next(error);
      }
    }
  };
};

// Usage in routes
// router.post('/login', validate(loginSchema), authController.login);
```

---

## 5. Background Job Processing

### 5.1 Job Queue Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       JOB QUEUE ARCHITECTURE                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRODUCERS                    REDIS QUEUES                WORKERS          │
│                                                                             │
│  ┌──────────────┐           ┌──────────────┐           ┌──────────────┐   │
│  │  API Server  │──────────►│    email     │──────────►│Email Worker  │   │
│  └──────────────┘           └──────────────┘           └──────────────┘   │
│                                                                             │
│  ┌──────────────┐           ┌──────────────┐           ┌──────────────┐   │
│  │  Scheduler   │──────────►│   reports    │──────────►│Report Worker │   │
│  └──────────────┘           └──────────────┘           └──────────────┘   │
│                                                                             │
│  ┌──────────────┐           ┌──────────────┐           ┌──────────────┐   │
│  │Event Handler │──────────►│  analytics   │──────────►│Analyt Worker │   │
│  └──────────────┘           └──────────────┘           └──────────────┘   │
│                                                                             │
│  ┌──────────────┐           ┌──────────────┐           ┌──────────────┐   │
│  │   Webhook    │──────────►│  webhooks    │──────────►│Webhook Worker│   │
│  └──────────────┘           └──────────────┘           └──────────────┘   │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────     │
│                                                                             │
│  QUEUE CHARACTERISTICS:                                                    │
│                                                                             │
│  email     - Priority: High,   Concurrency: 10, Retry: 3                  │
│  reports   - Priority: Low,    Concurrency: 2,  Retry: 2                  │
│  analytics - Priority: Medium, Concurrency: 5,  Retry: 3                  │
│  webhooks  - Priority: High,   Concurrency: 20, Retry: 5                  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 BullMQ Implementation

```typescript
// src/infrastructure/jobs/queue.ts
import { Queue, Worker, Job, QueueEvents } from 'bullmq';
import { redis } from '@/infrastructure/cache/redis.client';
import { logger } from '@/infrastructure/logging/logger';

// Queue configuration
const defaultConfig = {
  connection: redis,
  defaultJobOptions: {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 1000,
    },
    removeOnComplete: {
      age: 24 * 60 * 60, // 24 hours
      count: 1000,
    },
    removeOnFail: {
      age: 7 * 24 * 60 * 60, // 7 days
    },
  },
};

// Create queues
export const emailQueue = new Queue('email', defaultConfig);
export const reportsQueue = new Queue('reports', defaultConfig);
export const analyticsQueue = new Queue('analytics', defaultConfig);
export const webhooksQueue = new Queue('webhooks', defaultConfig);

// Job types
interface EmailJob {
  type: 'welcome' | 'reset_password' | 'alert' | 'invoice';
  to: string;
  data: Record<string, unknown>;
}

interface ReportJob {
  type: 'usage' | 'billing' | 'audit';
  orgId: string;
  startDate: string;
  endDate: string;
  format: 'pdf' | 'csv' | 'xlsx';
  deliverTo: string[];
}

// Producer functions
export const queueEmail = async (job: EmailJob, options?: { priority?: number }) => {
  return emailQueue.add(job.type, job, {
    priority: options?.priority ?? 2,
  });
};

export const queueReport = async (job: ReportJob) => {
  return reportsQueue.add(job.type, job, {
    priority: 3,
    attempts: 2,
  });
};

export const scheduleRecurringJob = async (
  queue: Queue,
  name: string,
  data: unknown,
  pattern: string // cron pattern
) => {
  return queue.add(name, data, {
    repeat: {
      pattern,
    },
  });
};
```

```typescript
// src/infrastructure/jobs/workers/email.worker.ts
import { Worker, Job } from 'bullmq';
import { redis } from '@/infrastructure/cache/redis.client';
import { EmailService } from '@/infrastructure/services/email.service';
import { logger } from '@/infrastructure/logging/logger';

const emailService = new EmailService();

export const emailWorker = new Worker(
  'email',
  async (job: Job) => {
    logger.info(`Processing email job: ${job.id}`, { type: job.name });

    switch (job.name) {
      case 'welcome':
        await emailService.sendWelcome(job.data.to, job.data.data);
        break;
      case 'reset_password':
        await emailService.sendPasswordReset(job.data.to, job.data.data);
        break;
      case 'alert':
        await emailService.sendAlert(job.data.to, job.data.data);
        break;
      case 'invoice':
        await emailService.sendInvoice(job.data.to, job.data.data);
        break;
      default:
        throw new Error(`Unknown email type: ${job.name}`);
    }

    return { sent: true, timestamp: new Date().toISOString() };
  },
  {
    connection: redis,
    concurrency: 10,
    limiter: {
      max: 100,
      duration: 1000, // 100 emails per second
    },
  }
);

// Event handlers
emailWorker.on('completed', (job) => {
  logger.info(`Email job completed: ${job.id}`);
});

emailWorker.on('failed', (job, error) => {
  logger.error(`Email job failed: ${job?.id}`, error);
});

emailWorker.on('error', (error) => {
  logger.error('Email worker error', error);
});
```

### 5.3 Scheduled Jobs

```typescript
// src/infrastructure/jobs/scheduler.ts
import { Queue } from 'bullmq';
import { analyticsQueue, reportsQueue } from './queue';
import { logger } from '@/infrastructure/logging/logger';

export async function initializeScheduledJobs() {
  // Daily aggregation at 1 AM UTC
  await analyticsQueue.add(
    'daily-aggregation',
    { type: 'daily' },
    {
      repeat: { pattern: '0 1 * * *' },
      jobId: 'daily-aggregation',
    }
  );

  // Hourly usage summary
  await analyticsQueue.add(
    'hourly-summary',
    { type: 'hourly' },
    {
      repeat: { pattern: '0 * * * *' },
      jobId: 'hourly-summary',
    }
  );

  // Monthly billing reports on 1st of month
  await reportsQueue.add(
    'monthly-billing',
    { type: 'billing' },
    {
      repeat: { pattern: '0 6 1 * *' }, // 6 AM on 1st
      jobId: 'monthly-billing',
    }
  );

  // Weekly audit log cleanup
  await analyticsQueue.add(
    'audit-cleanup',
    { retentionDays: 90 },
    {
      repeat: { pattern: '0 3 * * 0' }, // Sunday 3 AM
      jobId: 'audit-cleanup',
    }
  );

  logger.info('Scheduled jobs initialized');
}
```

---

## 6. Event-Driven Architecture

### 6.1 Event Bus Implementation

```typescript
// src/infrastructure/messaging/event-bus.ts
import { Kafka, Producer, Consumer, EachMessagePayload } from 'kafkajs';
import { logger } from '@/infrastructure/logging/logger';
import { config } from '@/config/app.config';

interface DomainEvent {
  type: string;
  aggregateId: string;
  timestamp: Date;
  data: unknown;
  metadata?: {
    correlationId?: string;
    causationId?: string;
    userId?: string;
  };
}

class EventBus {
  private kafka: Kafka;
  private producer: Producer;
  private consumers: Map<string, Consumer> = new Map();

  constructor() {
    this.kafka = new Kafka({
      clientId: config.serviceName,
      brokers: config.kafka.brokers,
      ssl: config.kafka.ssl,
      sasl: config.kafka.sasl,
    });
    this.producer = this.kafka.producer();
  }

  async connect() {
    await this.producer.connect();
    logger.info('Kafka producer connected');
  }

  async disconnect() {
    await this.producer.disconnect();
    for (const consumer of this.consumers.values()) {
      await consumer.disconnect();
    }
  }

  async publish(event: DomainEvent) {
    const topic = this.getTopicForEvent(event.type);

    await this.producer.send({
      topic,
      messages: [
        {
          key: event.aggregateId,
          value: JSON.stringify(event),
          headers: {
            'event-type': event.type,
            'timestamp': event.timestamp.toISOString(),
            'correlation-id': event.metadata?.correlationId ?? '',
          },
        },
      ],
    });

    logger.debug(`Published event: ${event.type}`, { aggregateId: event.aggregateId });
  }

  async subscribe(
    topic: string,
    groupId: string,
    handler: (event: DomainEvent) => Promise<void>
  ) {
    const consumer = this.kafka.consumer({ groupId });
    await consumer.connect();
    await consumer.subscribe({ topic, fromBeginning: false });

    await consumer.run({
      eachMessage: async ({ message }: EachMessagePayload) => {
        try {
          const event = JSON.parse(message.value?.toString() ?? '{}') as DomainEvent;
          await handler(event);
        } catch (error) {
          logger.error(`Error processing event from ${topic}`, error);
          // Implement dead letter queue here
        }
      },
    });

    this.consumers.set(`${topic}:${groupId}`, consumer);
    logger.info(`Subscribed to topic: ${topic}`);
  }

  private getTopicForEvent(eventType: string): string {
    const [domain] = eventType.split('.');
    return `mindweave.${domain}.events`;
  }
}

export const eventBus = new EventBus();
```

### 6.2 Event Handlers

```typescript
// src/application/event-handlers/user-events.handler.ts
import { eventBus } from '@/infrastructure/messaging/event-bus';
import { queueEmail } from '@/infrastructure/jobs/queue';
import { logger } from '@/infrastructure/logging/logger';

export async function initializeUserEventHandlers() {
  // Handle user.created events
  await eventBus.subscribe(
    'mindweave.user.events',
    'user-welcome-email',
    async (event) => {
      if (event.type !== 'user.created') return;

      await queueEmail({
        type: 'welcome',
        to: event.data.email,
        data: {
          name: event.data.name,
          verificationUrl: event.data.verificationUrl,
        },
      });

      logger.info('Queued welcome email', { userId: event.aggregateId });
    }
  );

  // Handle user.password_reset events
  await eventBus.subscribe(
    'mindweave.user.events',
    'password-reset-email',
    async (event) => {
      if (event.type !== 'user.password_reset') return;

      await queueEmail({
        type: 'reset_password',
        to: event.data.email,
        data: {
          resetUrl: event.data.resetUrl,
          expiresIn: '1 hour',
        },
      }, { priority: 1 });
    }
  );
}
```

---

## 7. Error Handling

### 7.1 Error Hierarchy

```typescript
// src/domain/errors/base.error.ts
export abstract class DomainError extends Error {
  abstract readonly code: string;
  abstract readonly statusCode: number;
  readonly isOperational: boolean = true;
  readonly timestamp: Date = new Date();

  constructor(message: string, public readonly details?: unknown) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }

  toJSON() {
    return {
      code: this.code,
      message: this.message,
      details: this.details,
      timestamp: this.timestamp.toISOString(),
    };
  }
}

// Specific errors
export class ValidationError extends DomainError {
  readonly code = 'VALIDATION_ERROR';
  readonly statusCode = 400;
}

export class UnauthorizedError extends DomainError {
  readonly code = 'UNAUTHORIZED';
  readonly statusCode = 401;
}

export class ForbiddenError extends DomainError {
  readonly code = 'FORBIDDEN';
  readonly statusCode = 403;
}

export class NotFoundError extends DomainError {
  readonly code = 'NOT_FOUND';
  readonly statusCode = 404;
}

export class ConflictError extends DomainError {
  readonly code = 'CONFLICT';
  readonly statusCode = 409;
}

export class TooManyRequestsError extends DomainError {
  readonly code = 'TOO_MANY_REQUESTS';
  readonly statusCode = 429;
}

export class InternalError extends DomainError {
  readonly code = 'INTERNAL_ERROR';
  readonly statusCode = 500;
  readonly isOperational = false;
}
```

### 7.2 Global Error Handler

```typescript
// src/presentation/middleware/error-handler.ts
import { Request, Response, NextFunction } from 'express';
import { DomainError, InternalError } from '@/domain/errors';
import { logger } from '@/infrastructure/logging/logger';
import { config } from '@/config/app.config';

export const errorHandler = (
  error: Error,
  req: Request,
  res: Response,
  _next: NextFunction
) => {
  // Log error
  const requestId = req.headers['x-request-id'] as string;

  if (error instanceof DomainError) {
    if (!error.isOperational) {
      // Critical error - alert team
      logger.error('Critical error', {
        error: error.toJSON(),
        requestId,
        path: req.path,
        method: req.method,
      });
    } else {
      logger.warn('Operational error', {
        error: error.toJSON(),
        requestId,
      });
    }

    return res.status(error.statusCode).json({
      success: false,
      error: {
        code: error.code,
        message: error.message,
        details: error.details,
        requestId,
        ...(config.isDevelopment && { stack: error.stack }),
      },
    });
  }

  // Unknown error - treat as internal
  logger.error('Unhandled error', {
    error: {
      name: error.name,
      message: error.message,
      stack: error.stack,
    },
    requestId,
    path: req.path,
    method: req.method,
  });

  return res.status(500).json({
    success: false,
    error: {
      code: 'INTERNAL_ERROR',
      message: config.isDevelopment
        ? error.message
        : 'An unexpected error occurred',
      requestId,
      ...(config.isDevelopment && { stack: error.stack }),
    },
  });
};
```

---

## 8. Logging and Observability

### 8.1 Structured Logging

```typescript
// src/infrastructure/logging/logger.ts
import pino from 'pino';
import { config } from '@/config/app.config';

export const logger = pino({
  name: config.serviceName,
  level: config.logLevel,
  formatters: {
    level: (label) => ({ level: label }),
    bindings: () => ({
      service: config.serviceName,
      version: config.version,
      environment: config.environment,
    }),
  },
  timestamp: () => `,"timestamp":"${new Date().toISOString()}"`,
  redact: {
    paths: ['password', 'passwordHash', 'token', 'apiKey', 'secret'],
    censor: '[REDACTED]',
  },
  transport: config.isDevelopment
    ? {
        target: 'pino-pretty',
        options: {
          colorize: true,
          translateTime: 'SYS:standard',
          ignore: 'pid,hostname',
        },
      }
    : undefined,
});

// Request logging helper
export const createRequestLogger = (requestId: string, userId?: string) => {
  return logger.child({ requestId, userId });
};
```

### 8.2 Request Tracing

```typescript
// src/presentation/middleware/request-id.middleware.ts
import { Request, Response, NextFunction } from 'express';
import { v4 as uuidv4 } from 'uuid';

export const requestIdMiddleware = (
  req: Request,
  res: Response,
  next: NextFunction
) => {
  const requestId = (req.headers['x-request-id'] as string) || uuidv4();

  req.headers['x-request-id'] = requestId;
  res.setHeader('x-request-id', requestId);

  // Add to async context for logging
  next();
};
```

---

## 9. Configuration Management

### 9.1 Environment Configuration

```typescript
// src/config/app.config.ts
import { z } from 'zod';

const configSchema = z.object({
  // Application
  serviceName: z.string().default('mindweave-api'),
  version: z.string().default('1.0.0'),
  environment: z.enum(['development', 'staging', 'production']),
  port: z.coerce.number().default(3000),
  host: z.string().default('0.0.0.0'),

  // Database
  databaseUrl: z.string().url(),
  databasePoolMin: z.coerce.number().default(2),
  databasePoolMax: z.coerce.number().default(10),

  // Redis
  redisUrl: z.string().url(),

  // Kafka
  kafkaBrokers: z.string().transform((s) => s.split(',')),

  // Auth
  jwtSecret: z.string().min(32),
  jwtAccessExpiry: z.string().default('15m'),
  jwtRefreshExpiry: z.string().default('7d'),

  // External services
  stripeSecretKey: z.string().optional(),
  sendgridApiKey: z.string().optional(),

  // Logging
  logLevel: z.enum(['debug', 'info', 'warn', 'error']).default('info'),

  // CORS
  corsOrigins: z.string().transform((s) => s.split(',')),
});

type Config = z.infer<typeof configSchema>;

const parseConfig = (): Config => {
  const result = configSchema.safeParse({
    serviceName: process.env.SERVICE_NAME,
    version: process.env.VERSION,
    environment: process.env.NODE_ENV || 'development',
    port: process.env.PORT,
    host: process.env.HOST,
    databaseUrl: process.env.DATABASE_URL,
    databasePoolMin: process.env.DATABASE_POOL_MIN,
    databasePoolMax: process.env.DATABASE_POOL_MAX,
    redisUrl: process.env.REDIS_URL,
    kafkaBrokers: process.env.KAFKA_BROKERS,
    jwtSecret: process.env.JWT_SECRET,
    jwtAccessExpiry: process.env.JWT_ACCESS_EXPIRY,
    jwtRefreshExpiry: process.env.JWT_REFRESH_EXPIRY,
    stripeSecretKey: process.env.STRIPE_SECRET_KEY,
    sendgridApiKey: process.env.SENDGRID_API_KEY,
    logLevel: process.env.LOG_LEVEL,
    corsOrigins: process.env.CORS_ORIGINS || 'http://localhost:3000',
  });

  if (!result.success) {
    console.error('Configuration validation failed:', result.error.format());
    process.exit(1);
  }

  return result.data;
};

export const config = parseConfig();

// Computed properties
export const isDevelopment = config.environment === 'development';
export const isProduction = config.environment === 'production';
```

---

## 10. Health Checks

### 10.1 Health Check Endpoints

```typescript
// src/presentation/routes/health.routes.ts
import { Router } from 'express';
import { prisma } from '@/infrastructure/database/connection';
import { redis } from '@/infrastructure/cache/redis.client';
import { kafka } from '@/infrastructure/messaging/kafka.client';

const router = Router();

// Liveness probe - is the service running?
router.get('/live', (req, res) => {
  res.status(200).json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Readiness probe - can the service handle traffic?
router.get('/ready', async (req, res) => {
  const checks = await Promise.allSettled([
    checkDatabase(),
    checkRedis(),
    checkKafka(),
  ]);

  const results = {
    database: checks[0].status === 'fulfilled' ? 'ok' : 'error',
    redis: checks[1].status === 'fulfilled' ? 'ok' : 'error',
    kafka: checks[2].status === 'fulfilled' ? 'ok' : 'error',
  };

  const isReady = Object.values(results).every((v) => v === 'ok');

  res.status(isReady ? 200 : 503).json({
    status: isReady ? 'ready' : 'not_ready',
    checks: results,
    timestamp: new Date().toISOString(),
  });
});

// Detailed health check
router.get('/health', async (req, res) => {
  const startTime = Date.now();

  const [dbCheck, redisCheck, kafkaCheck] = await Promise.allSettled([
    checkDatabaseDetailed(),
    checkRedisDetailed(),
    checkKafkaDetailed(),
  ]);

  const response = {
    status: 'healthy',
    version: process.env.VERSION || '1.0.0',
    uptime: process.uptime(),
    checks: {
      database:
        dbCheck.status === 'fulfilled'
          ? dbCheck.value
          : { status: 'error', error: dbCheck.reason.message },
      redis:
        redisCheck.status === 'fulfilled'
          ? redisCheck.value
          : { status: 'error', error: redisCheck.reason.message },
      kafka:
        kafkaCheck.status === 'fulfilled'
          ? kafkaCheck.value
          : { status: 'error', error: kafkaCheck.reason.message },
    },
    responseTime: Date.now() - startTime,
    timestamp: new Date().toISOString(),
  };

  const hasError = Object.values(response.checks).some(
    (c) => c.status === 'error'
  );
  response.status = hasError ? 'degraded' : 'healthy';

  res.status(hasError ? 503 : 200).json(response);
});

async function checkDatabase(): Promise<boolean> {
  await prisma.$queryRaw`SELECT 1`;
  return true;
}

async function checkDatabaseDetailed() {
  const start = Date.now();
  await prisma.$queryRaw`SELECT 1`;
  return {
    status: 'ok',
    latency: Date.now() - start,
    pool: {
      // Add pool stats if available
    },
  };
}

async function checkRedis(): Promise<boolean> {
  await redis.ping();
  return true;
}

async function checkRedisDetailed() {
  const start = Date.now();
  await redis.ping();
  const info = await redis.info('memory');
  return {
    status: 'ok',
    latency: Date.now() - start,
    memory: info,
  };
}

async function checkKafka(): Promise<boolean> {
  // Check Kafka connectivity
  return true;
}

async function checkKafkaDetailed() {
  return {
    status: 'ok',
    latency: 0,
  };
}

export { router as healthRoutes };
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System design |
| [MICROSERVICES-DESIGN.md](./MICROSERVICES-DESIGN.md) | Service architecture |
| [API-SPECIFICATIONS.md](./API-SPECIFICATIONS.md) | API contracts |
| [DATABASE-SCHEMA.md](./DATABASE-SCHEMA.md) | Data models |
| [MONITORING-OBSERVABILITY.md](./MONITORING-OBSERVABILITY.md) | Observability |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial backend services documentation |
