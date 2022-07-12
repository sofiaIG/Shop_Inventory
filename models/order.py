class Order:
    def __init__(
        self, order_date, plant_id, quantity, customer_id, order_number, id=None
    ):
        self.order_date = order_date
        self.plant_id = plant_id
        self.quantity = quantity
        self.customer_id = customer_id
        self.order_number = order_number
        self.id = id
