from django.http import HttpResponse

def index(request):
    return HttpResponse("esta en la app MY CARS!!!")
