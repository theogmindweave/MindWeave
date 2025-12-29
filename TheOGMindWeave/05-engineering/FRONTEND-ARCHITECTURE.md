# MindWeave Frontend Architecture

## Document Information
| Field | Value |
|-------|-------|
| Document ID | ENG-005 |
| Version | 1.0 |
| Last Updated | 2024-01-15 |
| Owner | Engineering Team |
| Status | Draft |
| Classification | Internal |

---

## Executive Summary

This document defines MindWeave's frontend architecture, including component design, state management, routing strategy, and build optimization. We use a modern React-based stack with Next.js for server-side rendering and optimal performance.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MINDWEAVE FRONTEND ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         PRESENTATION                                 │   │
│  │                                                                      │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐ │   │
│  │  │   Pages     │  │ Components  │  │   Layouts   │  │   Styles   │ │   │
│  │  │             │  │             │  │             │  │            │ │   │
│  │  │ • Dashboard │  │ • Charts    │  │ • Main      │  │ • Tailwind │ │   │
│  │  │ • Settings  │  │ • Tables    │  │ • Auth      │  │ • CSS Vars │ │   │
│  │  │ • Analytics │  │ • Forms     │  │ • Empty     │  │ • Themes   │ │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                        │                                    │
│  ┌─────────────────────────────────────▼───────────────────────────────┐   │
│  │                          STATE MANAGEMENT                            │   │
│  │                                                                      │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │   │
│  │  │    Zustand      │  │   React Query   │  │     Context         │ │   │
│  │  │  (Client State) │  │  (Server State) │  │   (Theme, Auth)     │ │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                        │                                    │
│  ┌─────────────────────────────────────▼───────────────────────────────┐   │
│  │                          DATA LAYER                                  │   │
│  │                                                                      │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │   │
│  │  │   API Client    │  │   WebSocket     │  │   GraphQL Client    │ │   │
│  │  │   (REST)        │  │   (Real-time)   │  │   (Optional)        │ │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────┘ │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Technology Stack

### 1.1 Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.x | UI library |
| **Next.js** | 14.x | Framework (App Router) |
| **TypeScript** | 5.x | Type safety |
| **Tailwind CSS** | 3.x | Styling |
| **shadcn/ui** | Latest | Component library base |
| **Zustand** | 4.x | Client state management |
| **TanStack Query** | 5.x | Server state management |
| **Recharts** | 2.x | Data visualization |
| **React Hook Form** | 7.x | Form management |
| **Zod** | 3.x | Schema validation |

### 1.2 Development Tools

| Tool | Purpose |
|------|---------|
| **ESLint** | Code linting |
| **Prettier** | Code formatting |
| **Vitest** | Unit testing |
| **Playwright** | E2E testing |
| **Storybook** | Component development |
| **Bundle Analyzer** | Bundle optimization |

---

## 2. Project Structure

### 2.1 Directory Layout

```
src/
├── app/                        # Next.js App Router
│   ├── (auth)/                 # Auth route group
│   │   ├── login/
│   │   ├── signup/
│   │   └── layout.tsx
│   ├── (dashboard)/            # Dashboard route group
│   │   ├── dashboard/
│   │   ├── projects/
│   │   ├── analytics/
│   │   ├── mcp/
│   │   ├── settings/
│   │   └── layout.tsx
│   ├── api/                    # API routes
│   │   └── webhooks/
│   ├── layout.tsx              # Root layout
│   ├── page.tsx                # Landing page
│   └── globals.css
│
├── components/                  # React components
│   ├── ui/                     # Base UI components (shadcn)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── dialog.tsx
│   │   └── ...
│   ├── charts/                 # Data visualization
│   │   ├── usage-chart.tsx
│   │   ├── cost-chart.tsx
│   │   └── ...
│   ├── forms/                  # Form components
│   │   ├── project-form.tsx
│   │   ├── policy-form.tsx
│   │   └── ...
│   ├── layouts/                # Layout components
│   │   ├── dashboard-layout.tsx
│   │   ├── sidebar.tsx
│   │   └── header.tsx
│   └── features/               # Feature-specific components
│       ├── projects/
│       ├── analytics/
│       ├── mcp/
│       └── settings/
│
├── hooks/                       # Custom React hooks
│   ├── use-auth.ts
│   ├── use-organization.ts
│   ├── use-projects.ts
│   └── use-websocket.ts
│
├── lib/                         # Utilities and configs
│   ├── api/                    # API client
│   │   ├── client.ts
│   │   ├── organizations.ts
│   │   ├── projects.ts
│   │   └── analytics.ts
│   ├── utils.ts                # Utility functions
│   ├── constants.ts            # App constants
│   └── validations.ts          # Zod schemas
│
├── stores/                      # Zustand stores
│   ├── auth-store.ts
│   ├── ui-store.ts
│   └── preferences-store.ts
│
├── types/                       # TypeScript types
│   ├── api.ts
│   ├── models.ts
│   └── index.ts
│
└── styles/                      # Additional styles
    ├── themes/
    └── animations.css
```

