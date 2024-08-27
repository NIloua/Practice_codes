import pytest
from my_calculator import Calculator


def test_add():
    calc=Calculator()
    assert calc.add(10,8)==18
def test_sub():
    calc=Calculator()
    assert calc.subtract(20,5)==15
def test_multiply():
    calc=Calculator()
    assert calc.multiply(3,4)==12
def test_division():
    calc=Calculator()
    assert calc.division(6,3)==2
def zero_division():
    calc=Calculator()
    assert calc.division(5,0)=="Error!"
def test_view_history():
    calc=Calculator()
    assert calc.view_history()!=""
def test_clear_history():
    calc=Calculator()
    assert calc.clear_history()=="Cleared successfully!"

