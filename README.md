# FlaskApp

## Project Structure

```text
FlaskApp/
├── app/                       # Main application package
│   ├── routes/                # Modular route blueprints
│   │   ├── __init__.py        # Routes package initializer
│   │   ├── api_routes.py      # JSON API endpoints (/api/*)
│   │   └── main_routes.py     # Frontend web views (/)
│   ├── static/                # Static frontend assets
│   │   └── CSS/
│   │       └── style.css      # Main stylesheet
│   ├── templates/             # Jinja2 HTML templates
│   │   ├── base.html          # Master layout template
│   │   └── index.html         # Home page view
│   ├── __init__.py            # Application factory & extensions
│   ├── config.py              # App & database configuration
│   └── models.py              # SQLAlchemy database models
├── instance/                  # Local runtime files & SQLite DB
├── .env                       # Environment variables (secrets)
├── .gitignore                 # Git ignored files & caches
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
└── run.py                     # Application entry point