### 2.2 Feature-Based Organization

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE MODULE STRUCTURE                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  components/features/projects/                                             │
│  ├── components/                # Feature-specific components              │
│  │   ├── project-card.tsx                                                 │
│  │   ├── project-list.tsx                                                 │
│  │   └── project-settings.tsx                                             │
│  ├── hooks/                     # Feature-specific hooks                   │
│  │   ├── use-project.ts                                                   │
│  │   └── use-project-metrics.ts                                           │
│  ├── api/                       # Feature API functions                    │
│  │   └── projects-api.ts                                                  │
│  └── index.ts                   # Public exports                           │
│                                                                             │
│  BENEFITS:                                                                 │
│  • Co-located code for better maintainability                             │
│  • Clear ownership boundaries                                              │
│  • Easier code splitting                                                   │
│  • Simplified imports                                                      │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Component Architecture

### 3.1 Component Hierarchy

```
┌────────────────────────────────────────────────────────────────────────────┐
│                      COMPONENT HIERARCHY                                    │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  LAYER 1: BASE UI (shadcn/ui)                                              │
│  ─────────────────────────────                                             │
│  Atomic, unstyled components with Tailwind                                 │
│                                                                             │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐         │
│  │Button│ │Input │ │Select│ │Dialog│ │Table │ │Card  │ │Badge │         │
│  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘         │
│                                                                             │
│  LAYER 2: COMPOSITE COMPONENTS                                             │
│  ─────────────────────────────                                             │
│  Composed from base UI, domain-aware                                       │
│                                                                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ DataTable    │ │ FormField    │ │ SearchInput  │ │ Pagination   │     │
│  │ with sorting │ │ with label   │ │ with debounce│ │ with routing │     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘     │
│                                                                             │
│  LAYER 3: FEATURE COMPONENTS                                               │
│  ───────────────────────────                                               │
│  Business logic, API integration                                           │
│                                                                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ UsageChart   │ │ ProjectCard  │ │ MCPServerList│ │ PolicyEditor │     │
│  │              │ │              │ │              │ │              │     │
│  │ • Data fetch │ │ • Click hdlr │ │ • Real-time  │ │ • Validation │     │
│  │ • Transform  │ │ • Navigation │ │ • Filtering  │ │ • Submit     │     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘     │
│                                                                             │
│  LAYER 4: PAGE COMPONENTS                                                  │
│  ─────────────────────────                                                 │
│  Full pages, layout composition                                            │
│                                                                             │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ Dashboard    │ │ Projects     │ │ Analytics    │ │ Settings     │     │
│  │ Page         │ │ Page         │ │ Page         │ │ Page         │     │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘     │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Component Patterns

```typescript
// 1. Base Component Pattern (shadcn style)
// components/ui/button.tsx

import * as React from 'react';
import { Slot } from '@radix-ui/react-slot';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils';

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : 'button';
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = 'Button';

export { Button, buttonVariants };
```

```typescript
// 2. Feature Component Pattern
// components/features/projects/project-card.tsx

'use client';

import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { MoreHorizontal, Activity } from 'lucide-react';
import { formatCurrency } from '@/lib/utils';
import type { Project } from '@/types';

interface ProjectCardProps {
  project: Project;
  onEdit?: (project: Project) => void;
  onDelete?: (project: Project) => void;
}

