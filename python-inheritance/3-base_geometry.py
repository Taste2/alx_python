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
