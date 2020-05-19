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
    max_date = MeetingDate.objects.latest('submission_date')
    families = IntermediateRecord.objects.filter(submission_date=max_date.submission_date)
    families_list = Family.objects.all()
    print
    if request.method == 'POST':
        form = TodayDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        context = {}
        context['max_date'] = max_date
        context['form'] = TodayDateForm()
        context['families'] = families
        context['families_list'] = families_list
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

def show_up(request, id):
    family = Family.objects.get(id=id)
    today = datetime.date.today()
    today = MeetingDate.objects.get(submission_date=today)
    if request.method == 'POST':
        showForm = ShowUpForm(request.POST, instance=family)
        dateForm = MeetingDateForm(request.POST, instance=today)
        if showForm.is_valid() and dateForm.is_valid():
            showForm.save()
            dateForm.save()
            return redirect("/")
    else:
        context = {}
        context['family'] = family
        context['showUpForm'] = ShowUpForm(initial={'name': family.name})
        context['dateForm'] = MeetingDateForm()
    return render(request, 'show_up.html', context)

def intermediate_record(request):
    families = Family.objects.all()
    for family in families:
        # reset all family attendence number to 0 in family table
        Family.objects.filter(name=family.name).update(nAdults=0)
        Family.objects.filter(name=family.name).update(nUnder12=0)
        Family.objects.filter(name=family.name).update(nAbove12=0)
    if request.method == 'POST':
        with connection.cursor() as cursor:
            res = cursor.execute(sql_s1+sql_s2+sql_s3+sql_s4+sql_s5)
    currentDay = IntermediateRecord.objects.all()
    context = {}
    context['currentDay'] = currentDay
    return render(request, 'intermediate_record.html', context)
