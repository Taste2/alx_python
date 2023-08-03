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
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
