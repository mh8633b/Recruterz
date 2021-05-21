from django.db import models

# Create your models here.

# https://vertabelo.com/blog/designing-a-database-for-an-online-job-portal/

class job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    experince = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
