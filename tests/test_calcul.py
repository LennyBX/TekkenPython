import pytest
from calcule import *
from main import *
from faker import Faker

def test_plus1():
    assert plus1(3) == 4

def test_soustraction():
    assert soustraction1(3) == 2

def test_foix2():
    assert foix2(3) == 6

def test_diviser2():
    assert diviser2(2) == 1

@pytest.mark.parametrize("user_input,choix_ennemi,result", [(1,3, "You Win!"), (2,3, "You lose!")])
def test_rock_papier_ciseau(user_input, choix_ennemi, result):
    assert rock_paper_for_test(user_input, choix_ennemi) == result