from django.db import models

# Create your models here.

class ImageCollections(models.Model):

    category_choices = (
        ('animal','Animal'),
        ('scenary','Scenary'),
        ('cars','Cars'),
        ('bike','Bikes')
    )

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length = 255, choices = category_choices)
    img = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length = 1000)

    def __str__(self):
        return str(self.id) + " " + self.description





