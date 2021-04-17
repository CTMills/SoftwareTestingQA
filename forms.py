from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class bmiForm(FlaskForm):
    heightFeet = IntegerField('Input height in feet: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    heightInches = IntegerField('Input height in inches: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    weightPounds = IntegerField('Input weight in pounds: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    submit = SubmitField('Calculate BMI Report')


class retirementForm(FlaskForm):
    age = IntegerField('Input age in years: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    salary = IntegerField('Input your salary: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    savedPercent = IntegerField('Input the percent saved: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    savingsGoal = IntegerField('Input your savings goal: ', validators=[InputRequired(message='You must enter your height'), 
                                                        NumberRange(min=0, message='You cannot have a negative height')])

    submit = SubmitField('Calculate Retirement Report')