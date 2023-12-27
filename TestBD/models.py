from django.db import models

class Students(models.Model):
    student_name = models.CharField(max_length = 100)
    student_surname = models.CharField(max_length = 100)
    student_age = models.IntegerField()
