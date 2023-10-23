from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='user')

    def __repr__(self):
        return f"Name: {self.name}"

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    venuename = db.Column(db.String(200))
    image = db.Column(db.String(400))
    organiser = db.Column(db.String(80))
    numticket = db.Column(db.Integer(80))
    ticketcost = db.Column(db.Integer(80))
    eventdate = db.Column(db.Datetime(80))
    eventstart = db.Column(db.Datetime(80))
    description = db.Column(db.String(200))
    
    def __repr__(self):
        return f"Name: {self.name}"







