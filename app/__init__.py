from flask import Flask
from config import config


def create_app(config_name):
    """Factory function to create app instance"""

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .language_model import lm as lm_blueprint
    app.register_blueprint(lm_blueprint)

    # Load ML models
    from app.language_model.conversation import Conversation
    convo = Conversation(guests=app.config["TALKSHOW_GUESTS"])
    app.config["CONVERSATION"] = convo

    # Sentiment classifier
    from app.language_model.sentiment import SentimentClassifier
    classifier = SentimentClassifier()
    app.config["SENTIMENT_CLASSIFIER"] = classifier

    return app
