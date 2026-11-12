# Versions

Resolved in `uv.lock` on 2026-10-29. "Previous" is the old `requirements.txt` / `runtime.txt`.

| Component | Version | Previous | Note |
|---|---|---|---|
| Python | 3.13 (resolved 3.13.18) | 3.10.9 | `requires-python >=3.13` |
| Django | 5.2.18 | 4.1.4 | 5.2 is the LTS line (6.1.x is newer but not LTS) |
| django-jazzmin | 3.0.5 | 2.6.0 | |
| django-embed-video | 1.4.10 | 1.4.8 | emits harmless SyntaxWarnings on import under Python 3.13 (upstream docstrings) |
| Pillow | 13.0.0 | 9.3.0 | |
| WhiteNoise | 6.12.0 | 6.2.0 | |
| dj-database-url | 3.1.2 | 1.2.0 | |
| gunicorn | 26.2.0 | unpinned (Procfile) | |
| psycopg | 3.3.6 (binary) | psycopg2 2.9.5 | |
| requests | 2.34.2 | 2.28.1 | |
| stripe | 16.0.1 | 5.0.0 | no code uses the SDK yet; payments view is a stub |
| django-heroku | removed | 0.3.1 | unmaintained |

Dev: pytest, pytest-django, ruff.
