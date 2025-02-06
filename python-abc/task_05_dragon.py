#!/usr/bin/env python3
"""
Design two mixin classes, SwimMixin and FlyMixin
equipped with methods swim and fly respectively. 
Next, construct a class Dragon
"""

class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
