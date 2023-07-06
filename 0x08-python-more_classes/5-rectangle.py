#!/usr/bin/python3
"""Rectangle empty class"""


class Rectangle:
    """Init method"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ repesentation rectangle"""
        rec = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rec += "#" * self.__width
                rec += "\n"
            rec = rec[:-1]
        elif self.__width == 0 or self.__height == 0:
            return ''
        return rec

    def __repr__(self):
        """ return rectangle"""
        return 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'

    def __del__(self):
        """Delete object """
        print("Bye rectangle...")
