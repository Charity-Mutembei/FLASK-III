import os

class Config:

    NEWS_API_ARTICLES_URL ='https://newsapi.org/v2/everything?q=everything&from={}&sortBy=publishedAt&apiKey={}'
    NEWS_API_KEY = 'c3011dcec4e546228a335c5326e69378'
    SECRET_KEY = 'hello world'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}