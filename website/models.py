from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    contactNumber = db.Column(db.String(12), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comments', backref='user')
    bookings = db.relationship('Booking', backref ='user')

    def __repr__(self):
        return f"Name: {self.name}"

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    status = db.Column(db.String(10))
    venuename = db.Column(db.String(200))
    image = db.Column(db.String(400))
    organiser = db.Column(db.String(80))
    numticket = db.Column(db.Integer)
    ticketcost = db.Column(db.Integer)
    eventdatetime = db.Column(db.DateTime)
    description = db.Column(db.String(200))
    username = db.Column(db.String(100))

    comments = db.relationship('Comments', backref='event')
    bookings = db.relationship('Booking', backref='event')
    
    def __repr__(self):
        return f"Name: {self.name}"
    
class Comments(db.Model):
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
    reference = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(100), db.ForeignKey('users.id'), nullable=False)
    eventID = db.Column(db.Integer, db.ForeignKey('events.id'),nullable=True)
    tickets = db.Column(db.Integer, nullable=False)
        
    def __repr__(self):
        return f"Comment: {self.text}"




