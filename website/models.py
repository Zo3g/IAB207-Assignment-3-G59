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
    numticket = db.Column(db.Integer)
    ticketcost = db.Column(db.Integer)
    eventdate = db.Column(db.DateTime)
    eventstart = db.Column(db.DateTime)
    description = db.Column(db.String(200))
    
    def __repr__(self):
        return f"Event: {self.name}"
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    User_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    Event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return f"Comment: {self.text}"
    
class Booking(db.Model):
    __tablename__ = 'booking'
    userID = db.Column(db.Integer)
    reference = db.Column(db.Integer, primary_key=True)
    eventID = db.Column(db.Integer, primary_key=True)
    tickets = db.Column(db.Integer)
        
    def __repr__(self):
        return f"Booking: {self.text}"




