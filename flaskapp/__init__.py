from flask import Flask

# Initialize the Flask app
def create_app():
    # Create the Flask instance
    app = Flask(__name__)

    # Configuration (if needed, you can add any configuration here)
    # app.config.from_object('config.Config')  # for example, you can load a config file

    # Register the routes (or blueprints) here
    from .app import app  # Import app from app.py and register it

    return app