export function ProjectCard({ project, onEdit, onDelete }: ProjectCardProps) {
  const [isHovered, setIsHovered] = useState(false);

  return (
    <Card
      className="relative transition-shadow hover:shadow-md"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <CardHeader className="flex flex-row items-center justify-between pb-2">
        <CardTitle className="text-sm font-medium">{project.name}</CardTitle>
        <Badge variant={project.status === 'active' ? 'default' : 'secondary'}>
          {project.status}
        </Badge>
      </CardHeader>
      <CardContent>
        <div className="flex items-center space-x-4 text-sm text-muted-foreground">
          <div className="flex items-center">
            <Activity className="mr-1 h-3 w-3" />
            {project.usage?.requestsToday?.toLocaleString() ?? 0} requests
          </div>
          <div>
            {formatCurrency(project.usage?.costToday ?? 0)} today
          </div>
        </div>
        {isHovered && (
          <div className="absolute right-2 top-2">
            <Button variant="ghost" size="icon">
              <MoreHorizontal className="h-4 w-4" />
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
```

```typescript
// 3. Page Component Pattern
// app/(dashboard)/projects/page.tsx

import { Suspense } from 'react';
import { Metadata } from 'next';
import { ProjectList } from '@/components/features/projects';
import { ProjectListSkeleton } from '@/components/features/projects/skeletons';
import { CreateProjectButton } from '@/components/features/projects';

export const metadata: Metadata = {
  title: 'Projects | MindWeave',
  description: 'Manage your AI projects',
};

export default function ProjectsPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Projects</h1>
          <p className="text-muted-foreground">
            Manage your Claude AI projects and monitor usage
          </p>
        </div>
        <CreateProjectButton />
      </div>

      <Suspense fallback={<ProjectListSkeleton />}>
        <ProjectList />
      </Suspense>
    </div>
  );
}
```

---

## 4. State Management

### 4.1 State Categories

```
┌────────────────────────────────────────────────────────────────────────────┐
│                       STATE MANAGEMENT STRATEGY                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     STATE CATEGORIES                                 │   │
│  │                                                                      │   │
│  │  SERVER STATE              CLIENT STATE           UI STATE          │   │
│  │  (TanStack Query)          (Zustand)              (React useState)  │   │
│  │                                                                      │   │
│  │  • API data                • User preferences     • Modal open      │   │
│  │  • Cache management        • Auth state           • Tab selection   │   │
│  │  • Background sync         • Draft forms          • Hover states    │   │
│  │  • Optimistic updates      • Feature flags        • Form values     │   │
│  │  • Infinite queries        • Theme settings       • Local filters   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  DECISION TREE:                                                            │
│  ──────────────                                                            │
│                                                                             │
│         Is the state from an API?                                          │
│              │                                                              │
│         ┌────┴────┐                                                        │
│        Yes        No                                                       │
│         │          │                                                        │
│         ▼          │    Does it need to persist across sessions?           │
│   TanStack Query   │              │                                        │
│                    │         ┌────┴────┐                                   │
│                    │        Yes        No                                  │
│                    │         │          │                                   │
│                    │         ▼          │    Shared across components?     │
│                    │      Zustand       │              │                   │
│                    │   + localStorage   │         ┌────┴────┐              │
│                    │                    │        Yes        No             │
│                    │                    │         │          │              │
│                    │                    │         ▼          ▼              │
│                    │                    │      Zustand   useState           │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Server State (TanStack Query)

```typescript
// lib/api/organizations.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from './client';
import type { Organization, CreateOrganizationInput } from '@/types';

// Query keys factory
export const organizationKeys = {
  all: ['organizations'] as const,
  lists: () => [...organizationKeys.all, 'list'] as const,
  list: (filters: Record<string, unknown>) =>
    [...organizationKeys.lists(), filters] as const,
  details: () => [...organizationKeys.all, 'detail'] as const,
  detail: (id: string) => [...organizationKeys.details(), id] as const,
};

// Fetch organizations
export function useOrganizations(filters?: { status?: string }) {
  return useQuery({
    queryKey: organizationKeys.list(filters ?? {}),
    queryFn: () => apiClient.get<Organization[]>('/organizations', { params: filters }),
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
}

// Fetch single organization
export function useOrganization(id: string) {
  return useQuery({
    queryKey: organizationKeys.detail(id),
    queryFn: () => apiClient.get<Organization>(`/organizations/${id}`),
    enabled: !!id,
  });
}

// Create organization mutation
export function useCreateOrganization() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (input: CreateOrganizationInput) =>
      apiClient.post<Organization>('/organizations', input),
    onSuccess: () => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: organizationKeys.lists() });
    },
  });
}

// Update organization with optimistic update
export function useUpdateOrganization() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<Organization> }) =>
      apiClient.patch<Organization>(`/organizations/${id}`, data),
    onMutate: async ({ id, data }) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: organizationKeys.detail(id) });

      // Snapshot previous value
      const previousOrg = queryClient.getQueryData<Organization>(
        organizationKeys.detail(id)
      );

      // Optimistically update
      if (previousOrg) {
        queryClient.setQueryData(organizationKeys.detail(id), {
          ...previousOrg,
          ...data,
        });
      }

      return { previousOrg };
    },
    onError: (err, { id }, context) => {
      // Rollback on error
      if (context?.previousOrg) {
        queryClient.setQueryData(organizationKeys.detail(id), context.previousOrg);
      }
    },
    onSettled: (data, err, { id }) => {
      // Refetch to ensure consistency
      queryClient.invalidateQueries({ queryKey: organizationKeys.detail(id) });
    },
  });
}
```

### 4.3 Client State (Zustand)

```typescript
// stores/auth-store.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import type { User, Organization } from '@/types';

interface AuthState {
  // State
  user: User | null;
  organization: Organization | null;
  isAuthenticated: boolean;

  // Actions
  setUser: (user: User | null) => void;
  setOrganization: (org: Organization | null) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      // Initial state
      user: null,
      organization: null,
      isAuthenticated: false,

      // Actions
      setUser: (user) =>
        set({
          user,
          isAuthenticated: !!user,
        }),

      setOrganization: (organization) =>
        set({ organization }),

      logout: () =>
        set({
          user: null,
          organization: null,
          isAuthenticated: false,
        }),
    }),
    {
      name: 'mindweave-auth',
      partialize: (state) => ({
        // Only persist these fields
        user: state.user,
        organization: state.organization,
      }),
    }
  )
);

// stores/ui-store.ts
import { create } from 'zustand';

interface UIState {
  // Sidebar
  sidebarOpen: boolean;
  toggleSidebar: () => void;

  // Command palette
  commandPaletteOpen: boolean;
  openCommandPalette: () => void;
  closeCommandPalette: () => void;

  // Notifications
  notificationCount: number;
  incrementNotifications: () => void;
  clearNotifications: () => void;
}

export const useUIStore = create<UIState>((set) => ({
  // Sidebar
  sidebarOpen: true,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),

  // Command palette
  commandPaletteOpen: false,
  openCommandPalette: () => set({ commandPaletteOpen: true }),
  closeCommandPalette: () => set({ commandPaletteOpen: false }),

  // Notifications
  notificationCount: 0,
  incrementNotifications: () =>
    set((state) => ({ notificationCount: state.notificationCount + 1 })),
  clearNotifications: () => set({ notificationCount: 0 }),
}));
```

---

## 5. Routing and Navigation

### 5.1 Route Structure

```
┌────────────────────────────────────────────────────────────────────────────┐
│                         ROUTE STRUCTURE                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PUBLIC ROUTES (No auth required)                                          │
│  ──────────────────────────────────                                        │
│                                                                             │
│  /                        Landing page                                     │
│  /login                   Login page                                       │
│  /signup                  Registration                                     │
│  /forgot-password         Password reset request                          │
│  /reset-password          Password reset form                             │
│  /verify-email            Email verification                              │
│  /docs                    Documentation (marketing)                       │
│  /pricing                 Pricing page                                    │
│                                                                             │
│  PROTECTED ROUTES (Auth required)                                          │
│  ─────────────────────────────────                                         │
│                                                                             │
│  /dashboard               Main dashboard                                   │
│  /projects                Project list                                    │
│  /projects/:id            Project details                                 │
│  /projects/:id/settings   Project settings                                │
│  /analytics               Usage analytics                                 │
│  /analytics/reports       Detailed reports                                │
│  /mcp                     MCP registry                                    │
│  /mcp/:id                 MCP server details                              │
│  /policies                Governance policies                             │
│  /policies/:id            Policy details                                  │
│  /team                    Team management                                 │
│  /settings                Account settings                                │
│  /settings/billing        Billing settings                                │
│  /settings/security       Security settings                               │
│  /settings/api-keys       API key management                              │
│                                                                             │
│  ADMIN ROUTES (Admin role required)                                        │
│  ───────────────────────────────────                                       │
│                                                                             │
│  /admin                   Admin dashboard                                 │
│  /admin/organizations     All organizations                               │
│  /admin/audit             Audit logs                                      │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Layout Implementation

```typescript
// app/(dashboard)/layout.tsx
import { redirect } from 'next/navigation';
import { getServerSession } from '@/lib/auth';
import { DashboardLayout } from '@/components/layouts/dashboard-layout';
import { Sidebar } from '@/components/layouts/sidebar';
import { Header } from '@/components/layouts/header';

export default async function DashboardRootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const session = await getServerSession();

  if (!session) {
    redirect('/login');
  }

  return (
    <DashboardLayout>
      <Sidebar />
      <div className="flex flex-1 flex-col">
        <Header user={session.user} />
        <main className="flex-1 overflow-auto p-6">{children}</main>
      </div>
    </DashboardLayout>
  );
}

// components/layouts/sidebar.tsx
'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import {
  LayoutDashboard,
  FolderKanban,
  BarChart3,
  Server,
  Shield,
  Users,
  Settings,
} from 'lucide-react';

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Projects', href: '/projects', icon: FolderKanban },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
  { name: 'MCP Registry', href: '/mcp', icon: Server },
  { name: 'Policies', href: '/policies', icon: Shield },
  { name: 'Team', href: '/team', icon: Users },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="flex h-full w-64 flex-col border-r bg-background">
      <div className="flex h-16 items-center border-b px-6">
        <Link href="/dashboard" className="flex items-center space-x-2">
          <span className="text-xl font-bold">MindWeave</span>
        </Link>
      </div>
      <nav className="flex-1 space-y-1 p-4">
        {navigation.map((item) => {
          const isActive = pathname.startsWith(item.href);
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                'flex items-center space-x-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors',
                isActive
                  ? 'bg-primary text-primary-foreground'
                  : 'text-muted-foreground hover:bg-accent hover:text-accent-foreground'
              )}
            >
              <item.icon className="h-5 w-5" />
              <span>{item.name}</span>
            </Link>
          );
        })}
      </nav>
      <div className="border-t p-4">
        <Link
          href="/settings"
          className={cn(
            'flex items-center space-x-3 rounded-lg px-3 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-accent hover:text-accent-foreground',
            pathname.startsWith('/settings') && 'bg-accent text-accent-foreground'
          )}
        >
          <Settings className="h-5 w-5" />
          <span>Settings</span>
        </Link>
      </div>
    </aside>
  );
}
```

---

## 6. Data Visualization

### 6.1 Chart Components

```typescript
// components/charts/usage-chart.tsx
'use client';

