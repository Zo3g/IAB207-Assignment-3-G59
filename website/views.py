from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event
from . import db


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = db.session.scalars(db.select(Event)).all()
    return render_template('index.html', events=events)

@bp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        events = db.session.scalars(db.select(Event)).where(Event.description.like(query))
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))
        
@bp.route('/filter')
def filter_events():
    search_term = request.args.get('faculty')
    if search_term:
        print(search_term)
        query = "%" + search_term + "%"
        events = db.session.scalars(db.select(Event).where(Event.organiser.like(query)))
        return render_template('index.html', events=events)
    else:
        return redirect(url_for('main.index'))



