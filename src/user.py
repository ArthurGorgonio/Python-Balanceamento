class User:
    def __init__(self, ttask):
        self.ttask = ttask
        self.spent = 0

    def is_finished(self) -> bool:
        """Check if the user finish to use the servers

        Returns:
            bool: Return True if the user finish the task in servers,
                and False otherwise
        """

        return self.spent > self.ttask

    def update_task(self) -> None:
        """Update the status of the task.
        """
        self.spent += 1

    def get_spent(self) -> int:
        """Get the total of spent time of the task

        Returns:
            int: The current total spent time of the task
        """

        return self.spent
