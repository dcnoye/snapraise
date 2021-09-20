# Settings common to all environments (development|staging|production)
import os


DEBUG = True

# Application settings
APP_NAME = "polish calc"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
CSRF_ENABLED = True

# Flask-SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Flask secret, yes it's not static
SECRET_KEY = os.urandom(16)
