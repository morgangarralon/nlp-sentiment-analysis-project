class Config(object):
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'
    MODEL_FOLDER = 'static/data/models/'

    @property
    def DATABASE_URI(self):         # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)

class ConfigProduction(Config):
    DB_SERVER = '192.168.19.32'

class ConfigDevelopment(Config):
    DB_SERVER = 'localhost'
    DEBUG = True