class Plant:
    def __init__(self, name, description, buying_cost,
    selling_price, manufacturer, id = None):
        self.name = name
        self.description = description
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id
        self.stock_quantity = [name]



    def stock_quantity_sum(self):
        return len(self.stock_quantity)