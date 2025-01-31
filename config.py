import os
import secrets

class Config():
  DEBUG = False
  SECRET_KEY = os.environ.get("SECRET_KEY",secrets.token_hex(16))
  
class DevelopmentConfiguration(Config):
  DEBUG = True
  
class ProductionConfiguration(Config):
  DEBUG = False