from django.db import models

# Create your models here.

class Type(models.Model):
    type = models.CharField(max_length=50)
    type_description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.type + " " + str(self.price) + " " + self.type_description


class Classes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

