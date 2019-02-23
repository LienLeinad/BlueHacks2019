from django.shortcuts import render
from django.http import HttpResponse
from .models import Day
from .models import Plans
# Create your views here.
def index(request):
    day_list = Day.objects.order_by('time_stamp')[0:]
    plan_list = Plans.objects.order_by('time_start')[0:]
    context = {'day_list': day_list, 'plan_list': plan_list }
    return render(request, 'index.html', context)