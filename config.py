class Config:
    # SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'
    SECRET_KEY = 'AUGGIE_AYUDE_GVN'


class DevelopmentConfig(Config):
    DEBUG = True
    """ MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB = 'flask_login' """


config = {
    'development': DevelopmentConfig
}
