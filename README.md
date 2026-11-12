# Food and Beverage Nepal

A website dedicated to showcasing food and beverage options in Nepal.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [License](#license)
- [Contributing](#contributing)

## About

This project provides a platform for exploring various food and beverage options available in Nepal. It is designed to give users an intuitive and visually appealing experience.

## Features

- Home page with the three latest posts; paginated posts list (6 per page) with embedded videos (django-embed-video).
- About page listing team members with photos.
- Contact/inquiry form for logged-in users (one inquiry per post per user).
- User registration, login, and logout (POST).
- Stripe payments page (publishable key shown; the charge endpoint returns 503 until payment processing is implemented).
- Django admin with the Jazzmin theme at `/admin/`.

## Technologies Used

Python 3.13, Django 5.2 LTS, django-jazzmin, django-embed-video, Stripe SDK, Pillow, WhiteNoise, gunicorn, SQLite by default or PostgreSQL via `DATABASE_URL`. Versions: [VERSIONS.md](./VERSIONS.md).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/kneeraazon404/FoodandBeverage.git
cd FoodandBeverage
export DJANGO_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_DEBUG=true
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Configuration is by environment variable; see [.env.example](./.env.example) (`DJANGO_SECRET_KEY` is required, `DATABASE_URL` selects PostgreSQL, `EMAIL`/`EMAIL_PASSWORD` plus `DJANGO_EMAIL_BACKEND` enable SMTP, `STRIPE_*` enable the payments page).

Production must use `DJANGO_DEBUG=false`, set `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS` to the real hostnames, then run `migrate` and `collectstatic --noinput`. `Procfile` runs gunicorn. Do not commit credentials or local settings backups.

## Testing

```bash
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
```

Tests (`tests/`) use `FoodandBeverage.settings_test` (in-memory SQLite, temp media) and cover registration/login/logout, posts, team, contact inquiries, and payments. CI: `.github/workflows/ci.yml`.

## Project structure

```
FoodandBeverage/  settings, urls, wsgi/asgi, static assets, settings_test.py
blog/ posts/ team/ contact/ users/ payments/   Django apps
templates/        shared templates and partials
tests/            pytest suite
pyproject.toml, uv.lock   dependencies (requirements.txt is exported for Heroku-style builds)
```

## License

This project is licensed under the [Apache License 2.0](LICENSE).

Please refer to the `LICENSE` file for more details.

## Contributing

We welcome contributions! If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

For any issues or inquiries, feel free to reach out via the [repository's issue tracker](https://github.com/kneeraazon404/FoodandBeverage/issues).
