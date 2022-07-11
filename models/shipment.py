class Shipment:
    def __init__(self, order_id, shipping_date, shipping_company_id, id=None):
        self.order_id = order_id
        self.shipping_date = shipping_date
        self.shipping_company_id = shipping_company_id
        self.id = id
