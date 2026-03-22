from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    order = models.IntegerField()  # controls display order

    def __str__(self):
        return self.name


class foodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.TextField()
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    