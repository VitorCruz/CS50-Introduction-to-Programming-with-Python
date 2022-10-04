
class Jar:
    def __init__(self, capacity=12, cookies=0):
        if capacity < 0:
            raise ValueError("Capacity must be a number > 0")

        self.capacity = capacity
        self.cookies = cookies

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.capacity:
            raise ValueError("Not enough capacity for that amount of cookies")
        if n < 0:
            raise ValueError("Must deposit a positive number of cookies")

        self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies in the jar. Maybe consider a diet?")
        if n < 0:
            raise ValueError("Must withdraw a positive number of cookies")

        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._cookies

    @size.setter
    def size(self, cookies):
        self._cookies = cookies

