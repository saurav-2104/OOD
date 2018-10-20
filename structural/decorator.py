"""
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
Follows open-closed principle.
"""
import abc

"""
Use case:
Any beverage can have one or multiple condiments. The price also varies as such. Example, an order for a coffee can be 
a double mocha with cream.
"""


class Beverage(metaclass=abc.ABCMeta):

    def get_description(self):
        return self.description

    @abc.abstractmethod
    def get_cost(self):
        raise NotImplementedError


class Condiments(Beverage, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_description(self):
        raise NotImplementedError


class Coffee(Beverage):

    def __init__(self):
        self.description = "Coffee"

    def get_cost(self):
        return 12


class Tea(Beverage):

    def __init__(self):
        self.description = "Tea"

    def get_cost(self):
        return 10


class Mocha(Condiments):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def get_cost(self):
        return self.beverage.get_cost() + 5


class Cream(Condiments):

    def __init__(self, beverage):
        self.beverage = beverage

    def get_cost(self):
        return self.beverage.get_cost() + 7

    def get_description(self):
        return self.beverage.get_description() + ', Cream'


if __name__ == '__main__':
    beverage1 = Coffee()
    cream = Cream(beverage1)
    mocha = Mocha(cream)
    mocha = Mocha(mocha)
    print("Beverage: {}, costs: {}".format(mocha.get_description(), mocha.get_cost()))
