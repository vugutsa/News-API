# import os
# class Config:
#     NEWS_API_BASE_URL ='http://newsapi.org/v2/everything?q={}&apiKey={}'
#     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
#     SECRET_KEY = os.environ.get('SECRET_KEY')
# class ProdConfig(Config):
#     """
#     production configuration child clas
#     Args:
#        config: The parent configuration class with general configuration settings
#     """
#     pass
# class DevConfig(Config):
#     """
#     development configuration child class
#     Args:
#         Config: The parent configuration class with General configuration settings.
#     """
#     DEBUG = True
# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig
# }