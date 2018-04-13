import os

class Config:
    '''
    General configuration parent class
    '''

    @staticmethod
    def init_app(app):
        pass





class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent Configuration class with general configuration settings
    '''
    pass
# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://lulumutuli:lulu@localhost/watchlist_test'


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    # password=lulu
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}
