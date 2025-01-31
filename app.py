from flask import Flask,render_template
from config import DevelopmentConfiguration, ProductionConfiguration
from controller.authorization import auth_blueprint
import os


def init_app():
  householdService_app = Flask(__name__)
  if(os.getenv("FLASK_ENV") == "development"): 
    householdService_app.config.from_object(DevelopmentConfiguration)
  elif(os.getenv("FLASK_ENV") == "production"):
    householdService_app.config.from_object(ProductionConfiguration)
  householdService_app.register_blueprint(auth_blueprint)
  return householdService_app
  
app = init_app()

@app.route("/")
def home():
  return "Hello"

if __name__ == "__main__":
  app.run(debug = True)