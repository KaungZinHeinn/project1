from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    name = models.CharField(max_length=200)
    note = models.TextField()
    des = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name