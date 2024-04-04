from django.db import models
from django.core.validators import MinLengthValidator

class Make(models.Model):
    name=models.CharField(max_length=300,
    help_text="Enter an item",
    validators=[MinLengthValidator(2, "Name must be greater than 1 charcter")]
    )

    def __str__(self):
         return self.name


class Auto(models.Model):
    nickname=models.CharField(max_length=200,
    validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )

    mileage=models.PositiveIntegerField()
    comments=models.CharField(max_length=300)
    make=models.ForeignKey('Make', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname







# Create your models here.
