from flask import Flask
from flask_security import hash_password, Security, SQLAlchemyUserDatastore
from config import DevelopmentConfiguration, ProductionConfiguration
from controller.authorization import auth_bp
from controller.admin import admin_bp
from controller.customer import customer_bp
from controller.home import home_bp
from controller.professional import professional_bp
from controller.resources import api_bp
from controller.models import User, Role
from extensions import db
import os


def init_app():
  householdService_app = Flask(__name__)
  if(os.getenv("FLASK_ENV") == "development"): 
    householdService_app.config.from_object(DevelopmentConfiguration)
  elif(os.getenv("FLASK_ENV") == "production"):
    householdService_app.config.from_object(ProductionConfiguration)
  db.init_app(householdService_app)
  api_bp.init_app(householdService_app)
  datastore = SQLAlchemyUserDatastore(db, User, Role)
  householdService_app.security = Security(householdService_app, datastore)
  householdService_app.register_blueprint(admin_bp)
  householdService_app.register_blueprint(auth_bp)
  householdService_app.register_blueprint(customer_bp)
  householdService_app.register_blueprint(home_bp)
  householdService_app.register_blueprint(professional_bp)
  householdService_app.app_context().push()
  return householdService_app
  
app = init_app()

with app.app_context():
  db.create_all()
  
  app.security.datastore.find_or_create_role(name = "Admin", description = "Superuser of an app")
  app.security.datastore.find_or_create_role(name = "Customer", description = "Customer of app")
  app.security.datastore.find_or_create_role(name = "Professional", description = "Professional of app")
  db.session.commit()
  
  if(not app.security.datastore.find_user(email = "user@admin.com")):
    app.security.datastore.create_user(email = "user@admin.com", 
                                      username = "admin01", 
                                      password = hash_password("1234"),
                                      roles = ["Admin"])

  if(not app.security.datastore.find_user(email = "user1@user.com")):
    app.security.datastore.create_user(email = "user1@user.com", 
                                    username = "user01", 
                                    password = hash_password("1234"),
                                    roles = ["Customer"])
    
  if(not app.security.datastore.find_user(email = "user2@user.com")):
    app.security.datastore.create_user(email = "user2@user.com", 
                                    username = "user02", 
                                    password = hash_password("1234"),
                                    roles = ["Professional"])
    
  db.session.commit()


if __name__ == "__main__":
  app.run(debug = True)