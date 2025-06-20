# System Patterns: Django Order Management System

## System Architecture

The application follows a standard Django architecture with a focus on simplicity and maintainability:

### Overall Structure
- **Single-app Architecture**: Using one main Django app (`core_app`) to avoid premature boundaries and keep the codebase focused
- **Server-side Rendering**: Primary approach is server-side HTML with minimal sprinkles of HTMX (Alpine.js or vanilla javascript if truly neccessary)
- **WSGI Deployment**: Synchronous processing for simplicity in debugging and deployment

### Data Flow
```
Browser <-> Django Views <-> Forms <-> Models <-> Database
```

### Request Lifecycle
1. URL routing directs requests to appropriate views
2. Views handle business logic and call appropriate services when needed
3. Forms validate user input
4. Models persist data and enforce database-level rules
5. Templates render the HTML response

## Key Technical Decisions

### Data Model Strategy
- **Multi-tenancy**: Every relevant model will have a FK to `Company` model
- **ID Strategy**: Using `UUIDField(primary_key=True)` for non-sequential, unguessable IDs
- **Data Isolation**: Manager filters to enforce row-level security by company

### URL Strategy
- **Object-based URLs**: `/objects/<uuid>/` namespaced under `core:`
- **Reverse-friendly**: All URLs use Django's naming conventions for easy `reverse()` lookups

### View Strategy
- **Class-based Views**: Try leverage Django's built-in CBVs for CRUD operations (short and battle-tested)
- **Mixins for Cross-cutting Concerns**: Custom mixins (e.g., `CompanyRestrictedMixin`) for tenant scoping
- **Authorization Approach**: Standard Django auth mixins (`LoginRequiredMixin`, `PermissionRequiredMixin`)

### Form Strategy
- **ModelForms**: Direct mapping to models for validation consistency
- **Validation Hierarchy**: 
  1. Model `clean()` for DB safety
  2. Form `clean()` for UX-level validation

## Design Patterns

### Multi-tenancy Pattern
```python
# Example of CompanyRestrictedMixin
class CompanyRestrictedMixin:
    def get_queryset(self):
        return super().get_queryset().filter(company=self.request.user.company)
```

### Service Layer Pattern
```
# For complex operations spanning multiple models
services/
  ├── order_services.py
  ├── resource_services.py
  └── financial_services.py
```

### Layer Responsibilities

| Layer | Responsibility | Example |
|-------|----------------|---------|
| Models | Data structure, validation, business rules | Resource model with categorization logic |
| Views | Request handling, orchestration | OrderCreateView handling form submission |
| Forms | Input validation, data preparation | OrderForm validating input constraints |
| Services | Complex workflows, cross-model operations | OrderService for order creation workflow |
| Templates | Presentation logic | order_detail.html showing order items |

## Component Relationships

### Core Domain Models
```
Company
 ├─ User (FK -> Company)
 ├─ Resource (FK -> Company)
 │   ├─ Type (equipment/personnel)
 │   └─ Category (ROV/Survey)
 └─ Order (FK -> Company)
     └─ OrderItem (FK -> Order, FK -> Resource)
         ├─ Planned Cost
         └─ Actual Cost
```

### Authentication Flow
```
Django Auth → User Model → Company Association → Row-level Filtering
```

### Order Processing Flow
```
Create Order → Add Order Items → Calculate Planned Costs → Track Actual Costs
```

## Critical Implementation Paths

### Row-Level Security Implementation
1. Custom User model with FK to Company
2. QuerySet filtering in views via CompanyRestrictedMixin
3. Permission checks for appropriate access levels

### Financial Tracking Implementation
1. Store planned costs at order creation
2. Update actual costs later (done manually by nexans user basedf on our invoices)
3. Calculate and display variances between planned and actual

### Resource Management Implementation
1. Resource categorization (ROV/Survey)
2. Custom defined ordering for ROV/Survey categories

