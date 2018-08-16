"""
The Template method pattern:
Define the skeleton of an algorithm in an operation, deferring some steps to subclasses.
Template Method lets subclasses redefine certain steps of an algorithm without letting them
to change the algorithm's structure.
Based on Inversion of Control aka Hollywood's Principle
"""

import abc

"""
Use case: KFC plans to open some restaurants in India. Most of the people in India are vegetarian.
"""


class Burger(metaclass=abc.ABCMeta):
    def make_burger(self):
        self.make_buns()
        self.insert_patty()
        self.insert_toppings()

    def make_buns(self):
        print("Buns have been baked.")

    def insert_toppings(self):
        print("Tomato and onions have been inserted")

    @abc.abstractmethod
    def insert_patty(self):
        raise NotImplementedError("This method needs implementation.")


class VegBurger(Burger):
    def insert_patty(self):
        print("A veg patty has been inserted")


class NonVegBurger(Burger):
    def insert_patty(self):
        print("A non-veg patty has been inserted")


if __name__ == '__main__':
    veg_burger = VegBurger()
    veg_burger.make_burger()
    non_ver_burger = NonVegBurger()
    non_ver_burger.make_burger()
