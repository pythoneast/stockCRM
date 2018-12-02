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
