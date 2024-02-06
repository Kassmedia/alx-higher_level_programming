#!usr/bin/python3
"""Define class square, inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a Square class instance."""

    def __init__(self, size):
        """
            Initialize a new Square instance.

            Args:
                size (int): The length of one side of the Sqaure instance.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the current Square instance. """
        return self.__size * self.__size
