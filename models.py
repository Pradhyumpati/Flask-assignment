from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "students"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
     
     
 
    def __init__(self, first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
         

        
 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"