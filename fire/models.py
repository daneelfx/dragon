from django.contrib.gis.db import models


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    based = models.PointField(null=True)
