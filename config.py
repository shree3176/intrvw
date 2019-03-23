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
    FLASKY_POSTS_PER_PAGE = 5
    FLASKY_FOLLOWERS_PER_PAGE = 50

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
    SQLALCHEMY_DATABASE_URI = "postgres://oimnlkvqkzrqft:72f96567f7bac9b0ccffcb64ed1b6e4081f08ea2406069d" \
                              "1bae6d84a8407532c@ec2-184-73-181-132.compute-1.amazonaws.com:5432/de1fdee9pok5nh"


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
