import copy
import os

from pathlib import Path

from server import Server


def converter(str_list: str) -> list[int]:
    converted = []

    for num in str_list:
        try:
            converted.append(int(str(num).split('\n')[0]))
        except ValueError as e:
            raise ValueError(f'Não foi possível converter {num} em número'
                             f' Exceção: {e}')

    return converted


def read_file(file_name: str = '../resources/input.txt') -> list[str]:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    return lines


def write_file(output_file_name, servers) -> None:
    with open(output_file_name, 'a') as output_file:
        if isinstance(servers, list):
            output_file.write(str(servers).replace(' ', '')[1:-1] + '\n')
        else:
            output_file.write(str(servers) + '\n')


def validate_input(var: int, min: int, max: int) -> bool:
    if var >= min and var <= max:
        return True
    else:
        raise ValueError(f'Era esperado o valor entre {min} e {max} para a'
                         f' e foi encontrado {var}')


def create_server(umax: int) -> Server:
    return copy.deepcopy(Server(umax=umax))


def remove_server(servers: list[Server]) -> tuple[list[Server], int]:
    cost = 0

    for server in servers.copy():
        if server.is_finished():
            cost += server.get_total_cost()
            servers.remove(server)

    return servers, cost


def calculate_servers_cost(
        servers: list[Server]) -> tuple[list[Server], list[int], int]:
    connected = []

    for server in servers:
        server.update_server()
    servers, cost = remove_server(servers)

    for server in servers:
        connected.append(server.user_connect())

    return servers, connected, cost


def controller_user_list(user_add: int, servers: list[Server],
                         ttask: int, umax: int) -> list[Server]:

    while user_add > 0:
        user_add -= 1
        is_added = False
        # Is any server avaliable?

        for server in servers:
            if not server.is_full() and server.user_connect() > 0:
                is_added = server.add_user(ttask)

                if is_added:
                    break
        # No server avaliable, create a new one

        if not is_added:
            servers.append(create_server(umax))
            servers[-1].add_user(ttask)

    return servers


def run() -> None:
    users_input = read_file()
    valid_users = converter(users_input)
    valid = []
    valid.append(validate_input(valid_users[0], 1, 10))
    valid.append(validate_input(valid_users[1], 1, 10))
    servers: list(Server) = []
    output_file = Path('../resources/output.txt')

    if output_file.is_file():
        os.remove(output_file)

    if all(valid):
        ttask = valid_users[0]
        umax = valid_users[1]
        users = valid_users[2:]
        server_cost = 0

        while len(servers) or len(users):
            if len(users):
                servers = controller_user_list(
                    users.pop(0), servers, ttask, umax)
            servers, connected, cost = calculate_servers_cost(servers)
            server_cost += cost

            if len(servers):
                write_file(output_file, connected)
            else:
                write_file(output_file, 0)
        write_file(output_file, server_cost)
    else:
        raise ValueError('error')


if __name__ == '__main__':
    run()
