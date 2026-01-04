from django.http import HttpResponse

def simple_form(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse(f"Hello {name}")
    return HttpResponse("Please enter your name in URL")
