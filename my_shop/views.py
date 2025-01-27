from django.shortcuts import render

# Create your views here.
def home(request):
    print("hyyyyyyyy homeeeeeee")
    return render(request, 'home.html')