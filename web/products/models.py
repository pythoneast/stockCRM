from django.db import models


class Product(models.Model):
    INSTOCK = 'ST'
    WAITING = 'WA'
    NOTAVAILABLE = 'NA'

    STATUS_CHOICES = (
        (INSTOCK, 'In stock'),
        (WAITING, 'Waiting for receipt'),
        (NOTAVAILABLE, 'Not available'),
    )

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOTAVAILABLE,
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} {self.quantity}'

    @property
    def get_title(self):
        x = f'{self.name}'\
            f'{self.quantity}'
        return x

    def get_product_count(self):
        return self.__class__.objects.count()

    @staticmethod
    def get_product_count2():
        return Product.objects.count()

    @classmethod
    def get_product_count3(cls):
        return cls.objects.count()

    @classmethod
    def get_product_quantity(cls):
        qs = cls.objects.all()
        quantity = sum([i.quantity for i in qs])
        # quantity = 0
        # for i in qs:
        #     quantity += i.quantity
        return quantity

