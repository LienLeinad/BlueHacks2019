from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Day, Plans
from .forms import DayForm,PlanForm,DayModelForm,PlanModelForm
# Create your views here.
def index(request):
   
   
    if request.method == 'POST':
        day_form = DayModelForm(request.POST)
        if day_form.is_valid():
            print ("VALID DAY FORM YAY")
            day_form.save()
            return redirect(index)
        

    day_list = Day.objects.order_by('day_made')[0:]
    plan_list = Plans.objects.order_by('time_start')[0:]
    day_form = DayModelForm(request.POST)
    context = {'day_list': day_list, 'plan_list': plan_list, 'day_form':day_form }
    return render(request, 'homePage.html', context)

def day_form(request):
    if request.method == "POST":
        form = DayModelForm(request.POST)
        if form.is_valid():
            print("VALID DAY FORM")
            form.save()
    form = DayModelForm()
    context = {'form':form}        
    return render(request,'day_form.html', context)

def plan_form(request):
    if request.method == "POST":
        form = PlanModelForm(request.POST)
        if form.is_valid():
            print("NANAY MO VALID")
            form.save()
    form = PlanModelForm()
    context = {'form':form}
    return render(request,'plan_form.html',context)