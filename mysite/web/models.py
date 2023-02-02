from django.db import models
  


# Create your models here.
class Employee(models.Model):
    Employee_id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=250)
    email =models.CharField(max_length=250)
    age =models.IntegerField()
    location =models.CharField(max_length=250)
    def _str_(self):
        return self.name
