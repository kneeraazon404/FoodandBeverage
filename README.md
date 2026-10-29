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

- User-friendly and responsive design.
- Comprehensive details about food and beverages.
- Easy navigation across categories.

## Technologies Used

- **CSS** (54.5%)
- **JavaScript** (26%)
- **HTML** (12.5%)
- **Python** (6.9%)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/kneeraazon404/FoodandBeverage.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FoodandBeverage
   ```
3. Create and activate a virtual environment, then install `requirements.txt`.
4. Set `DJANGO_SECRET_KEY` to a unique secret. For local development, set
   `DJANGO_DEBUG=true` and `DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1`.
5. Set `DATABASE_URL` for PostgreSQL deployments; without it, the app uses a
   local SQLite database. Set `STRIPE_SECRET_KEY` and
   `STRIPE_PUBLISHABLE_KEY` only when configuring Stripe.
6. Run `python manage.py migrate` and `python manage.py runserver`.

Production must use `DJANGO_DEBUG=false` and set `DJANGO_ALLOWED_HOSTS` to the
actual hostnames. Do not commit credentials or local settings backups.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

Please refer to the `LICENSE` file for more details.

## Contributing

We welcome contributions! If you would like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

For any issues or inquiries, feel free to reach out via the [repository's issue tracker](https://github.com/kneeraazon404/FoodandBeverage/issues).
