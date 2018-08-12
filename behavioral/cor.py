"""
Chain of Responsibility Pattern
Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
Chain the receiving objects and pass the request along the chain until an object handles it.
Launch-and-leave requests with a single processing pipeline that contains many possible handlers.
An object-oriented linked list with recursive traversal.
"""
import abc
from enum import Enum

"""
Use case: A bug when raised has to be handled depending on the severity.
Developer: Handles low severity bugs
Director: Handles medium severity bugs
VP: Handles critical severity bugs
"""


class Severity(Enum):
    low = 1
    high = 2
    critical = 3


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, successor=None):
        self.successor = successor

    @abc.abstractmethod
    def handle(self, severity):
        raise NotImplementedError("Please implement the method.")


class DeveloperHandler(Handler):

    def handle(self, severity):
        if severity == Severity.low:
            print("Developer handled the issue. Please do not escalate.")
        elif self.successor:
            self.successor.handle(severity)


class ManagerHandler(Handler):

    def handle(self, severity):
        if severity == Severity.high:
            print("Manager handled the issue. Please do not escalate.")
        elif self.successor:
            self.successor.handle(severity)


class VicePresidentHandler(Handler):

    def handle(self, severity):
        if severity == Severity.critical:
            print("VP handled the issue.")
        else:
            print("We are sorry !")


if __name__ == '__main__':
    low = Severity.low
    high = Severity.high
    critical = Severity.critical
    invalid = "Invalid"
    vp = VicePresidentHandler()
    manager = ManagerHandler(vp)
    dev = DeveloperHandler(manager)
    dev.handle(low)
    dev.handle(high)
    dev.handle(critical)
    dev.handle(invalid)
