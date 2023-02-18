import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.change
def test_remove_second_name(user):
    user.second_name = ''
    assert user.second_name == ''
