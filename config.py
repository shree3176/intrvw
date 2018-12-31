import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SANSKRITY_MAIL_SUBJECT_PREFIX = '[SANSKRITY]'
    SANSKRITY_MAIL_SENDER = 'SANSKRITY Admin <shweta.3176@gmail.com>'
    SANSKRITY_ADMIN = os.environ.get('SANSKRITY_ADMIN')
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/shri'


#   SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#      'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # pushed local db to remote
    SQLALCHEMY_DATABASE_URI = "postgres://jxqryrhydozgpw:cf18d5231299e255c29c50068a0cc398f080873d4cf" \
                              "3b0152e7c107a982667f7@ec2-50-16-196-238.compute-1.amazonaws.com:5432/d8oehp79kvc7r1"


# class HerokuConfig(ProductionConfig):
#     SSL_REDIRECT = True if os.environ.get('DYNO') else False
#
#     @classmethod
#     def init_app(cls, app):
#         ProductionConfig.init_app(app)
#
#         # handle reverse proxy server headers
#         from werkzeug.contrib.fixers import ProxyFix
#         app.wsgi_app = ProxyFix(app.wsgi_app)
#
#         # log to stderr
#         import logging
#         from logging import StreamHandler
#         file_handler = StreamHandler()
#         file_handler.setLevel(logging.INFO)
#         app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    # 'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
