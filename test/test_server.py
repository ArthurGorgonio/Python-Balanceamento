import pytest

from server import Server


@pytest.fixture
def base_server():
    return Server(umax=2)


@pytest.fixture
def server_max_user():
    server = Server(umax=2)
    server.add_user(2)
    server.add_user(2)

    return server


def test_is_finished(server_max_user):
    assert server_max_user.is_finished() == False

    server_max_user.update_server()
    server_max_user.update_server()
    server_max_user.update_server()
    assert server_max_user.is_finished() == True


def test_calculate(base_server, server_max_user):
    base_server.calculate()
    assert base_server.get_total_cost() == 0

    server_max_user.calculate()
    assert server_max_user.get_total_cost() == 1


def test_user_connect(base_server, server_max_user):
    assert base_server.user_connect() == 0
    assert server_max_user.user_connect() == 2


def test_add_user(base_server, server_max_user):
    assert base_server.add_user(4) == True
    assert server_max_user.add_user(4) == False


def test_remove_user(base_server, server_max_user):
    server_max_user.update_server()
    server_max_user.update_server()
    server_max_user.update_server()
    assert server_max_user.user_connect() == 0

    base_server.remove_user()
    assert base_server.user_connect() == 0
