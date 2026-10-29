# Work done: FoodandBeverage

Branch: `chore/modernize` (local, not pushed). Date: 2026-10-29.

## What was there
A Django 4.1 site (apps `blog`, `posts`, `team`, `contact`, `users`, `payments`) on Python 3.10 with 2022 pins, Heroku-style deployment (django-heroku, Procfile), and only empty `tests.py` stubs. Tracked in git: `.pyc`/`__pycache__`, `.DS_Store`, a SQLite database file named `foodandbeverage`, 18 uploaded photos in `media/`, and `.vscode/settings.json` (a personal interpreter path).

## Step 1: your uncommitted work, committed as-is
- `FoodandBeverage/settings.py`: hardcoded secret key, DEBUG and ALLOWED_HOSTS replaced by env vars; `DATABASE_URL` support; WhiteNoise middleware; a commented-out block containing a database password removed.
- `payments/views.py`, `payments/urls.py`: payment view reduced to a login-protected 503 stub; publishable key read from settings.
- `README.md`: setup notes. `.gitignore`: ignores `local_settings.py.save*`. Deleted tracked `local_settings.py.save` and `.save.1`.

## Step 2: modernization changes by file
| File | Before | Change |
|---|---|---|
| `pyproject.toml`, `uv.lock`, `.python-version` | absent | New uv project, Python 3.13, Django 5.2 LTS, pytest/ruff config |
| `requirements.txt`, `runtime.txt` | 2022 pins; python-3.10.9 | Regenerated from lockfile; python-3.13 |
| `FoodandBeverage/settings.py` | `django_heroku`, `USE_L10N`, duplicated commented email block, `EMAIl` env typo | Removed those; `STORAGES` with WhiteNoise manifest storage; email defaults to the console backend (SMTP via env), accepts `EMAIL` and the old `EMAIl`; CSRF trusted origins; HTTPS/HSTS/secure cookies when not debug |
| `FoodandBeverage/settings_test.py` | absent | New test settings |
| `users/views.py` | `logout` returned `None` on GET (HTTP 500); unused Contact query in `dashboard` | `@require_POST` on logout (GET now 405); dead query and import removed (dashboard still redirects home) |
| `contact/models.py`, `posts/models.py`, `team/models.py` | `default=datetime.now` (naive datetimes with `USE_TZ=True`) | `default=timezone.now` |
| `contact/migrations/0006_*`, `posts/migrations/0006_*`, `team/migrations/0005_*` | absent | New: record the default change |
| `blog/tests.py`, `contact/tests.py`, `payments/tests.py`, `posts/tests.py`, `team/tests.py`, `users/tests.py` | empty stubs | Deleted; replaced by `tests/` (18 tests) |
| other `.py` files | mixed formatting | `ruff format` and import sorting only |
| `.github/workflows/ci.yml`, `.env.example` | absent | New |
| `.gitignore` | had pyc/local_settings | Also ignores the SQLite file, media/, staticfiles/, .venv, .env, .vscode, .DS_Store, caches |
| `foodandbeverage` (SQLite), `media/`, `.vscode/`, pycache, `.DS_Store` | tracked | Untracked with `git rm --cached`; files remain on disk |
| `README.md` | generic feature list, language percentages | Rewritten to match the code: features, uv setup, testing, structure |
| `VERSIONS.md`, `work-done.md` | absent | New |

## Verification (actual runs)
- `uv run pytest -q`: 18 passed.
- `uv run ruff check .` and `ruff format --check .`: clean.
- `makemigrations --check --dry-run`: no changes; `migrate` applies cleanly on a fresh SQLite DB.
- `check --deploy` with production-style env: only the two optional HSTS warnings (include-subdomains, preload).

## Needs your attention
- **Rotate secrets.** The old Django secret key and a PostgreSQL password (in a commented-out settings block) are in git history. Removing them from the working tree does not remove them from history.
- The tracked SQLite file and `media/` photos are also in history.
- Not touched, flagged only:
  - `contact/models.py`: `user_id` is an IntegerField with `default="user_id"` (invalid default; the view always sets it).
  - `team/urls.py` references `views.team`; the root URL conf includes it.
  - `posts/views.py` `search` renders a template that does not exist.
  - The Stripe `charge` endpoint is a 503 stub; payments are not implemented.
- Nothing pushed. To publish: `git push -u origin chore/modernize`
