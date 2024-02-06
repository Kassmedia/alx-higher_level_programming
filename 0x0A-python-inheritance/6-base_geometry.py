#!/usr/bin/python3
"""Documentation for an empty class creation"""


class BaseGeometry:

    """Takes no function"""

    def area(self):
        """that raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")
