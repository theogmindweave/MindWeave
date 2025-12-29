# MindWeave Marketplace

Enterprise AI Usage Intelligence Platform - Claude Code Plugin Marketplace

## Overview

This is the official plugin marketplace for MindWeave, curating the best Claude Code plugins for enterprise AI usage analytics, APIR scoring, team intelligence, and code health monitoring.

## Installation

```bash
# Add the marketplace
/plugin marketplace add jivaunderworld/mindweave-marketplace

# Or from local path (for development)
/plugin marketplace add ./mindweave-marketplace
```

## Available Plugins

### Core Development

| Plugin | Description |
|--------|-------------|
| **ralph-wiggum** | Iterative development loops - continuous self-referential AI loops until task completion |
| **feature-dev** | Feature development workflow with exploration, architecture, and review agents |
| **plugin-dev** | Plugin development toolkit - scaffold, validate, and build plugins |
| **frontend-design** | Production-grade frontend interface development |

### Code Quality

| Plugin | Description |
|--------|-------------|
| **code-review** | Automated code review and quality analysis |
| **pr-review-toolkit** | Comprehensive pull request review and feedback |
| **security-guidance** | Security vulnerability detection and warnings |

### Workflow Automation

| Plugin | Description |
|--------|-------------|
| **hookify** | User-configurable hooks via YAML in .local.md files |
| **commit-commands** | Streamlined git workflow commands |

### Schema-First Development

| Plugin | Description |
|--------|-------------|
| **specforge** | OpenAPI + DB schema dual-spec development |
| **plugin-builder** | Interactive plugin scaffolding and validation |

## Plugin Categories

- `development-automation` - Automated development workflows
- `workflow-automation` - Custom hooks and automation
- `developer-tools` - Development productivity tools
- `code-quality` - Review and analysis tools
- `security` - Security scanning and guidance
- `frontend` - UI/UX development
- `git` - Git workflow automation

## For MindWeave Enterprise

This marketplace is optimized for teams using Claude Code for enterprise development with focus on:

- **APIR Scoring** - AI Performance, Insights, Risk scoring
- **Usage Analytics** - Track team Claude Code usage patterns
- **Code Health** - Security scanning and quality metrics
- **Compliance** - Enterprise governance and audit trails

## Adding Plugins

1. Fork this repository
2. Add your plugin to `./plugins/your-plugin/`
3. Update `marketplace.json` with your plugin entry
4. Submit a PR

## Structure

```
mindweave-marketplace/
├── .claude-plugin/
│   └── marketplace.json    # Marketplace manifest
├── plugins/                # Local plugins
│   └── mindweave-core/     # MindWeave core plugin (coming soon)
└── README.md
```

## License

MIT - Jiva Underworld ODI
