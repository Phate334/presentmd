import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATA_PATH = os.path.join(basedir, 'present')
    API_KEY = os.getenv('PRESENTMD_KEY') or ''
    MD_SEPARATOR = '^-----'
    MD_SEPARATOR_VERTICAL = '^---'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {'default': DevelopmentConfig}
