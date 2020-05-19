from django.db import models
import datetime


class Family(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nAdults = models.IntegerField(default=0)
    nUnder12 = models.IntegerField(default=0)
    nAbove12 = models.IntegerField(default=0)
    nMeals = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MeetingDate(models.Model):
    submission_date = models.DateField()
    family = models.ManyToManyField(Family)
    def __str__(self):
        return self.submission_date.strftime('%d/%m/%Y')

class IntermediateRecord(models.Model):
    submission_date = models.DateField()
    name = models.CharField(max_length=100)
    nAdults = models.IntegerField(default=0)
    nUnder12 = models.IntegerField(default=0)
    nAbove12 = models.IntegerField(default=0)

    def __str__(self):
        return self.submission_date.strftime('%d/%m/%Y')
