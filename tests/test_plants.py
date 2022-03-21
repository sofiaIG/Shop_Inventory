import unittest
from models.plant import Plant

class TestPlant(unittest.TestCase):
    def setUp(self):
        self.plant = Plant("Wallace", "Monkey face plant; Monkey plant; Mini Swiss cheese plant",
        2.55, 5, 32)


    def test_has_name(self):
        self.assertEqual("Wallace", self.plant.name)


    def test_has_description(self):
        self.assertEqual("Monkey face plant; Monkey plant; Mini Swiss cheese plant",
        self.plant.description)


    def test_has_selling_price(self):
        self.assertEqual(5, self.plant.selling_price)


    def test_has_buying_cost(self):
        self.assertEqual(2.55, self.plant.buying_cost)


    def test_has_id(self):
        self.assertEqual(32, self.plant.manufacturer)


    def test_stock_quantity_sum_add_item(self):
        self.assertEqual(1, self.plant.stock_quantity_sum())


    