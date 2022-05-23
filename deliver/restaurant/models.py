from django.db import models
from django.contrib.auth.models import User




BRANCH_CHOICES = (
    ("Trivandrum", "Trivandrum"),
    ("Kollam ", "Kollam"),
    ("Allapuzha ", "Allapuzha"),
    ("Kozhikode ", "Kozhikode"),
    ("Ernakulam ", "Ernakulam"),
    ("Thrissur ", "Thrissur"),
    ("Kasargod ", "Kasargod"),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    branch = models.CharField(choices=BRANCH_CHOICES, max_length=60)

    def __str__(self):
        return self.name