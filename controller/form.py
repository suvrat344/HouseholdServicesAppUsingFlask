from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
  username = StringField("Username",
                         validators=[ 
                          DataRequired(message = "Please enter a username."), 
                          Length(min = 4, max = 20,message = "Username must be between 4 to 20 characters.") ],
                         render_kw = {"placeholder" : "ENTER USERNAME"}
                         )
  
  email = StringField("Email",
                      validators=[ 
                       DataRequired(message = "Email is required."), 
                       Email(message = "Invalid email format.")],
                      render_kw = {"placeholder" : "ENTER EMAIL"}
                      )
  
  password = PasswordField("Password", 
                        validators=[ 
                          DataRequired("Password is required."),
                          Length(min = 6, max = 12, message = "Password must be between 6 to 12 characters.")],
                        render_kw = {"placeholder" : "ENTER PASSWORD"}
                        )
  
  confirmPassword = PasswordField("Confirm Password", 
                          validators=[ 
                            DataRequired(message = "Please confirm your password."), 
                            EqualTo('password', message = "Passwords must match.") ],
                          render_kw = {"placeholder" : "ENTER PASSWORD"}
                          )
  
  submit = SubmitField("Register")