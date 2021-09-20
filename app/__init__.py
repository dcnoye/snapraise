from flask import Flask

def create_app(extra_config_settings={}):
    """Create a Flask application.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    app.config.from_object('app.settings')

    # Register blueprints
    from app.views.home_views import home_blueprint
    app.register_blueprint(home_blueprint)

    return app
