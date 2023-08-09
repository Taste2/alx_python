"""
Rectangle Module

This module defines a rectangle

Classes:
- Base - Represents base class for rest of classes
- Rectangle: Represents a rectangle inherited from Base class
"""

from models.base import Base

class Rectangle(Base):
    """
    Representsg a rectangle

    Attributes:
    width (int): width of the rectangle
    height (int): height of the rectangle
    x (int): x position o rectangle
    y (int): y position of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes rectangle instance with  widht, height, x and y.

        Parameters:
        width (int): width of the rectangle
        height (int): height of the rectangle
        x (int): x position of rectangle
        y (int): y position of rectangle
        """
        super().__init__(id)
        self.validate(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate(self, width, height, x, y):
        """
        validates the arguments passed into the object
        """
        if width != int(width):
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be > 0".format(width))
        if height != int(height):
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be > 0".format(height))
        if x != int(x):
            raise TypeError("{} must be an integer".format(x))
        if x < 0:
            raise ValueError("{} must be >= 0".format(x))
        if y != int(y):
            raise TypeError("{} must be an integer".format(y))
        if y < 0:
            raise ValueError("{} must be >= 0".format(y))

    @property
    def width(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of width
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        """
        Sets value and validation for private attribute

        attribute:
        width: the width of rectangle
        """
        if width != int(width):
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be > 0".format(width))
        self.__width = width

    @property
    def height(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of height
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """
        Sets value and validation for private attribute

        attribute:
        height: the height of rectangle
        """
        if height != int(height):
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be > 0".format(height))
        self.__height = height

    @property
    def x(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of x
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        Sets value and validation for private attribute

        attribute:
        x: the x position of rectangle
        """
        if x != int(x):
            raise TypeError("{} must be an integer".format(x))
        if x < 0:
            raise ValueError("{} must be >= 0".format(x))
        self.__x = x

    @property
    def y(self):
        """
        Gives access to the private attribute

        Returns:
        int: the private attribute of y
        """
        return self.__y
    
    @y.setter
    def y(self, y):
        """
        Sets value and validation for private attribute

        attribute:
        y: the y position of rectangle
        """
        if y != int(y):
            raise TypeError("{} must be an integer".format(y))
        if y < 0:
            raise ValueError("{} must be >= 0".format(y))
        self.__y = y
