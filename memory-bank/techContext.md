# Technical Context

### Core Stack
- **Python 3.12**: Latest stable with security updates to 2028 and modern syntax support
- **Django 5.0.x**: Current stable release with active bug-fixes and clear documentation
- **SQLite**: Used for both development and production due to its simplicity and adequate performance for the expected load

### Frontend
- **Django Templates**: Standard template system for server-side rendering
- **Bootstrap 5**: Via CDN for responsive styling without a build step
- **HTMX**: Mainly simple HTMX with sprinkles of alpine.js or vanilla javascript where enhanced interactivity is needed

## Configuration
- **Settings**: `settings/dev.py` & `settings/prod.py`
- **Secrets**: python-decouple with `.env` files
- **Database**: SQLite with UUID primary keys

## Constraints
- **Performance**: ≤20 concurrent users, <2s response time
- **Security**: Django auth (→ SSO later), app-level row filtering
- **Maintainability**: Views ≤20 LOC, clear documentation

## Dependencies
- **Core**: Django, python-decouple, crispy-forms-bootstrap5, django-filter, WhiteNoise
- **Dev**: pytest-django, factory_boy
- **Future**: django-axes, Sentry

## Key Patterns
- **DB Access**: Use `.select_related('company')`, filter by company
- **Form Processing**: Auto-assign company in `form_valid`
- **Auth**: Standard Django login/redirect URLs
- **Static Files**: WhiteNoise with compression

## Workflow
- **Development**: venv, runserver, localhost:8000
- **Testing**: pytest with fixtures and factories
- **Deployment**: collectstatic → migrate → waitress → nginx
