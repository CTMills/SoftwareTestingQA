from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class bmiForm(FlaskForm):
    heightFeet = IntegerField('Input height in feet: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    heightInches = IntegerField('Input height in inches: ', validators=[InputRequired(message='You must enter your height in inches'), 
                                                        NumberRange(min=0, max=12, message='There are only between 0-12 inches')])

    weightPounds = IntegerField('Input weight in pounds: ', validators=[InputRequired(message='You must enter your weight in pounds'), 
                                                        NumberRange(min=0, message='You cannot have a negative weight')])

    submit = SubmitField('Calculate BMI Report')


class retirementForm(FlaskForm):
    age = IntegerField('Input age in years: ', validators=[InputRequired(message='You must enter your age in years'), 
                                                        NumberRange(min=0, message='You cannot have a negative age')])

    salary = IntegerField('Input your salary: ', validators=[InputRequired(message='You must enter your salary'), 
                                                        NumberRange(min=0, message='You cannot have a negative salary')])

    savedPercent = IntegerField('Input the percent saved: ', validators=[InputRequired(message='You must enter your percent saved'), 
                                                        NumberRange(min=0, max=100, message='Percentages go from 0 to 100')])

    savingsGoal = IntegerField('Input your savings goal: ', validators=[InputRequired(message='You must enter your savings goal'), 
                                                        NumberRange(min=0, message='You cannot have a negative savings goal')])

    submit = SubmitField('Calculate Retirement Report')