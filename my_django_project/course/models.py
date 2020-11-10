from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=45, null=False)
    type = models.CharField(max_length=45, null=False)
    price = models.CharField(max_length=45, null=False)
    image = models.FileField(upload_to='static/images/course')
