import pytest

from user import User


@pytest.fixture
def base_user():
    return User(ttask=2)


def test_is_finished(base_user):
    expected_list = [False, False, True, True]

    for expected in expected_list:
        base_user.update_task()
        assert base_user.is_finished() == expected


def test_updade_task(base_user):
    assert base_user.get_spent() == 0
    base_user.update_task()
    assert base_user.get_spent() == 1
