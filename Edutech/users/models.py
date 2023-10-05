from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    instructor_name=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)

    def __str__(self):
        return self.instructor_name
