"""
This module checks if an instance is directly or indirectly inherits a specific class

"""
def inherits_from(obj, a_class):
    """AI is creating summary for inherits_from

    Args:
        obj ([type]): object
        a_class ([type]): a class

    Returns:
        True: obj is a subclass of a_class
        False: obj not a sub class of a_class
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False