import { useMemo } from 'react';
import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { formatNumber, formatDate } from '@/lib/utils';

interface UsageDataPoint {
  timestamp: string;
  tokens: number;
  cost: number;
}

interface UsageChartProps {
  data: UsageDataPoint[];
  title?: string;
  metric?: 'tokens' | 'cost';
}

export function UsageChart({
  data,
  title = 'Usage Over Time',
  metric = 'tokens',
}: UsageChartProps) {
  const chartData = useMemo(() => {
    return data.map((point) => ({
      ...point,
      date: formatDate(point.timestamp, 'MMM dd'),
      value: metric === 'tokens' ? point.tokens : point.cost,
    }));
  }, [data, metric]);

  const formatValue = (value: number) => {
    if (metric === 'cost') {
      return `$${value.toFixed(2)}`;
    }
    return formatNumber(value);
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="h-[300px]">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={chartData}>
              <defs>
                <linearGradient id="colorValue" x1="0" y1="0" x2="0" y2="1">
                  <stop
                    offset="5%"
                    stopColor="hsl(var(--primary))"
                    stopOpacity={0.3}
                  />
                  <stop
                    offset="95%"
                    stopColor="hsl(var(--primary))"
                    stopOpacity={0}
                  />
                </linearGradient>
              </defs>
              <CartesianGrid
                strokeDasharray="3 3"
                className="stroke-muted"
              />
              <XAxis
                dataKey="date"
                tick={{ fontSize: 12 }}
                tickLine={false}
                axisLine={false}
                className="text-muted-foreground"
              />
              <YAxis
                tickFormatter={formatValue}
                tick={{ fontSize: 12 }}
                tickLine={false}
                axisLine={false}
                className="text-muted-foreground"
              />
              <Tooltip
                content={({ active, payload }) => {
                  if (!active || !payload?.length) return null;
                  const data = payload[0].payload;
                  return (
                    <div className="rounded-lg border bg-background p-2 shadow-sm">
                      <div className="text-sm font-medium">{data.date}</div>
                      <div className="text-sm text-muted-foreground">
                        {formatValue(data.value)}
                      </div>
                    </div>
                  );
                }}
              />
              <Area
                type="monotone"
                dataKey="value"
                stroke="hsl(var(--primary))"
                fill="url(#colorValue)"
                strokeWidth={2}
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </CardContent>
    </Card>
  );
}
```

### 6.2 Dashboard Widgets

```typescript
// components/features/dashboard/stats-cards.tsx
'use client';

