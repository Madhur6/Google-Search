from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "search1/index.html")

def image(request):
    return render(request, "search1/image.html")

def advance(request):
    return render(request, "search1/advance.html")