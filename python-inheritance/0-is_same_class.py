"""
This module checks if an object is the instance of a class

"""
def is_same_class(obj, a_class):
    """Check if object is an instance of a class

    Args:
        obj: An object instance
        a_class: a class

    Returns:
        True: If object is instance of the class
        False: if object not imstance of the class
    """
    if isinstance(obj, a_class):
       return True
    else:
        return False