#!/usr/bin/python
from flask import Flask, render_template, url_for, flash, redirect, request, make_response
from forms import MonthYearForm
from config import Config
from datetime import datetime, timedelta, date

import requests
import json
import time
import calendar

app = Flask(__name__)
app.config.from_object(Config)

headers = {
    'Content-Type': 'application/json',
    'api-key': app.config['TOKEN']
}
url = app.config['URL']

@app.route("/", methods=['GET', 'POST'])
def index():
    form = MonthYearForm()
    response = requests.get(f'{url}/events', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return render_template('wszystko.html', events=data, form=form)

@app.route("/kalendarz")
def kalendarz():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    days = [date(int(year), int(month), day) for day in range(1, calendar.monthrange(int(year), int(month))[1]+1)]
    thisdict = {day: [] for day in days}
    response = requests.get(f'{url}/events', headers=headers)
    if response.status_code == 200:
        data = response.json()
        for event in data:
            parsed_date = datetime.strptime(event["start_time"], "%Y-%m-%dT%H:%M:%S")
            if parsed_date.date() in thisdict.keys():
                thisdict[parsed_date.date()].append(event)
    return render_template('kalendarz.html', thisdict=thisdict, year=year, month=month, day=int(day))

@app.route("/wydarzenie/<int:id>")
def wydarzenie(id):
    response = requests.get(f'{url}/events/{id}', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return render_template('wydarzenie.html', event=data)

@app.route("/filtruj/<string:tag>")
def filtruj(tag):
    form = MonthYearForm()
    response = requests.get(f'{url}/events/filter/?tag={tag}', headers=headers)
    if response.status_code == 200:
        data = response.json()
        return render_template('wszystko.html', events=data, form=form, tag=tag)

@app.errorhandler(404)
def page_not_found(e):
    return "Oops! The page you are looking for does not exist.", 404

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
