from django.db import models

# Create your models here.
class Band(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_band = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']