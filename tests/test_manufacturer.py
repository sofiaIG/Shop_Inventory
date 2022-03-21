import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer_1 = Manufacturer("Plants Limited")


    def test_name(self):
        self.assertEqual("Plants Limited", self.manufacturer_1.name)


        