from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "portfolio/home.html", {"page": "home"})