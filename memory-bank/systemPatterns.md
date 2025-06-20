# System Patterns

## Architecture
- **Single-app**: One `core_app` to avoid premature boundaries
- **Server-side Rendering**: HTML with minimal HTMX and only Alpine.js/vanilla javascript when truly needed
- **WSGI**: Synchronous for simple debugging/deployment

## Key Decisions
- **Multi-tenancy**: FK to `Company` on relevant models
- **IDs**: `UUIDField(primary_key=True)` for security
- **Security**: Row-level filtering by company
- **URLs**: `/objects/<uuid>/` under `core:` namespace
- **Views**: Django CBVs with custom mixins
- **Forms**: ModelForms with validation hierarchy (Model → Form)

## Core Patterns

### Multi-tenancy
```python
class CompanyRestrictedMixin:
    def get_queryset(self):
        return super().get_queryset().filter(company=self.request.user.company)
```

### Layer Responsibilities
- **Models**: Data structure, validation, business rules
- **Views**: Request handling, orchestration (≤20 LOC)
- **Forms**: Input validation, data preparation
- **Services**: Complex workflows across models
- **Templates**: Presentation only

## Domain Model
```
Company
 ├─ User (FK → Company)
 ├─ Resource (FK → Company)
 │   ├─ Type (equipment/personnel)
 │   └─ Category (ROV/Survey)
 └─ Order (FK → Company)
     └─ OrderItem (FK → Order, Resource)
         ├─ Planned Cost
         └─ Actual Cost
```

## Critical Paths
1. **Row-Level Security**: Custom User model → Company FK → QuerySet filtering
2. **Financial Tracking**: Store planned costs → Update actuals → Calculate variance
3. **Resource Management**: Categorization (ROV/Survey) → Custom ordering
