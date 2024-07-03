#!/usr/bin/env python3
# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition when a shoe is created

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self._brand = value
        else:
            raise ValueError("Brand must be a string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
