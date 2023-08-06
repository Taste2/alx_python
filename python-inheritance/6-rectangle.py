"""
This module is an empty class 
"""


class BaseGeometry():
    """
    This class models an empty class
    """
    def __dir__(cls) -> None:
        """
        control access to some inherited attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    def area(self):
        """a method to raise an exception with a message"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        A method that validates value
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
    
class Rectangle(BaseGeometry):
    """
    Models a rectangle. A derived class of BaseGeometgry
    """
    def __init__(self, width, height) -> None:
        """
        Call attriutes of parent.
        validates attributes for positive integer
        """
        super().__init__(self, width, height)
        self.__width = width
        self.__height = height
        self.__width.integer_validator("width", width)
        self.__height.integer_validator("height", height)
        