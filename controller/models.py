from extensions import db
from flask_security import RoleMixin, UserMixin

class User(db.Model, UserMixin):
  __tablename__ = "user"
  user_id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), nullable = False, unique = True)
  email = db.Column(db.String, nullable = False, unique = True)
  password = db.Column(db.Text, nullable = False)
  fs_uniquifier = db.Column(db.String, nullable = False, unique = True)
  active = db.Column(db.Boolean, nullable = False)
  roles = db.relationship('Role', backref = "users", secondary = "users_role")
  user_request = db.relationship("ServiceRequest", backref = "user_service_request")
  user = db.relationship("UserDetails", backref = "user_details", uselist = False)
  professional = db.relationship("ProfessionalQualification", backref = "professional_qualification", uselist = False)
  
  
class Role(db.Model, RoleMixin):
  __tablename__ = "role"
  role_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(20), nullable = False, unique = True)
  description = db.Column(db.Text)
  __table_args__ = (
    db.CheckConstraint(
      "name IN ('Admin', 'Customer', 'Professional')", 
      name = "checkRole"
      ),
  )
  

class UserRole(db.Model):
  __tablename__ = "users_role"
  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete = "CASCADE"))
  role_id = db.Column(db.Integer, db.ForeignKey("role.role_id", ondelete = "CASCADE"))
  
  
class UserDetails(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete = "CASCADE"), primary_key = True)
  name = db.Column(db.String(30), nullable = False)
  contact_number = db.Column(db.String(10), nullable = False)
  state = db.Column(db.String(20), nullable = False)
  city = db.Column(db.String(30), nullable = False)
  pin_code = db.Column(db.String(6), nullable = False)
  address = db.Column(db.String(50), nullable = False)
  image_file = db.Column(db.Text, nullable = False)
  search_column = db.Column(db.Text, nullable = True)
  
  
class ProfessionalQualification(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete = "CASCADE"), primary_key = True)
  service_type = db.Column(db.String(20), nullable = False)
  experience = db.Column(db.Integer, nullable = False)
  resume = db.Column(db.Text, nullable =False)
  search_column = db.Column(db.Text, nullable = True)
  
  
class Service(db.Model):
  __tablename__ = "services_offered"
  service_id = db.Column(db.Integer, primary_key = True)
  service_name = db.Column(db.String(20), nullable = False, unique = True)
  description = db.Column(db.Text, nullable = False)
  image_file = db.Column(db.Text, nullable = False)
  price = db.Column(db.Float, nullable = False)
  time_required = db.Column(db.Numeric(2,2), nullable = False)
  is_delete = db.Column(db.Boolean, default = False)
  service_correspond_request = db.relationship("ServiceRequest", backref = "related_service")
  search_column = db.Column(db.Text, nullable = True)
  
  
class ServiceRequest(db.Model):
  __tablename__ = "service_request"
  service_request_id = db.Column(db.Integer, primary_key = True)
  service_id = db.Column(db.Integer, db.ForeignKey("services_offered.service_id", ondelete = "CASCADE"))
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete = "CASCADE"))
  date_of_request = db.Column(db.Date, nullable = False)
  date_of_completion = db.Column(db.Date, nullable = False)
  service_status = db.Column(db.String(10), default = "Pending")
  problem_description = db.Column(db.Text, nullable = True)
  professional_rating = db.Column(db.Integer, nullable = True)
  remarks = db.Column(db.Text, nullable = True)
  actions = db.relationship("ProfessionalAction", backref = "related_service_request")
  search_column = db.Column(db.Text, nullable = True)
  
  __table_args__ = (
    db.CheckConstraint(
      'professional_rating >= 1 AND professional_rating <=5', 
      name = 'check_professional_rating'
      ),
    db.CheckConstraint(
      'service_status IN ("Pending", "Accepted", "Cancelled", "Closed")', 
      name = "check_service_status"
      ),
  )
  
class ProfessionalAction(db.Model):
  __tablename__ = "professional_action"
  service_request_id = db.Column(db.Integer, db.ForeignKey("service_request.service_request_id"))
  user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
  action_type = db.Column(db.String(10), nullable = False)
  
  __table_args__ = (
    db.PrimaryKeyConstraint(
      "service_request_id", "user_id",
      name = "primary_key_constraint"
      ),
    db.CheckConstraint(
      "action_type IN ('Pending', 'Accepted', 'Requested', 'Cancelled', 'Closed')", 
      name = 'professional_action_status'
      ),
  )