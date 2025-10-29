from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=500)
    published_at = models.CharField(max_length=255)

    def __str__(self):
        return self.title