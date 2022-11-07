from django.db import models

# Create your models here.

#creating Company model
class Company(models.Model):
    company_id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    about = models.TextField(max_length=100)
    type = models.CharField(max_length=100,choices = (('IT','IT'),
                                                      ('NON-IT','NON-IT'),
                                                      ('MOBILE PHONES','MOBILE PHONES')))
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#creating Employee model

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=(('Manager','Manager'),
                                                       ('SDE','SDE'),
                                                       ('PL','PL')))
    
    company = models.ForeignKey(Company,on_delete=models.CASCADE)

