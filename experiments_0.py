import numpy
import inspect
import sys


def introspection_info(variable):
    # Attempt to find the module of the variable
    module = inspect.getmodule(variable)

    print(isPrimitive(variable))
    # print(variable.__mod__.__name__)

    if module is not None:
        return module.__name__  # Return the module name
    else:
        return "The variable is not defined in a module."


# Example usage
def isPrimitive(obj):
    return not hasattr(obj, '__dict__')

print(introspection_info(numpy.pi))  # Expected output: numpy

# sys.exit()
PI = float(str(numpy.pi))
print(introspection_info(PI))  # The variable is defined in this module.


print(getattr(numpy, 'pi', 'default'))
print(getattr(numpy, 'pii', 'default'))
setattr(numpy, 'pii', 3.14)
print(getattr(numpy, 'pii', 'default'))

PI = float(str(numpy.pi))
print(PI is numpy.pi)
print(PI == numpy.pi)

