from django.db import models
from django.utils import timezone



# Create your models here.
class File(models.Model):
    name = models.TextField(default="")
    file = models.FileField(upload_to ='')
    hashCode = models.TextField(default="")
    uploaded_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name