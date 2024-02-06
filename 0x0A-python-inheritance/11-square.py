#!/usr/bin/python3
"""Define class Square, inherit from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class instance."""

    def __init__(self, size):
        """
            Intialize a new Square instances.

            Args:
                size (int): Th len of one side of square instance.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().init__(size, size)

    def area(self):
        """Returns the area of the current Square instance. """
        return self.__size * self.__size
    def __str__(self):
        """Return the representation of the square instance."""
        return "[Square] {}/{}".format(self.__size, self.__size)
