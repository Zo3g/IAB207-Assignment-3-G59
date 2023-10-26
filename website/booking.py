from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event, Booking
from .forms import BookingForm
# from .forms import CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
# additional import:
from flask_login import login_required, current_user

bookingbp = Blueprint('booking', __name__, url_prefix='/booking')
