import time
from django.test import TestCase
from products.models import Product


class ProductModelTestCase(TestCase):
    def setUp(self):
        start = time.time()
        # Product.objects.bulk_create([
        #     Product(name="table", status="ST", quantity=234),
        #     Product(name="chair", status="ST", quantity=234),
        #     Product(name="lamp", status="ST", quantity=234),
        #     Product(name="pc", status="ST", quantity=234),
        #     Product(name="laptop", status="ST", quantity=234),
        # ])
        names = ["table", "chair", "lamp", "pc", "laptop"]
        Product.objects.bulk_create(
            [Product(name=name, status="ST", quantity=234) for name in names])
        end = time.time()
        print(end-start, 'seconds')

    def test_get_product_count3(self):
        Product.objects.create(name="mouse", status="ST", quantity=234)
        quantity = Product.get_product_count3()
        self.assertEqual(quantity, 6)

    def test_get_product_quantity(self):
        quantity = Product.get_product_count3()
        quantity2 = Product.get_product_quantity()
        self.assertEqual(quantity, 5)
        self.assertEqual(quantity2, 1170)
