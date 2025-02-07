from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length= 300)
    receipe_description = models.CharField(max_length= 600)
    receipe_image = models.ImageField(upload_to= "receipe")

    def __str__(self):
        return self.receipe_name