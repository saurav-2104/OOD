"""
Define an interface for creating an object, but let subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.
"""

import abc

"""
Use case:
There are many varieties of pizzas. Each Pizza Store specializes in some specific pizzas.
"""


class PizzaStore(metaclass=abc.ABCMeta):
    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.pack()

    @abc.abstractmethod
    def create_pizza(self, type):
        raise NotImplementedError


class Pizza(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = None
        self.dough = "Standard dough"
        self.sauce = None
        self.toppings = list()

    def prepare(self):
        print("Preparing pizza: {}".format(self.name))
        print("Tossing dough: {}".format(self.dough))
        print("Adding sauce: {}".format(self.sauce))
        for topping in self.toppings:
            print("Adding topping: {}".format(topping))

    def bake(self):
        print("Baking at 250 for 10 mins")

    def cut(self):
        print("Cutting into 6 slices")

    def pack(self):
        print("Packing in company standard boxes")


class NewYorkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "New York Pizza"
        self.sauce = "sweet chilly sauce"
        self.toppings.extend(["Basil", "Cheese", "Tomato"])


class CaliforniaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "California Pizza"
        self.sauce = "Tomato sauce"
        self.toppings.extend(["Onion", "Corn", "Pineapple"])


class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'cheese':
            return NewYorkPizza()


class CaliforniaPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'pineapple':
            return CaliforniaPizza()


if __name__ == '__main__':
    pizza_store = NewYorkPizzaStore()
    pizza_store.order_pizza('cheese')
    cal_pizza_store = CaliforniaPizzaStore()
    cal_pizza_store.order_pizza('pineapple')
