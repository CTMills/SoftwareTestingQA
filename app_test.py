import pytest
from calculation import retirement_calculate, bmi_calculate
import app

def test_method1():
    x = bmi_calculate(5, 10, 250)
    assert x == 36.7

def test_method2():
    x = bmi_calculate(4, 2, 125)
    assert x == 36.0

def test_method3():
    x = bmi_calculate(5, 10, 150)
    assert x == 22.0

def test_method4():
    x = bmi_calculate(5, 10, 100)
    assert x == 14.7

def test_method5():
    x = bmi_calculate(5, 10, 175)
    assert x == 25.7

def test_method6():
    x = retirement_calculate(75, 255000, 15, 1000000)
    assert x == 95

def test_method7():
    x = retirement_calculate(25, 450000, 5, 2500000)
    assert x == 108

def test_method8():
    x = retirement_calculate(50, 50000, 5, 100000)
    assert x == 80

def test_method9():
    x = retirement_calculate(45, 500000, 35, 10000000)
    assert x == 88

def test_method10():
    x = retirement_calculate(50, 50000, 15, 1000000)
    assert x == 149

def test_method11():
    assert app.test() == "Works!"