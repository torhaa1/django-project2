# Active Context: Django Order Management System

## Current Work Focus

The project is in its initial setup phase. Django has been installed and the basic project structure has been created. The focus is now on completing the foundation setup according to Phase 1 of the project plan.

### Recent Changes
- Initial Django project setup completed
- Project configuration with default settings
- Django 5.0.x installed
- Memory Bank documentation created

### Current Decision Points
- Authentication approach (currently planning to start with Django's built-in auth with flexibility to migrate to company Azure or SSO later)
- Database schema design for the core models (Company, User, Resource, Order, OrderItem) (can probably bake Company into User)
- Implementation approach for row-level security

## Active Considerations

### Technical Approach
- Following the single-app architecture with `core_app` to avoid premature boundaries
- Using server-side rendering with minimal JavaScript (HTMX and Alpine.js only when necessary)
- Implementing row-level security at the application level through query filtering
- Using SQLite for both development and production due to simplicity and adequate performance for the expected load

### Design Patterns in Use
- Multi-tenancy with FK to Company model
- Class-based views with mixins for cross-cutting concerns
- Model-driven validation for business rules
- Service layer for complex operations

### Implementation Priorities
1. Custom user model with company association
2. Core models (Resource, Order, OrderItem)
3. Row-level security implementation
4. Basic CRUD views
5. Templates with Bootstrap 5

## Important Patterns and Preferences

### Code Organization
- Models should encapsulate business rules and DB invariants
- Views should be thin (≤20 LOC) and leverage CBVs when possible
- Forms handle UI-level validation
- Services handle complex workflows

### Naming Conventions
- PascalCase for model names
- snake_case for fields, functions, and variables
- Descriptive names that reflect business domain

### Security Practices
- All secrets in environment variables via python-decouple
- UUIDs for primary keys to avoid sequential ID exposure
- Company-based filtering for all querysets

## Project Insights and Learnings

### Key Insights
- The multi-tenant nature of the application requires careful consideration of data isolation
- The project aims to balance simplicity for novice developers with proper security practices
- The application will need to handle different pricing models (unit, time-based, lump sum)

### Open Questions
- How to best implement the resource categorization (ROV/Survey) in the models
- Detailed permission structure for different user types

## Next Steps

### Immediate Tasks
1. Create `core_app` Django application
2. Implement custom user model with company association
3. Set up settings structure with dev/prod separation
4. Implement basic User/Company model
5. Begin implementation of Resource model with categorization

### Upcoming Milestones
- Complete data model implementation
- Implement row-level security
- Create basic CRUD views
- Set up authentication and permission system
- Implement financial tracking functionality
