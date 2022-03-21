class Plant:
    def __init__(self, name, description, stock_quantity, buying_cost,
    selling_price, manufacturer_id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.manufacturer_id = manufacturer_id


    def add_stock(self, item):
        self.stock_quantity.append(item)

    def stock_quantity_sum(self):
        return len(self.stock_quantity)