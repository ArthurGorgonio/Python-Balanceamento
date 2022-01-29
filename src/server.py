from user import User
import copy


class Server:
    def __init__(self, cost=1, umax=1):
        self.cost = cost
        self.total_cost = 0
        self.umax = umax
        self.full = False
        self.users: list[User] = []

    def add_user(self, ttask) -> bool:
        """Add an user to the server

        Args:
            ttask (int): How many ticks a task should (user length of
                stay)

        Returns:
            bool: True if the user is added, False otherwise.
        """

        if not self.full and self.add_user_to_server():
            self.users.append(copy.deepcopy(User(ttask=ttask)))
            self.server_avaliable()

            return True

        return False

    def add_user_to_server(self) -> bool:
        """Auxiliary function to identify if a user will br removed in
            the next iteration (optimize server balancing)

        Returns:
            bool: True if the user can be added to the server, False
                otherwise.
        """
        add = []

        if self.total_cost == 0:
            return True
        else:
            for user in self.users:
                add.append(user.ttask > user.get_spent())

            return any(add)

    def calculate(self) -> None:
        if self.user_connect():
            self.total_cost += 1

    def get_total_cost(self) -> int:
        return self.total_cost

    def is_full(self) -> bool:
        return self.full

    def is_finished(self) -> bool:
        if self.user_connect() == 0 and self.get_total_cost() > 0:
            return True
        else:
            return False

    def remove_user(self) -> None:
        for user in self.users.copy():

            if user.is_finished():
                self.users.remove(user)
        self.server_avaliable()

    def server_avaliable(self) -> None:
        if self.user_connect() < self.umax and self.user_connect() > 0:
            self.full = False
        else:
            self.full = True

    def update_server(self) -> None:
        """Update the server's status and its users
        """

        for user in self.users:
            user.update_task()
        self.remove_user()
        self.calculate()

    def user_connect(self) -> int:
        return len(self.users)
