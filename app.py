from flask import Flask, request
from flask_babel import Babel
from config import Config
from extensions import db, init_extensions
from models import User
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)
    app.logger.setLevel(logging.DEBUG)

    # Initialize extensions
    init_extensions(app)
    app.logger.debug("Extensions initialized")

    # Initialize Babel
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        return 'de'  # Set German as the default language

    # Import and register blueprints
    from routes import auth, main, dashboard, resources, forum
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(resources.bp)
    app.register_blueprint(forum.bp)
    app.logger.debug("Blueprints registered")

    # Create tables and test user within app context
    with app.app_context():
        app.logger.debug("Creating database tables")
        db.create_all()
        app.logger.debug("Database tables created")

        # Create test user if it doesn't exist
        test_user = User.query.filter_by(username='testuser').first()
        if not test_user:
            app.logger.debug("Creating test user")
            test_user = User(username='testuser', email='testuser@example.com')
            test_user.set_password('testpassword123')
            db.session.add(test_user)
            db.session.commit()
            app.logger.debug("Test user created")
        else:
            app.logger.debug("Test user already exists")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
