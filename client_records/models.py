from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class LSERecord(models.Model):
    CLUB_CHOICES = [
        ('Afternoon Club', 'Afternoon Club'),
        ('Holiday Club', 'Holiday Club'),
    ]

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    counselor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    club_type = models.CharField(max_length=20, choices=CLUB_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class HCTRecord(models.Model):
    RESULT_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ]

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    counselor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES)
    tb_tested = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"