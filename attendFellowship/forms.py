from django import forms
from .models import Family
from .models import MeetingDate
import datetime

def dynamicChoice():
    family_name=[]
    final_tuple=[]
    count=1
    for family in list(Family.objects.filter(nAdults__gte=1)):
        family_name.append(family.name)
    for name in family_name:
        final_tuple.append((str(count),name))
        count+=1
    return final_tuple
class MeetingDateForm(forms.ModelForm):
    # print(list(Family.objects.filter(nAdults__gte=1)))

    # print(list(Family.objects.filter(nAdults__gte=1))[0].name)
    submission_date = forms.DateField(widget=forms.SelectDateWidget(), label="Attendence date")
    family = forms.MultipleChoiceField(choices = dynamicChoice)
    class Meta:
        model = MeetingDate
        fields = {'submission_date', 'family'}

class TodayDateForm(forms.ModelForm):
    submission_date = forms.DateField(widget=forms.SelectDateWidget(), label="today_date")
    class Meta:
        model = MeetingDate
        fields = {'submission_date'}

class NewFamilyForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    class Meta(object):
        model = Family
        fields = ("name",)

class ShowUpForm(forms.ModelForm):
    nAdults = forms.IntegerField(label='Adults')
    nUnder12 = forms.IntegerField(label='Kid 0-12 yo')
    nAbove12 = forms.IntegerField(label='Youth over 12 yo')
    nMeals = forms.IntegerField(label='How many will join the dinner(Adult+Youth)')
    class Meta(object):
        model = Family
        fields = ("nAdults", "nUnder12", "nMeals")
