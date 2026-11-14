from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize database extension instance globally
db = SQLAlchemy()

def create_app(config_class=Config):
    """Factory function to build and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app instance
    db.init_app(app)

    # Register blueprints (routes)
    from app.routes.main_routes import main_bp
    from app.routes.api_routes import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app