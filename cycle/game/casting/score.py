import constants

from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost.

    The responsibility of Score is to keep track of the points the player has earned.
    It contains methods for adding and getting points. Client should use get_text() to get a string
    representation of the points earned.

    Attributes:
    ---
        _points (int): The points earned in the game.
        position (Point): A point value to place each players score on the screen.
        _player_name (string): A string that will hold each players name.
        set_position (method): A method that sets the scores position on the screen.
        set_text (method): A method that displays each players name.
    """
    def __init__(self):
        """Sets starting points and position of points display

        """
        super().__init__()
        self._points = 1
        position = Point(0, 0)
        self._player_name = ""
        self.set_text(f"{self._player_name}: {self._points}")
        self.set_position(position)


    def add_points(self, points):
        """Adds the given points to the running total and updates the text.

        Args:
        ---
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._points += points
        self.set_text(f"{self._player_name}: {self._points}")

    def get_points(self):
        """Sets points for the user

        Returns:
        ---
            Integer: A point value for each player.
        """
        return self._points

    def reduce_points(self):
        """Reduces points for the user"""
        if self._points >= 1:
            self._points -= 1
        else:
            self._points = 0
        self.set_text(f"{self._player_name}: {self._points}")

    def set_player_name(self,name):
        """Sets the player's name

        Args:
        ---
            name (string): gets the user inputted name
        """
        self._player_name = name
        self.set_text(f"{self._player_name}: {self._points}")
