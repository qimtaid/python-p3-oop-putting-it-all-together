#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = self._validate_size(size)
        self.condition = "Used"

    def _validate_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
            return 0
        return size

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")