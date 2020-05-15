from django.contrib import admin

from .models import Family
from .models import MeetingDate

@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name', 'nAdults', 'nUnder12', 'nAbove12', 'nMeals']


@admin.register(MeetingDate)
class MeetingDateAdmin(admin.ModelAdmin):
    list_display = ['submission_date']
