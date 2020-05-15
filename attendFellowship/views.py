from django.shortcuts import render, redirect
from .forms import NewFamilyForm, MeetingDateForm, ShowUpForm, TodayDateForm
from .models import Family, MeetingDate
import datetime


def home(request):
    showPeople = False
    today = datetime.date.today()
    if MeetingDate.objects.filter(submission_date=today).exists():
        showPeople = True
    families = Family.objects.all()
    if request.method == 'POST':
        form = TodayDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        context = {}
        context['showPeople'] = showPeople
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

def show_up(request, id):
    family = Family.objects.get(id=id)
    today = datetime.date.today()
    print(today)
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
