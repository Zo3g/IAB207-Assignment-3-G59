from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking
# from .forms import BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bookingbp = Blueprint('booking', __name__, url_prefix='/booking')


@bookingbp.route('/', methods=['GET', 'POST'])
@login_required
def get_booking():
    bookings = db.session.scalar(db.select(Booking).where(Booking.userName.like(current_user.name)))
    return render_template('booking.html', bookings = bookings)
