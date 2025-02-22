from flask import current_app as app, jsonify
from flask_security import auth_required, current_user, roles_required


@app.route("/admin")
@auth_required("token")               # Authentication
@roles_required("admin")              # RBAC Authorization
def admin_home():
  return jsonify({
    "message" : "admin logged in successfully"
  })


@app.route("/customer")
@auth_required("token")
@roles_required("customer")
def user_home():
  user = current_user
  return jsonify({
    "username" : user.username,
    "email" : user.email,
    "password" : user.password
  })