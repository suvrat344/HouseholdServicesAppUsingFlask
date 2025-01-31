from flask import Blueprint, render_template
from controller.form import RegistrationForm

auth_blueprint = Blueprint("auth","__name__")


@auth_blueprint.route("/")
@auth_blueprint.route("/register", methods = ["GET", "POST"])
def register():
  form = RegistrationForm()
  if(form.validate_on_submit()):
    return "Successful"
  return render_template("register.html", form = form)