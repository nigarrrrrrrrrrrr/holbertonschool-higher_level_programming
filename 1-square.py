#!/usr/bin/python3
"""Defines a square."""


class Square:
    """A square class with a private size attribute."""

    def __init__(self, size):
        """Initializes the square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
