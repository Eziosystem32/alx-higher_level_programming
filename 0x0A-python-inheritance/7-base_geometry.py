#!/usr/bin/python3
"""
Module containing the class BaseGeometry
"""


class BaseGeometry:
    """The BaseGeometry class"""
    def area(self):
        """raises an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
