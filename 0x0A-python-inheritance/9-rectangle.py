#!/usr/bin/python3
"""This refers to a class Rectangle that is inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle."""

    def __init__(self, width, height):
        """This intializes new Rectangle.
        Args:
            width : the width.
            height : The height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
