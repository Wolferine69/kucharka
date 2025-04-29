from django.http import HttpResponse


def home(request):
    return HttpResponse("Vítej v kuchařce!")  # Dočasná odpověď