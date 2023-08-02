"""
This module is an empty class 
"""


class BaseGeometry():
    """
    This class models an empty class
    """
    def __dir__(cls):
        """
        control access to some inherited attributes
        """
        n_attributes = []
        attributes = super().__dir__()
        for attr in attributes:
            if attr != '__init_subclass__':
                n_attributes.append(attr)
        return n_attributes
