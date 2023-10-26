from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking
from .forms import BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bookingbp = Blueprint('booking', __name__, url_prefix='/booking')


@bookingbp.route('/booking', methods=['GET', 'POST'])
@login_required
def book():
    print('Method type: ', request.method)
    form = BookingForm()
