from django import forms
from .models import Family
from .models import MeetingDate
import datetime


class MeetingDateForm(forms.ModelForm):
    submission_date = forms.DateField(widget=forms.SelectDateWidget(), label="Attendence date")
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
