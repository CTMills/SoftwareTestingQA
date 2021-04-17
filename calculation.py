import math

def retirement_calculate (age, salary, savedPercent, savingsGoal):
    decimalPercent = savedPercent / 100
    savingsPerYear = round(salary * decimalPercent * 1.35, 5)
    yearsTilGoal = math.ceil(savingsGoal / savingsPerYear)
    goalAge = age + yearsTilGoal
    return goalAge


def bmi_calculate (heightFeet, heightInch, weight):
    height = (heightFeet * 12) + heightInch
    metricWeight = weight * 0.45
    metricHeight = height * 0.025
    bmiHeight = metricHeight ** 2
    bmiFinal = round(metricWeight / bmiHeight, 1)
    return bmiFinal