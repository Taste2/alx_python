"""
This module is a definition of a class Square that represents a square.

Attributes:
    size(int): The length of each side of the square.

Methods:
    __init__(self, size): Initializes an instance or object of the class
"""
class Square():
    """
    A class that represents a square
    
    Attributes:
        size(int): The size of the square

    Methods:
        __init__(self, size): Initializes a Square object with the given size.
    """

    def __init__(self, size):
        """Initialize a square instance
            Args:
                size(int): the size of the square
                """
        self.__size = size