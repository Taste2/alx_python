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

    def __init__(self, size=0):
        """Initialize a square instance
            Args:
                size(int): the size of the square initialized to 0
                """
        self.__size = size


    def sq_size(self, size):
        """
        A setter to set the size of attribute to an integer

        Args:
            size: The size of the square
        """
        if size == int(size):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size  >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")