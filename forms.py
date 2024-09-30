from flask_wtf import FlaskForm
from wtforms import SelectField, RadioField, SubmitField, HiddenField
from datetime import datetime, timedelta
import calendar

class MonthYearForm(FlaskForm):
    months = [(str(i), datetime(2000, i, 1).strftime('%B')) for i in range(1, 13)]  # Month names
    years = [(str(y), str(y)) for y in range(2020, 2031)]  # Example range of years

    month = SelectField('Choose Month', choices=months, default=str(datetime.now().month))
    year = SelectField('Choose Year', choices=years, default=str(datetime.now().year))
    day = HiddenField()

    submit = SubmitField('Submit')
