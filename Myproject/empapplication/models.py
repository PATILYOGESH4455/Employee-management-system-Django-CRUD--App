
from django.db import models


class Employee (models.Model):
    id = models.AutoField(primary_key=True)
    Employee_id = models.IntegerField()
    First_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=40)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=10)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.First_name






