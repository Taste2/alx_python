"""
Rectangle Module

This module defines a rectangle

Classes:
- Base - Represents base class for rest of classes
- Rectangle: Represents a rectangle inherited from Base class
"""

class Base:
    """
    Base class for subsequent tasks
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Class constructor. Pass attributes to objects
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        Sets value for private attribute

        attribute:
        width: the width of rectangle
        """
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
        Sets value for private attribute

        attribute:
        height: the height of rectangle
        """
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
        Sets value for private attribute

        attribute:
        x: the x position of rectangle
        """
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
        Sets value for private attribute

        attribute:
        y: the y position of rectangle
        """
        self.__y = y