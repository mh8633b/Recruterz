from django.db import models

# Create your models here.


class job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    experince = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.title
