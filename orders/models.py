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


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food_item = models.ForeignKey(foodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.food_item.name} x {self.quantity}"
    
class User(models.Model):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('manager', 'Manager'),
    ]

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # hashed password
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"