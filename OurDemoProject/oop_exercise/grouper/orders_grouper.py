from oop_exercise.grouper.bad_data_tracker import BadDataTracker


class NotExistingGroupingFn(Exception):
    pass


class OrdersGrouper:
    def __init__(self, orders_data):
        self.orders_data = orders_data
        self.bad_data_tracker = BadDataTracker()

    def group_by_location(self):
        for order_info in self.orders_data:
            order_info["details"].sort(key=lambda detail: detail["location"])
            self.bad_data_tracker.update_counts(order_info["details"], order_info["order_id"])
        return self.orders_data

    def get_grouped_data(self, group_by="location"):
        if grouping_fn := getattr(self, f"group_by_{group_by}", None):
            return grouping_fn()
        else:
            raise NotExistingGroupingFn()