import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ArrowUpIcon, ArrowDownIcon } from 'lucide-react';
import { cn, formatNumber, formatCurrency } from '@/lib/utils';

interface StatCardProps {
  title: string;
  value: string | number;
  change?: number;
  changeLabel?: string;
  icon?: React.ComponentType<{ className?: string }>;
  format?: 'number' | 'currency' | 'none';
}

export function StatCard({
  title,
  value,
  change,
  changeLabel = 'from last period',
  icon: Icon,
  format = 'number',
}: StatCardProps) {
  const formattedValue = useMemo(() => {
    if (format === 'currency') return formatCurrency(value as number);
    if (format === 'number') return formatNumber(value as number);
    return value;
  }, [value, format]);

  const isPositive = change && change > 0;
  const isNegative = change && change < 0;

  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium text-muted-foreground">
          {title}
        </CardTitle>
        {Icon && <Icon className="h-4 w-4 text-muted-foreground" />}
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{formattedValue}</div>
        {change !== undefined && (
          <p className="mt-1 flex items-center text-xs text-muted-foreground">
            {isPositive && (
              <ArrowUpIcon className="mr-1 h-3 w-3 text-green-500" />
            )}
            {isNegative && (
              <ArrowDownIcon className="mr-1 h-3 w-3 text-red-500" />
            )}
            <span
              className={cn(
                isPositive && 'text-green-500',
                isNegative && 'text-red-500'
              )}
            >
              {Math.abs(change)}%
            </span>
            <span className="ml-1">{changeLabel}</span>
          </p>
        )}
      </CardContent>
    </Card>
  );
}

