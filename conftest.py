import pytest


class User():
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Sofiia'
        self.second_name = 'Serve'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user  
    user.remove()