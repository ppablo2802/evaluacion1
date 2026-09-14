from django.http import HttpResponse

def vista_tres(request):
    return HttpResponse("<h1>Hola desde la Vista 1 de App 2</h1>")

def vista_cuatro(request):
    return HttpResponse("<h1>Hola desde la Vista 2 de App 2</h1>")