// Usage in dashboard
export function DashboardStats({ stats }) {
  return (
    <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      <StatCard
        title="Total Tokens"
        value={stats.totalTokens}
        change={stats.tokensChange}
        format="number"
      />
      <StatCard
        title="Total Cost"
        value={stats.totalCost}
        change={stats.costChange}
        format="currency"
      />
      <StatCard
        title="API Requests"
        value={stats.totalRequests}
        change={stats.requestsChange}
        format="number"
      />
      <StatCard
        title="Active Users"
        value={stats.activeUsers}
        change={stats.usersChange}
        format="number"
      />
    </div>
  );
}
```

---

## 7. Forms and Validation

### 7.1 Form Pattern with React Hook Form + Zod

```typescript
// lib/validations/project.ts
import { z } from 'zod';

export const projectFormSchema = z.object({
  name: z
    .string()
    .min(1, 'Name is required')
    .max(100, 'Name must be less than 100 characters'),
  slug: z
    .string()
    .min(1, 'Slug is required')
    .regex(/^[a-z0-9-]+$/, 'Slug can only contain lowercase letters, numbers, and hyphens'),
  description: z.string().max(500).optional(),
  settings: z.object({
    allowedModels: z.array(z.string()).min(1, 'Select at least one model'),
    defaultModel: z.string().optional(),
    mcpAutoApprove: z.boolean().default(false),
  }),
  quotas: z.object({
    maxTokensPerDay: z.number().positive().nullable(),
    maxCostPerDayUsd: z.number().positive().nullable(),
    maxRequestsPerMinute: z.number().positive().default(100),
  }),
});

export type ProjectFormValues = z.infer<typeof projectFormSchema>;

// components/forms/project-form.tsx
'use client';

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Switch } from '@/components/ui/switch';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { projectFormSchema, type ProjectFormValues } from '@/lib/validations/project';
import { useCreateProject, useUpdateProject } from '@/hooks/use-projects';
import { CLAUDE_MODELS } from '@/lib/constants';

interface ProjectFormProps {
  initialData?: Partial<ProjectFormValues>;
  projectId?: string;
  onSuccess?: () => void;
}

