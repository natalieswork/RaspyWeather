from flask import Flask, Blueprint, render_template, request, flash, jsonify, redirect
from website.weather import main as get_weather
from .models import Location
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':

        city = request.form['cityName']
        state = request.form['stateName']
        country = request.form['countryName']

        try:
            data = get_weather(city, state, country)
            new_loc = Location(city=city, state=state,
                               country=country, nickname="")
            db.session.add(new_loc)
            db.session.commit()
            flash('Location Added!', category='success')
        except Exception as e:
            print(str(e))
            flash('Invalid Location!', category='error')

    locations = Location.query.all()

    weather_data = []
    for location in locations:
        data = get_weather(location.city, location.state, location.country)
        weather_data.append({
            'location': location,
            'weather': data
        })

    return render_template('index.html',  weather_data=weather_data)


@views.route('/delete-location', methods=['POST'])
def delete_location():
    location = json.loads(request.data)
    id = location['LocId']
    loc = Location.query.get(id)
    if loc:
        db.session.delete(loc)
        db.session.commit()

    return jsonify({})


@views.route('/edit-location/<int:location_id>', methods=['POST'])
def edit_location(location_id):
    new_nickname = request.form['nickname']
    location = Location.query.get(location_id)
    if location:
        location.nickname = new_nickname
        db.session.commit()
        flash('Nickname updated successfully!', category='success')
    else:
        flash('Location not found!', category='error')
    return redirect('/')
