
"""
Module containing the Rectangle class.
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
    def __dir__(cls) -> None:
        """
        Removes __init_subclass__ from list of class attributes
        """
        attributes = super().__dir__()
        n_attributes = []
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
    
    def __init__(self, width, height):
        """
        Call attriutes of parent.
        validates attributes for positive integer
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
            """
            Returns the string representation"""
            return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
            """
            This method computes the area of the triangle
            """
            return self.__width * self.__height
    
class Square(Rectangle):
    """
    A class or blueprint that models a square
    """
    def __init__(self, size):
        """
          instantiate attributes to an object 
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        computes area of the square
        """
        return self.__size ** 2
    