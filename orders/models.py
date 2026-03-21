from django.db import models

# Create your models here.
class foodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    def __str__(self):
        return self.name