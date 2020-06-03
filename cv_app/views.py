from django.shortcuts import render
from cv_app.models import Jobs

# Create your views here.
def home(request):
    jobs=Jobs.objects
    return render(request,'cv_app/home.html',{'jobs':jobs})


def skills(request):
    return render(request,'cv_app/skills.html')

def experience(request):
    return render(request,'cv_app/experience.html')

def about(request):
    return render(request,'cv_app/about.html')
