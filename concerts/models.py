from django.db import models

class Concert(models.Model):
    band_name = models.CharField(max_length=200)
    venue = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    date = models.DateField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.band_name} at {self.venue}"
