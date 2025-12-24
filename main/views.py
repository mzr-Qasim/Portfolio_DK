# Create your views here.
from django.shortcuts import render
from main.models import siteLogo, heroSection, aboutSection, servicesSection, blogsSection

# Create your views here.
def home(request):
    site_logo = siteLogo.objects.all()
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    service_section = servicesSection.objects.all()
    blog_section = blogsSection.objects.all()
    

    context={
        'site_logo': site_logo,
        'hero_section':hero_section,
        'about_section':about_section,
        'service_section': service_section,
        'blog_section': blog_section,
    }
    return render(request, 'index.html', context)  



def about(request):
    site_logo = siteLogo.objects.all()
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    

    context={
        'site_logo': site_logo,
        'hero_section':hero_section,
        'about_section':about_section,
    }
    return render(request, 'about.html', context)  