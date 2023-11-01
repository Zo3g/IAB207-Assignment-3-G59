from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking
# from .forms import BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bookingbp = Blueprint('booking', __name__, url_prefix='/booking')


@bookingbp.route('/booking/<userID>', methods=['GET', 'POST'])
@login_required
def get_booking(userID):
    booking = db.session.scalar(db.select(Booking).where(Booking.id == id))
    booking = Booking.query.filter_by(id == userID)
    return ('booking.html', booking == booking)
