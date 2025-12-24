# Create your views here.
from django.shortcuts import render
from main.models import heroSection, aboutSection

# Create your views here.
def home(request):
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    

    context={
        'hero_section':hero_section,
        'about_section':about_section,
    }
    return render(request, 'index.html', context)  



def about(request):
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    

    context={
        'hero_section':hero_section,
        'about_section':about_section,
    }
    return render(request, 'about.html', context)  