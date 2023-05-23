from django.db import models


# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=250)
    Password = models.CharField(max_length=260)

    def __str__(self):
        return self.Name
