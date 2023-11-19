from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=200)
    number = models.TextField()
    grade = models.TextField()
    create_date = models.DateTimeField()

class Parents(models.Model):
    pname = models.ForeignKey(Students, on_delete=models.CASCADE)
    number = models.TextField()
    create_date = models.DateTimeField()