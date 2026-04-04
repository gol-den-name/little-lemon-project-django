from django.db import models


from django.db import models


class Booking(models.Model):  # Capital 'B'
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        # register differentation via date stamps with user names
        return f"{self.first_name} - {self.reservation_date}"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f"{self.name} : {str(self.price)}"
