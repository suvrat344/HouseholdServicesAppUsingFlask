from flask import Blueprint, jsonify
from flask_security import auth_required, roles_required

admin_bp = Blueprint("admin", "__name__")


@admin_bp.route("/admin")
@auth_required("token")               # Authentication
@roles_required("admin")              # RBAC Authorization
def admin_home():
  return jsonify({
    "message" : "admin logged in successfully"
  })


