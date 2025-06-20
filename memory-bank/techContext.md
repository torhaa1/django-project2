# Technical Context: Django Order Management System

## Technologies Used

### Core Stack
- **Python 3.12**: Latest stable with security updates to 2028 and modern syntax support
- **Django 5.0.x**: Current stable release with active bug-fixes and clear documentation
- **SQLite**: Used for both development and production due to its simplicity and adequate performance for the expected load

### Frontend
- **Django Templates**: Standard template system for server-side rendering
- **Bootstrap 5**: Via CDN for responsive styling without a build step
- **HTMX**: Mainly simple HTMX with sprinkles of alpine.js or vanilla javascript where enhanced interactivity is needed

### Deployment
- **WSGI**: Using `waitress` as the application server
- **Nginx**: For TLS offload and static caching in production
- **WhiteNoise**: For serving static files efficiently without separate object storage

## Development Setup

### Configuration Management
- **Settings Structure**:
  - `settings/dev.py`: Development-specific settings
  - `settings/prod.py`: Production-specific settings
- **Environment Variables**: Using python-decouple with `.env` files
  - Keeps secrets (e.g., `SECRET_KEY`, DB credentials) outside of code

### Database
- **Engine**: SQLite for both development and production
- **Primary Keys**: Using UUIDs (`UUIDField(primary_key=True)`) for security
- **Migrations**: Maintain linear history, squash when reaching ~25 migrations

## Technical Constraints

### Performance Requirements
- **Concurrent Users**: System designed for ≤20 concurrent users
- **Response Time**: Pages should load in under 2 seconds
- **Database Size**: Expected to remain small enough for SQLite to handle efficiently

### Security Requirements
- **Authentication**: Initially Django's built-in system, with flexibility to migrate to Azure AD or SSO
- **Row-Level Security**: Implemented at the application level through query filtering
- **HTTPS**: All production traffic must use HTTPS
- **Password Policy**: Django's default PBKDF2 with enforced complexity via validators

### Maintainability Requirements
- **Code Complexity**: Views should be ≤20 lines of code when possible
- **Documentation**: Keep the well-structures memory bank updated and lean
- **Testing**: Pytest for unit and integration tests

## Dependencies

### Required Packages
- Django 5.0.x
- python-decouple (for environment variable management)
- crispy-forms-bootstrap5 (for form styling)
- django-filter (for easy filtering in list views)
- WhiteNoise (for static file serving)

### Development Packages
- pytest-django (for testing)
- factory_boy (for test data generation)

### Future Considerations
- django-axes (for login attempt throttling)
- Sentry (for error tracking)

## Tool Usage Patterns

### Database Access
- Use `.select_related('company')` to avoid N+1 queries
- Access company data through `request.user.company` in views
- Filter querysets using the `CompanyRestrictedMixin`

### Form Processing
```python
# Standard pattern for form processing in views
def form_valid(self, form):
    form.instance.company = self.request.user.company
    return super().form_valid(form)
```

### Authentication Flow
```python
# Login URL configuration
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'core:dashboard'
```

### Static File Management
```python
# Static file configuration
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Deployment Process
1. Collect static files with `python manage.py collectstatic`
2. Run migrations with `python manage.py migrate`
3. Start Waitress server
4. Configure Nginx as reverse proxy with HTTPS

## Development Workflow

### Local Development
1. Activate virtual environment
2. Run development server with `python manage.py runserver`
3. Access the application at `http://localhost:8000`

### Testing
1. Write tests using pytest fixtures and factories
2. Run tests with `pytest`
3. Aim for good coverage of models and views

### Deployment
1. Update requirements with pip-tools
2. Collect static files
3. Apply migrations
4. Restart application server
