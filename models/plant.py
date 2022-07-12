class Plant:
    def __init__(
        self,
        name,
        description,
        buying_cost,
        selling_price,
        manufacturer,
        stock_quantity,
        id=None,
    ):
        self.name = name
        self.description = description
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.stock_quantity = stock_quantity
        self.id = id
