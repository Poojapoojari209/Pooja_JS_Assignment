from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def show_time(request):
    current_time = datetime.now()
    return render(request, 'time.html', {
        'time': current_time
    })

def name_form(request):
    name = request.GET.get('name')
    return render(request, 'name.html', {
        'name': name
    })