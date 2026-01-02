from django.shortcuts import render

def add(request):
    result = None

    if request.method == 'POST':
        num1 = int(request.POST.get('number1'))
        num2 = int(request.POST.get('number2'))
        result = num1 + num2

    return render(request, 'add.html', {'result': result})

