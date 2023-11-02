from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking, User
# from .forms import BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bookingbp = Blueprint('booking', __name__, url_prefix='/booking')


@bookingbp.route('/', methods=['GET', 'POST'])
@login_required
def bookings():
    user = db.session.scalar(db.select(User).where(User.id == current_user.id))
    # event = db.session.scalar(db.select(Event).where(Booking.event))
    return render_template('booking.html', user = user)
