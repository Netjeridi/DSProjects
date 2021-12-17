class Config(object):
    DEBUG = False
    TESTING = False
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    ENV = "prod"
    SUB_FOLDER = "prod"


class DevelopmentConfig(Config):
    ENV = "dev"
    DEBUG = True
    SUB_FOLDER = "dev"


class TestingConfig(Config):
    TESTING = True
    SUB_FOLDER = "dev"
