from flask import Blueprint, jsonify
from flask_security import auth_required, current_user, roles_required

customer_bp = Blueprint("customer", "__name__")


@customer_bp.route("/customer")
@auth_required("token")
@roles_required("customer")
def customer_home():
  user = current_user
  return jsonify({
    "username" : user.username,
    "email" : user.email,
    "password" : user.password
  })