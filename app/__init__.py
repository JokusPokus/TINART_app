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

    from .conversation import lm as lm_blueprint
    app.register_blueprint(lm_blueprint)

    # Load ML models
    from app.conversation.conversation import Conversation
    convo = Conversation(guests=app.config["TALKSHOW_GUESTS"])
    app.config["CONVERSATION"] = convo

    # Sentiment classifier
    from app.conversation.sentiment import SentimentClassifier
    classifier = SentimentClassifier()
    app.config["SENTIMENT_CLASSIFIER"] = classifier

    return app
