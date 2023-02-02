import datetime

from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from testapp.validator import validate_file_size


# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



class Student_reg(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',null=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    phone_no = models.IntegerField()
    age = models.IntegerField(default=0)
    image = models.FileField(upload_to="images",validators=[validate_file_size])

    def age(self):
        age = datetime.date.today() - self.dob
        return int((age).days/365.25)


    def __str__(self):
       return self.name


class Admin_reg(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='admin',null=True)
    name = models.CharField(max_length=200)
    dob = models.DateField()
    phone_no = models.IntegerField()

    def __str__(self):
       return self.name


class MARK(models.Model):
    name = models.ForeignKey(Student_reg,on_delete=models.CASCADE)
    english = models.IntegerField(validators=[MaxValueValidator(50)])
    maths = models.IntegerField(validators=[MaxValueValidator(50)])
    chemistry = models.IntegerField(validators=[MaxValueValidator(50)])
    physics = models.IntegerField(validators=[MaxValueValidator(50)])
    totalmark = models.IntegerField(validators=[MaxValueValidator(200)])
    total = models.IntegerField(default=0)

    def __str__(self):
       return self.name + self.total
    def total(self):
        self.total=self.english+self.maths+self.chemistry+self.physics
        return self.total