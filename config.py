import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '#A?jYd$D\Hv8>P8W'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    TALKSHOW_GUESTS = ["lindner", "wagenknecht"]
    DEBUG = True


class TestingConfig(Config):
    TALKSHOW_GUESTS = ["lindner", "wagenknecht"]
    TESTING = True


class ProductionConfig(Config):
    TALKSHOW_GUESTS = os.environ.get("TALKSHOW_GUESTS") or ["lindner", "wagenknecht"]


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}