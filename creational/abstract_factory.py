"""

"""

import abc

from creational.factory_method import PizzaStore

"""
Use case:
Pizza Factory with customization of ingredients
"""


class ThinCrustDough:
    pass


class ThickCrustDough:
    pass


class HotSauce:
    pass


class TomatoSauce:
    pass


class MozzarellaCheese:
    pass


class ReggianoCheese:
    pass


class PizzaIngredientFactory(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_dough(self):
        pass

    @abc.abstractmethod
    def create_sauce(self):
        pass

    @abc.abstractmethod
    def create_cheese(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return HotSauce()

    def create_cheese(self):
        return MozzarellaCheese()


class CAPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return TomatoSauce()

    def create_cheese(self):
        return ReggianoCheese()


class Pizza(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print('Baking for 30 mins at 225 F')

    def cut(self):
        print("Cutting into 6 equal slices")

    def pack(self):
        print("Packing into corrugated boxes")


class CheesePizza(Pizza):
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        dough = self.ingredient_factory.create_dough()
        sauce = self.ingredient_factory.create_sauce()
        cheese = self.ingredient_factory.create_cheese()
        print(
            'Prepared pizza using: dough: {}, sauce: {}, cheese: {}'.format(
                dough.__class__.__name__, sauce.__class__.__name__, cheese.__class__.__name__
            )
        )


class NewYorkPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'cheese':
            return CheesePizza(NYPizzaIngredientFactory())


class CaliforniaPizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == 'cheese':
            return CheesePizza(CAPizzaIngredientFactory())


if __name__ == '__main__':
    ny_store = NewYorkPizzaStore()
    ny_store.order_pizza('cheese')
    ca_store = CaliforniaPizzaStore()
    ca_store.order_pizza('cheese')