export function ProjectForm({ initialData, projectId, onSuccess }: ProjectFormProps) {
  const createProject = useCreateProject();
  const updateProject = useUpdateProject();
  const isEditing = !!projectId;

  const form = useForm<ProjectFormValues>({
    resolver: zodResolver(projectFormSchema),
    defaultValues: {
      name: '',
      slug: '',
      description: '',
      settings: {
        allowedModels: ['claude-3-sonnet'],
        defaultModel: 'claude-3-sonnet',
        mcpAutoApprove: false,
      },
      quotas: {
        maxTokensPerDay: null,
        maxCostPerDayUsd: null,
        maxRequestsPerMinute: 100,
      },
      ...initialData,
    },
  });

  const onSubmit = async (values: ProjectFormValues) => {
    try {
      if (isEditing) {
        await updateProject.mutateAsync({ id: projectId, data: values });
      } else {
        await createProject.mutateAsync(values);
      }
      onSuccess?.();
    } catch (error) {
      // Error is handled by mutation
    }
  };

  // Auto-generate slug from name
  const handleNameChange = (name: string) => {
    if (!isEditing && !form.getValues('slug')) {
      const slug = name
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
      form.setValue('slug', slug);
    }
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <FormField
          control={form.control}
          name="name"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Project Name</FormLabel>
              <FormControl>
                <Input
                  placeholder="My AI Project"
                  {...field}
                  onChange={(e) => {
                    field.onChange(e);
                    handleNameChange(e.target.value);
                  }}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="slug"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Slug</FormLabel>
              <FormControl>
                <Input placeholder="my-ai-project" {...field} disabled={isEditing} />
              </FormControl>
              <FormDescription>
                Used in URLs and API requests
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="description"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Description (Optional)</FormLabel>
              <FormControl>
                <Textarea
                  placeholder="Describe your project..."
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="settings.defaultModel"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Default Model</FormLabel>
              <Select onValueChange={field.onChange} defaultValue={field.value}>
                <FormControl>
                  <SelectTrigger>
                    <SelectValue placeholder="Select a model" />
                  </SelectTrigger>
                </FormControl>
                <SelectContent>
                  {CLAUDE_MODELS.map((model) => (
                    <SelectItem key={model.id} value={model.id}>
                      {model.name}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <FormMessage />
            </FormItem>
          )}
        />

        <FormField
          control={form.control}
          name="settings.mcpAutoApprove"
          render={({ field }) => (
            <FormItem className="flex items-center justify-between rounded-lg border p-4">
              <div className="space-y-0.5">
                <FormLabel className="text-base">Auto-approve MCP Servers</FormLabel>
                <FormDescription>
                  Automatically approve new MCP server registrations
                </FormDescription>
              </div>
              <FormControl>
                <Switch checked={field.value} onCheckedChange={field.onChange} />
              </FormControl>
            </FormItem>
          )}
        />

        <Button
          type="submit"
          disabled={createProject.isPending || updateProject.isPending}
        >
          {isEditing ? 'Update Project' : 'Create Project'}
        </Button>
      </form>
    </Form>
  );
}
```

---

## 8. Real-time Updates

### 8.1 WebSocket Integration

```typescript
// hooks/use-websocket.ts
import { useEffect, useRef, useCallback } from 'react';
import { useAuthStore } from '@/stores/auth-store';

interface WebSocketMessage {
  type: string;
  channel: string;
  data: unknown;
  timestamp: string;
}

interface UseWebSocketOptions {
  channels: string[];
  onMessage: (message: WebSocketMessage) => void;
  onError?: (error: Event) => void;
  reconnect?: boolean;
}

export function useWebSocket({
  channels,
  onMessage,
  onError,
  reconnect = true,
}: UseWebSocketOptions) {
  const wsRef = useRef<WebSocket | null>(null);
  const reconnectTimeoutRef = useRef<NodeJS.Timeout>();
  const { user } = useAuthStore();

  const connect = useCallback(() => {
    if (!user) return;

    const token = localStorage.getItem('access_token');
    const ws = new WebSocket(
      `${process.env.NEXT_PUBLIC_WS_URL}?token=${token}`
    );

    ws.onopen = () => {
      // Subscribe to channels
      channels.forEach((channel) => {
        ws.send(JSON.stringify({ type: 'subscribe', channel }));
      });
    };

    ws.onmessage = (event) => {
      const message = JSON.parse(event.data) as WebSocketMessage;

      if (message.type === 'ping') {
        ws.send(JSON.stringify({ type: 'pong' }));
        return;
      }

      onMessage(message);
    };

    ws.onerror = (error) => {
      onError?.(error);
    };

    ws.onclose = () => {
      if (reconnect) {
        reconnectTimeoutRef.current = setTimeout(() => {
          connect();
        }, 5000);
      }
    };

    wsRef.current = ws;
  }, [channels, onMessage, onError, reconnect, user]);

  useEffect(() => {
    connect();

    return () => {
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
      wsRef.current?.close();
    };
  }, [connect]);

  const send = useCallback((data: unknown) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify(data));
    }
  }, []);

  return { send };
}

// Usage example
// components/features/dashboard/realtime-usage.tsx
'use client';

import { useState, useCallback } from 'react';
import { useWebSocket } from '@/hooks/use-websocket';
import { useAuthStore } from '@/stores/auth-store';

