from flask import Flask, render_template, redirect
from forms import bmiForm, retirementForm
from calculation import bmi_calculate, retirement_calculate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jfkldsajffdsafdsf'

@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route("/bmi", methods=['GET', 'POST'])
def bmi():
    bmi_report = -1
    form = bmiForm()
    if form.validate_on_submit():
        bmi_report = bmi_calculate(form.heightFeet.data, form.heightInches.data, form.weightPounds.data)

    return render_template('bmi.html', title='BMI', form=form, bmi_report=bmi_report)

@app.route("/retirement", methods=['GET', 'POST'])
def retirement():
    retirement_report = -1
    form = retirementForm()
    if form.validate_on_submit():
        retirement_report = retirement_calculate(form.age.data, form.salary.data, form.savedPercent.data, form.savingsGoal.data)
        
    return render_template('retirement.html', title='Retirement', form=form, retirement_report=retirement_report)

@app.route("/test")
def test():
    return "Works!"
