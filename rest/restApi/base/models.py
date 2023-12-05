from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self) -> str:
        return super().__str__()


