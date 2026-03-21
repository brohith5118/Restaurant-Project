from django.db import models

# Create your models here.
class foodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name