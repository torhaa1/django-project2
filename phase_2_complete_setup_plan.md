# Django CRUD Web App – **Phase 2: Complete Setup Plan**

**Goal**
Polish the MVP into a production‑ready service: add user niceties, admin tooling, automated tests, observability, and deployment hardening.

---

## 10 · User‑Facing Extras

| Feature | Rationale |
| --- | --- |
| **Filtering** (`django‑filter`) | One‑liner drop‑in to help users narrow result sets. |
| **Pagination** (25/page) | Balances load time and scrolling; built into CBVs. |

## 11 · Admin

| Decision | Rationale |
| --- | --- |
| Register all models; `list_filter=('company',)` | Instant back‑office UI while preserving tenant boundaries. |

## 12 · Testing & Quality

| Tool | Rationale |
| --- | --- |
| `pytest‑django` | Succinct asserts & fixtures; great IDE support. |
| `factory_boy` | Declarative, reusable test data. |

## 13 · Performance Guidelines

- Use `.select_related('company')` to eliminate N + 1 queries.
- Only add `cache_page` or local‑mem cache when profiling shows clear wins.

## 14 · Observability

| Aspect | Choice | Rationale |
| --- | --- | --- |
| **Errors** | Sentry free tier | Zero‑ops stack traces & release tracking. |
| **Logging** | first: JSON → stdout; optional later: `django‑db‑logger` | Docker/Kubernetes friendly; DB sink for audit trails. |

## 15 · Deployment Snapshot

| Component | Choice | Rationale |
| --- | --- | --- |
| Web server | `nginx` | TLS offload & static caching. |
| App server | `waitress` (WSGI) | Minimal config, cross‑platform. |
| Static/media | WhiteNoise | Avoids separate object storage at this scale. |

## 16 · Docs & Ongoing Care

- **README.md**: 5‑minute project overview + `make dev` quick‑start.
- **docs/quickstart.md**: Step‑by‑step newcomer guide.
- **docs/ADRs/**: Record architectural choices (one ADR ≈ 1 decision).

---

### Layer Responsibilities (cheat‑sheet)

| Layer | Owns | Never contains |
| --- | --- | --- |
| **Models** | Permanent business rules, DB invariants | HTTP/session data |
| **Forms** | UX‑level validation & coercion | Cross‑tenant checks |
| **Views** | Orchestrate model ↔ form ↔ template | Heavy loops/business logic |
| **Templates** | Presentation only | Permissions, DB hits |
| **Services** | Multi‑step workflows/side‑effects | HTML rendering |

---

Complete these steps to reach Phase 2:
1. Add `django‑filter` filters to list views.
2. Register all models in admin with tenant filters.
3. Write baseline pytest fixtures & first CRUD tests.
4. Integrate Sentry and JSON logging.
5. Containerise with `nginx` + `waitress`; enable WhiteNoise.
6. Capture decisions as ADRs and polish docs.