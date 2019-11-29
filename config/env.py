from os import environ


class EnvConfig(object):
    DEBUG = False
    REDIS_HOST = "0.0.0.0"
    REDIS_PORT = 6379
    BROKER_URL = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))
    CELERY_RESULT_BACKEND = BROKER_URL


class DevelopmentEnv(EnvConfig):
    DEBUG = True


class TestingEnv(EnvConfig):
    TESTING = True
    DEBUG = True


class StagingEnv(EnvConfig):
    DEBUG = True


class ProductionEnv(EnvConfig):
    DEBUG = False
    TESTING = False


app_env = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'staging': StagingEnv,
    'production': ProductionEnv
}

