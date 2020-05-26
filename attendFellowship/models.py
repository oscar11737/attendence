from django.db import models
import datetime

def get_attendence():
    print(dir(Family.objects.filter(nAdults__gte=1)))
    print(Family.objects.filter(nAdults__gte=1).values())
    print([Family.objects.get(nAdults=1).pk])
    return [Family.objects.get(nAdults=1).pk]


class Family(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nAdults = models.IntegerField(default=0)
    nUnder12 = models.IntegerField(default=0)
    nAbove12 = models.IntegerField(default=0)
    nMeals = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class MeetingDate(models.Model):
    submission_date = models.DateField(unique=True)
    family = models.ManyToManyField(Family)
    def __str__(self):
        return self.submission_date.strftime('%Y-%m-%d')

class IntermediateRecord(models.Model):
    submission_date = models.DateField()
    name = models.CharField(max_length=100)
    nAdults = models.IntegerField(default=0)
    nUnder12 = models.IntegerField(default=0)
    nAbove12 = models.IntegerField(default=0)

    def __str__(self):
        return self.submission_date.strftime('%d/%m/%Y')
