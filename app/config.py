import os
class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../DB.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'change on deploy'

class HerokuConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')


def get_config():
    if os.environ.get('PROVIDER') == 'heroku':
        HerokuConfig.SQLALCHEMY_DATABASE_URI = \
            HerokuConfig.SQLALCHEMY_DATABASE_URI.replace(
                    "postgres://", "postgresql://", 1
                )

        return HerokuConfig
    
    else:

        return BaseConfig

