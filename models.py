"""from app import db, app
from flask_login import LoginManager, UserMixin #, login_user, logout_user

# Create user model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
 
 
# Initialize app with extension
db.init_app(app)
# Create database within app context
 
with app.app_context():
    db.create_all()
"""
"""
from datetime import datetime
from app import db


class ReportHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)  # Store the file name
    generated_on = db.Column(db.DateTime, default=datetime.now())  # Date and time of generation
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Link to user (optional)
    
    # Optionally, you can define a relationship with the User model if needed
    #user = db.relationship('User', backref=db.backref('reports', lazy=True))

    def __repr__(self):
        return f"<ReportHistory {self.filename} generated on {self.generated_on}>"
"""