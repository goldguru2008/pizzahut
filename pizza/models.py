from django.db import models

# Create your models here.
class size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Pizza(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)
    size = models.ForeignKey(size, on_delete=models.CASCADE)
