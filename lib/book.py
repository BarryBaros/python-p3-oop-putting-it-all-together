#!/usr/bin/env python3

# lib/book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Title must be a string.")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            raise ValueError("Page count must be a positive integer.")
            
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
