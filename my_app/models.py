from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=True)
    experience = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='teacher')
    
    def __str__(self):
        return self.user.username
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    parents_phone_number = models.CharField(max_length=100)
    telegram_link = models.CharField(max_length=500)
    address = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    
    def __str__(self):
        return self.user.username