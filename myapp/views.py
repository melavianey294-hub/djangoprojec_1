from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hellow World</h1>")


def about_view(request):
    return HttpResponse("Página About")

def nombre(request):
    return HttpResponse("Melissa Bolaños")