export function RealtimeUsage() {
  const { organization } = useAuthStore();
  const [usage, setUsage] = useState({ tokens: 0, cost: 0 });

  const handleMessage = useCallback((message) => {
    if (message.type === 'usage.update') {
      setUsage((prev) => ({
        tokens: prev.tokens + message.data.tokens,
        cost: prev.cost + message.data.cost_usd,
      }));
    }
  }, []);

  useWebSocket({
    channels: [`org:${organization?.id}:usage`],
    onMessage: handleMessage,
  });

  return (
    <div className="flex items-center space-x-4">
      <div className="animate-pulse h-2 w-2 rounded-full bg-green-500" />
      <span className="text-sm text-muted-foreground">
        Live: {usage.tokens.toLocaleString()} tokens (${usage.cost.toFixed(2)})
      </span>
    </div>
  );
}
```

---

## 9. Performance Optimization

### 9.1 Optimization Techniques

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    PERFORMANCE OPTIMIZATION                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  CODE SPLITTING                                                            │
│  ──────────────                                                            │
│  • Route-based: Next.js automatic                                          │
│  • Component-based: dynamic imports                                        │
│  • Feature-based: lazy loading                                             │
│                                                                             │
│  CACHING                                                                   │
│  ───────                                                                   │
│  • TanStack Query staleTime/cacheTime                                     │
│  • Next.js ISR for static pages                                           │
│  • Browser cache headers                                                   │
│                                                                             │
│  RENDERING                                                                 │
│  ─────────                                                                 │
│  • Server Components (default)                                             │
│  • Client Components (interactivity)                                       │
│  • Streaming with Suspense                                                 │
│                                                                             │
│  BUNDLE                                                                    │
│  ──────                                                                    │
│  • Tree shaking                                                            │
│  • Import cost awareness                                                   │
│  • Bundle analyzer monitoring                                              │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### 9.2 Lazy Loading Pattern

```typescript
// Dynamic imports for heavy components
import dynamic from 'next/dynamic';

// Lazy load chart components
const UsageChart = dynamic(
  () => import('@/components/charts/usage-chart').then(mod => mod.UsageChart),
  {
    loading: () => <ChartSkeleton />,
    ssr: false, // Charts don't need SSR
  }
);

// Lazy load modals
const ProjectModal = dynamic(
  () => import('@/components/features/projects/project-modal'),
  {
    loading: () => null,
  }
);

// Route-based code splitting (automatic with Next.js App Router)
// Each route in app/ is automatically code-split
```

---

## 10. Testing Strategy

### 10.1 Testing Pyramid

| Type | Tools | Coverage Target |
|------|-------|-----------------|
| Unit | Vitest | 80% |
| Integration | Testing Library | Key flows |
| E2E | Playwright | Critical paths |
| Visual | Storybook | Components |

### 10.2 Test Examples

```typescript
// Component test
// __tests__/components/project-card.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { ProjectCard } from '@/components/features/projects/project-card';

describe('ProjectCard', () => {
  const mockProject = {
    id: '1',
    name: 'Test Project',
    status: 'active',
    usage: {
      requestsToday: 1000,
      costToday: 5.50,
    },
  };

  it('renders project name', () => {
    render(<ProjectCard project={mockProject} />);
    expect(screen.getByText('Test Project')).toBeInTheDocument();
  });

  it('shows active badge', () => {
    render(<ProjectCard project={mockProject} />);
    expect(screen.getByText('active')).toBeInTheDocument();
  });

  it('displays usage stats', () => {
    render(<ProjectCard project={mockProject} />);
    expect(screen.getByText('1,000 requests')).toBeInTheDocument();
    expect(screen.getByText('$5.50 today')).toBeInTheDocument();
  });
});

// E2E test
// e2e/dashboard.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    // Login
    await page.goto('/login');
    await page.fill('[name=email]', 'test@example.com');
    await page.fill('[name=password]', 'password');
    await page.click('[type=submit]');
    await page.waitForURL('/dashboard');
  });

  test('displays usage stats', async ({ page }) => {
    await expect(page.locator('[data-testid=total-tokens]')).toBeVisible();
    await expect(page.locator('[data-testid=total-cost]')).toBeVisible();
  });

  test('navigates to projects', async ({ page }) => {
    await page.click('[href="/projects"]');
    await expect(page).toHaveURL('/projects');
    await expect(page.locator('h1')).toHaveText('Projects');
  });
});
```

---

## Related Documents

| Document | Description |
|----------|-------------|
| [SYSTEM-ARCHITECTURE.md](./SYSTEM-ARCHITECTURE.md) | System design |
| [API-SPECIFICATIONS.md](./API-SPECIFICATIONS.md) | API contracts |
| [DESIGN-SYSTEM.md](../02-product/design/DESIGN-SYSTEM.md) | Design system |
| [COMPONENT-LIBRARY.md](../02-product/design/COMPONENT-LIBRARY.md) | Components |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-01-15 | Engineering | Initial frontend architecture |
