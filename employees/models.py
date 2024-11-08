from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    birth_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
