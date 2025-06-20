# Active Context

## Current Status
- Initial Django project setup complete
- Basic structure created
- Focus on Phase 1 foundation setup

## Decision Points
- Authentication approach (Django auth → potential Azure/SSO)
- Database schema for core models
- Row-level security implementation

## Technical Approach
- Single-app architecture (`core_app`)
- Server-side rendering with minimal JS
- Row-level security via query filtering
- SQLite for dev/prod

## Implementation Priorities
1. Custom user model with company association
2. Core models (Resource, Order, OrderItem)
3. Row-level security
4. Basic CRUD views
5. Bootstrap templates

## Code Standards
- Models: Business rules and DB invariants
- Views: Thin (≤20 LOC), use CBVs
- Forms: UI validation
- Services: Complex workflows
- Naming: PascalCase models, snake_case fields/functions
- Security: Env vars for secrets, UUIDs for PKs, company filtering

## Open Questions
- Resource categorization implementation
- Permission structure details

## Next Steps
1. Create `core_app`
2. Implement custom User model
3. Set up settings structure
4. Create Company model
5. Begin Resource model implementation
