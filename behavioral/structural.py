"""
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
Helps in solving "Open-Closed Principle" in SOLID
"""

import abc

"""
Use case: As a Bangalorean, I would like to determine my strategy on travelling to 
the airport.
"""


class Person(object):
    """
    The Context
    """

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def travel_to_airport(self):
        self.strategy.travel()


class TravelStrategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    TravelStrategy.
    """

    @abc.abstractmethod
    def travel(self):
        pass


class BusStrategy(TravelStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def travel(self):
        print("Travelling by bus....")


class CabStrategy(TravelStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def travel(self):
        print("Travelling by cab....")


class WalkStrategy(TravelStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def travel(self):
        print("Walking....")


class AutoStrategy(TravelStrategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def travel(self):
        raise NotImplementedError


if __name__ == '__main__':
    walk = WalkStrategy()
    bus = BusStrategy()
    auto = AutoStrategy()
    cab = CabStrategy()
    person = Person('Saurav', bus)
    # person.travel_to_airport()
    person_fresher = Person('Fresher', auto)
    person_fresher.travel_to_airport()
