import pytest
class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Olena'
        self.second_name = 'Lisova'

    def remove(self):
        self.name = ''
        self.second_name = ''

"""def test_change_name():
    user = User()
    user.create()

    assert user.name == 'Olena'
    user.remove()

def test_second_name():
    user = User()
    user.create()

    assert user.second_name == 'Lisova'
    user.remove()    """

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

def test_change_name(user):
    assert user.name == 'Olena'


def test_change_second_name(user):
    assert user.second_name == 'Lisova'    