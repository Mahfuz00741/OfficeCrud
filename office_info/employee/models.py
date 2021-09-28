from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Dept(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField(auto_created=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    code = models.CharField(
        unique=True,
        max_length=4,
        validators=[MinLengthValidator(4, 'Code Must be 4 characters')]
    )
    name = models.CharField(
        max_length=35,
        null=False,
        validators=[MinLengthValidator(3, "Name min 3 and max 35 characters long")]
    )
    mobile = models.CharField(max_length=14)
    date_of_birth = models.DateField(auto_now=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
