from django.shortcuts import render, redirect
from .forms import NewFamilyForm, MeetingDateForm, ShowUpForm, TodayDateForm
from .models import Family, MeetingDate, IntermediateRecord
import datetime
from django.db import connection

sql_s1 = "insert into 'attendFellowship_intermediaterecord' (id, submission_date, name, nAdults, nUnder12, nAbove12) select null, submission_date, name, nAdults, nUnder12, nAbove12 "
sql_s2 = "from attendFellowship_meetingdate inner join attendFellowship_meetingdate_family "
sql_s3 = "on attendFellowship_meetingdate.id = attendFellowship_meetingdate_family.meetingdate_id "
sql_s4 = "inner join attendFellowship_family "
sql_s5 = "on attendFellowship_family.id = attendFellowship_meetingdate_family.family_id;"


def home(request):
    try:
        max_date = MeetingDate.objects.latest('submission_date')
    except:
        max_date = "awaiting data"
    families = Family.objects.all()
    if request.method == 'POST':
        MeetingDate.objects.all().delete()
        form = TodayDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {}
    context['max_date'] = max_date
    context['form'] = TodayDateForm()
    context['families'] = families
    return render(request, 'home.html', context)

def new_family(request):
    if request.method == 'POST':
        form = NewFamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = NewFamilyForm()
    return render(request, 'new_family.html', {'form':form})

def show_up(request, name):
    family = Family.objects.get(name=name)
    if request.method == 'POST':
        showForm = ShowUpForm(request.POST, instance=family)
        if showForm.is_valid():
            showForm.save()
            return redirect("/")
    else:
        context = {}
        context['family'] = family
        context['showUpForm'] = ShowUpForm(initial={'name': family.name})
    return render(request, 'show_up.html', context)

def intermediate_record(request):
    currentRecord = IntermediateRecord.objects.all()
    max_date = MeetingDate.objects.latest('submission_date')
    context = {}
    context['dateForm'] = MeetingDateForm()
    context['currentRecord'] = currentRecord
    context['max_date'] = max_date
    if request.method == 'POST':
        dateForm = MeetingDateForm(request.POST, instance=max_date)
        if dateForm.is_valid():
            dateForm.save()
        with connection.cursor() as cursor:
            res = cursor.execute(sql_s1+sql_s2+sql_s3+sql_s4+sql_s5)
        return redirect('intermediate_record.html')
    else:
        return render(request, 'intermediate_record.html', context)

def reset_record(request):
    families = Family.objects.all()
    context = {}
    context['families'] = families
    if request.method == 'POST':
        for family in families:
            # reset all family attendence number to 0 in family table
            Family.objects.filter(name=family.name).update(nAdults=0)
            Family.objects.filter(name=family.name).update(nUnder12=0)
            Family.objects.filter(name=family.name).update(nAbove12=0)
            Family.objects.filter(name=family.name).update(nMeals=0)
        return redirect('reset_record.html')
    else:
        return render(request, 'reset_record.html', context)
