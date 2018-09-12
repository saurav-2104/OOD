"""
Provide a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem easier to use.
"""

"""
Use case:
As a lazy, shopaholic person, I need a one button-click checkout to place my order.
"""


class BuyNow:
    """
    One-click buy feature
    """

    def __init__(self):
        self.order = OrderService()
        self.inventory = InventoryService()
        self.shipper = ShippingService()
        self.invoice = InvoiceService()

    def buy(self, item):
        self.order.generate_order(item)
        self.inventory.reduce(item)
        self.shipper.ship(item)
        self.invoice.generate_bill(item)


class OrderService:

    def generate_order(self, item):
        print("Order generated for item: {}".format(item))


class InventoryService:

    def reduce(self, item):
        print("Reduced the quantity of the item: {}".format(item))


class ShippingService:

    def ship(self, item):
        print("Added to the shipment queue.")


class InvoiceService:

    def generate_bill(self, item):
        print("Generated the bill.")


if __name__ == '__main__':
    item = "BF Pizza"
    BuyNow().buy(item)
