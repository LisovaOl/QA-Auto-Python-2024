import pytest


class User:

    def __init__(self) -> None:
        self.name = "Olena"
        self.second_name = "Lisova"


@pytest.fixture
def user():
    yield User()

def test_remove_name(user):
    user.name = ''
    assert user.name == ''

def test_name(user):
    assert user.name == 'Olena'

def test_second_name(user):
    assert user.second_name == 'Lisova'    