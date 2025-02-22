from flask import Blueprint, jsonify
from flask_security import auth_required, current_user, roles_required

professional_bp = Blueprint("professional", "__name__")
  
  
@professional_bp.route("/professional")
@auth_required("token")
@roles_required("customer")
def professional_home():
  user = current_user
  return jsonify({
    "username" : user.username,
    "email" : user.email,
    "password" : user.password
  })