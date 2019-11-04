# -*- coding: utf-8 -*-


from django.db import models

# Create your models here.

class User(models.Model):
    ID = models.CharField(max_length=255)
    User_name = models.CharField(max_length=255)
    Company = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    DATE = models.DateField()
    Device_Serial_Number = models.CharField(max_length = 255)
    
    class Meta:
        db_table = "infinity_user"
    
    # def __str__(self):
    #     return self.User_name