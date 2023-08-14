from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=2000)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}"
