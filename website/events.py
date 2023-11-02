from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Comments, Booking
from .forms import EventForm, CommentForm, BookingForm, EventEditForm
from . import db
from datetime import datetime
import os
from werkzeug.utils import secure_filename

from flask_login import login_required, current_user

eventbp = Blueprint('event', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    bookingForm = BookingForm() 
    commentForm = CommentForm()   
    return render_template('events/show.html', event=event, commentForm=commentForm, bookingForm = bookingForm)

@eventbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)
    form = EventForm()
    if form.validate_on_submit():

        db_file_path = check_upload_file(form)
        event_datetime = datetime.combine(form.eventdate.data, form.eventtime.data)
        event = Event(name=form.name.data, description=form.description.data,
                      image=db_file_path, organiser=form.organiser.data, numticket=form.numticket.data, 
                      ticketcost=form.ticketcost.data, 
                      eventdatetime=event_datetime, venuename=form.venuename.data, username=current_user.name)
       
        db.session.add(event)
        db.session.commit()
        flash('Successfully created new event!', 'success')
        return redirect(url_for('event.create'))
    return render_template('events/create.html', form=form, heading='Create Event')

@eventbp.route('/delete/<id>', methods=['GET', 'DELETE'])
def delete(id):
    if current_user.is_authenticated:
        if (event.username != current_user.name):
            flash('Unauthorised attempt - an event may only be edited by the creator.')
            return redirect(url_for('event.show', id=event.id))
        
        event = db.session.scalar(db.select(Event).where(Event.id==id))
        db.session.delete(event)
        db.session.commit()
        flash('Event deleted')
        return redirect(url_for('main.index'))
    else:
        flash('Unauthorised attempt - an event may only be edited by the creator. If you are the creator, please sign in to your account.')
        return redirect(url_for('event.show', id=event.id))

@eventbp.route('/update/<id>', methods=['GET','POST'])
def update(id):
    form = EventEditForm()
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    if current_user.is_authenticated:

        if (event.username != current_user.name):
            flash('Unauthorised attempt - an event may only be edited by the creator.')
            return redirect(url_for('event.show', id=event.id))

        if form.validate_on_submit():

            db_file_path = check_upload_file(form)
            event_datetime = datetime.combine(form.eventdate.data, form.eventtime.data)


            event.name = form.name.data
            event.description=form.description.data
            event.image=db_file_path 
            event.organiser=form.organiser.data 
            event.numticket=form.numticket.data
            event.ticketcost=form.ticketcost.data
            event.eventdatetime=event_datetime
            event.venuename=form.venuename.data

            db.session.commit()
            return redirect(url_for('event.show', id=event.id))
        return render_template('events/create.html', form=form, heading='Update Event', subheading='Please fill out all fields with your updated event details')
    else:
        flash('Unauthorised attempt - an event may only be edited by the creator. If you are the creator, please sign in to your account.')
        return redirect(url_for('event.show', id=event.id))






def check_upload_file(form):
  fp = form.image.data
  filename = fp.filename
  BASE_PATH = os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH, 'static/img', secure_filename(filename))
  db_upload_path = '/static/img/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path


@eventbp.route('/<id>/comment', methods=['GET', 'POST'])
@login_required
def comment(id):
    form = CommentForm()
    event = db.session.scalar(db.select(Event).where(Event.id == id))
    if form.validate_on_submit():
        comment = Comments(text=form.text.data, event=event,
                          user=current_user, datetime=datetime.now())
       
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added', 'success')
    return redirect(url_for('event.show', id=id))

@eventbp.route('/<id>/booking', methods=['GET', 'POST'])
@login_required
def booking(id):
    form = BookingForm()
    event = db.session.scalar(db.select(Event).where(Event.id==id))
    if form.validate_on_submit():
        booking = Booking(tickets=form.tickets.data, event=event,
                          user=current_user)

        db.session.add(booking)
        db.session.commit()
        flash('Your booking has been confirmed', 'success')
    return redirect(url_for('booking.bookings'))
