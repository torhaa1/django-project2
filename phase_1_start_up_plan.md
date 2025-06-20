# Django CRUD Web App – **Phase 1: Start‑up Plan**

**Goal**
A functional, multi‑tenant CRUD MVP that a novice developer can run locally or on a small VPS. Focus on essentials: foundations, data model, core views, and baseline security. All advanced tooling and polish are deferred to **Phase 2**.

---

## 1 · Foundations

| Choice | Value | Rationale |
| --- | --- | --- |
| **OS** | Windows (dev & prod) | Ensures compatibility and consistent behavior across environments. |
| **Python** | 3.12 | Latest stable with security updates to 2028 and modern syntax while broadly supported. |
| **Django** | 5.0.x | Current stable release with active bug‑fixes and clear docs. |
| **Environment** | `python -m venv` + `pip‑tools` | Native, deterministic, zero lock‑file surprises. |
| **Settings layout** | `settings/dev.py` & `settings/prod.py`, loading environment variables via **python‑decouple** and `.env` files | Keep secrets (e.g. `SECRET_KEY`, DB credentials, API tokens) in `.env` files, never in code. |

## 2 · Architecture

| Decision | Rationale |
| --- | --- |
| **Single app `core_app`** | One clear namespace; avoids premature boundaries. |
| **Server‑side HTML + sprinkles of HTMX** | Simple request/response debug path; only add HTMX and Alpine.js or vanilla javascript if truly neccessary. |
| **No async** | WSGI keeps deployment & debugging trivial for ≤20 concurrent users. |
| **Logic placement** | Models enforce rules; views stay ≤20 LOC; escape‑hatch `services/` for workflows. |

## 3 · Database

| Choice | Value | Rationale |
| --- | --- | --- |
| **Engine** | SQLite (dev & prod) | Zero‑maintenance, file‑backup, fast enough for early traffic. |
| **PK** | `UUIDField(primary_key=True)` | Unguessable IDs; safe for external links. |
| **Multi‑tenancy** | FK → `Company` + default manager filters | Row isolation without DB‑level RLS. |
| **Migrations** | Linear; squash ~25 | Keeps history readable and CI quick. |

## 4 · URLs

| Pattern | Rationale |
| --- | --- |
| `/objects/<uuid>/` namespaced under `core:` | Reverse‑safe and hides sequential IDs. |

## 5 · Views

| Choice | Rationale |
| --- | --- |
| **Prefer Built‑in CBVs** (`ListView`, `DetailView`, `CreateView`, etc.) | CRUD in a handful of lines; inherits Django best‑practice behaviour; inline with lean, simple codebase. |
| **Project-specific mixins for cross-cutting concerns** | Write few small mixins to handle things like tenant scoping or automatic “owner/tenant” stamping; this removes repetitive code while staying explicit and easy to audit. |
| **Standard auth/permission mixins (LoginRequiredMixin, PermissionRequiredMixin, etc.)** | Add access control declaratively—plug-and-play security with zero bespoke logic. |

## 6 · Forms

| Decision | Rationale |
| --- | --- |
| `ModelForm` + **crispy‑forms‑bootstrap5** | One‑liner Bootstrap markup; no custom CSS. Short and functional. |
| **Validation ladder** | 1) Model `clean()` – DB safety. 2) Form `clean()` – UX rules. |

## 7 · Templates & Static Assets

| Choice | Value | Rationale |
| --- | --- | --- |
| **Template engine** | Django Templates | Zero learning curve for tutorials. |
| **CSS** | Bootstrap 5 CDN | Reliable styling, no build step. |
| **JS** | HTMX + Alpine (CDN) | Loaded only when needed; avoid SPA weight. |
| **Static serve** | WhiteNoise (gzip+br, hashed names) | Production‑ready caching without S3/CDN yet. |

## 8 · Auth & Authorization

| Decision | Rationale |
| --- | --- |
| **Custom user `AccountUser`** | Adds FK → `Company` now; future‑proofs SSO fields. |
| **Authentication backend** | Default Django; SSO can be dropped in later. |
| **RBAC** | `CompanyRestrictedMixin` auto‑filters QuerySets; templates stay permission‑free. |

## 9 · Security Basics (apply from Day 1)

- `SECURE_HSTS_SECONDS = 31536000`, `SECURE_SSL_REDIRECT = True` once behind TLS.
- `CSRF_TRUSTED_ORIGINS` set via env per deploy host.
- Password hashing: Django PBKDF2 defaults.
- Install **django‑axes** early to throttle brute‑force logins.

---

### Quick‑start Checklist
1. `python -m venv .venv && pip‑tools compile && pip‑tools sync`
2. `django‑admin startproject project_config .` and create `core_app` app.
3. Implement initial models.
4. Add `CompanyRestrictedMixin` + basic CRUD CBVs.
5. Run `python manage.py migrate && python manage.py createsuperuser`.
6. Verify tenant scoping locally with two test companies.

Move to **Phase 2** once the MVP works end‑to‑end.