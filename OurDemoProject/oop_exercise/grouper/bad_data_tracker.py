from collections import defaultdict


class BadDataTracker:
    def __init__(self):
        self.locations_orders = defaultdict(set)
        self.to_locations_orders = defaultdict(set)

    @property
    def bad_locations(self):
        return {
            location: orders
            for location, orders in self.locations_orders.items()
            if len(orders) > 1
        }

    @property
    def bad_to_locations(self):
        return {
            to_location: orders
            for to_location, orders in self.to_locations_orders.items()
            if len(orders) > 1
        }

    def update_counts(self, products_data, order_id):
        for product_data in products_data:
            if not product_data["location"] or not product_data["tolocation"]:
                continue
            self.locations_orders[product_data["location"]].add(order_id)
            # self.to_locations_orders[product_data["tolocation"]].add(order_id)
