from django.db import models

# Create your models here.
class Waifu(models.Model):
    alt = models.CharField(max_length=64)
    imageUrl = models.URLField(max_length=384)

    def __str__(self):
        return self.alt
