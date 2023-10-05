
from django.db import models
from django.contrib.auth.models import User
from users.models import Instructor

class Course(models.Model):
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField()
    image = models.ImageField(upload_to="img/product", null=True, blank=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    #course=models.ForeignKey(Course,on_delete=models.CASCADE)
    module_number=models.IntegerField()
    category=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField()
    price = models.DecimalField(max_digits=8,null=True, decimal_places=2)
    instructor = models.ForeignKey(Instructor,null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="img/product", null=True, blank=True)
    file=models.FileField(upload_to='files/product',null=True,blank=True)

    def __str__(self):
        return self.title
