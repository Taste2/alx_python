
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
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not positive.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
            str: String representation of the Square instance.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size