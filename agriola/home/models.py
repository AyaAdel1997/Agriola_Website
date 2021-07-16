from django.db import models

# Create your models here.
"""class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/")
    #image2 = models.ImageField(upload_to='img/')
    def __str__(self):
        return self.caption """

class Imagemodel(models.Model) :
    #name = models.CharField(max_length=100)
    images = models.FileField(upload_to='img/', blank=True)