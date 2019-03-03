from unittest import TestCase
from models.item import ItemModel


class ItemModelTest(TestCase):
    def setUp(self):
        pass

    def test_create_item_model(self):
        item = ItemModel('test', 9.99)

        self.assertEqual(item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument")
        self.assertEqual(item.price, 9.99,
                         "The price of the item after creation does not equal the constructor argument")

    def test_json(self):
        item = ItemModel('test', 9.99)

        expected = {'name': 'test', 'price': 9.99}

        self.assertEqual(item.json(), expected, "The JSON export of the item is incorrect. Received {}, expected {}".format(expected, item.json()))
