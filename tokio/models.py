from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        return self.firstName + ' ' + self.lastName