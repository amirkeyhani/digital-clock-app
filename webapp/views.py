from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
# Create your views here.

def clock(request):
    now = datetime.now()
    format ='%H:%M:%S %p'
    current_time = now.strftime(format)
    current_date = now.strftime('%d-%m-%Y')
    context = {'time': current_time, 'date': current_date}
    return render(request, 'clock.html', context)
    