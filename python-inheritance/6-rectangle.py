
"""
Module containing the Rectangle class.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

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