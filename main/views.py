# Create your views here.
from django.shortcuts import render
from main.models import siteLogo, heroSection, aboutSection, servicesSection, blogsSection, SkillsSection, LanguageSection, ContactInfo, Timeline, TimelineExperience, PresentationSection, ProjectSkillsCounter, PortfolioCategory, PortfolioItem

# Create your views here.
def home(request):
    site_logo = siteLogo.objects.all()
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    service_section = servicesSection.objects.all()
    portfolio_items = PortfolioItem.objects.select_related('category')
    categories = PortfolioCategory.objects.all()
    blog_section = blogsSection.objects.all()
    contact_info = ContactInfo.objects.all()
    

    context={
        'site_logo': site_logo,
        'hero_section':hero_section,
        'about_section':about_section,
        'service_section': service_section,
        'portfolio_items': portfolio_items,
        'categories': categories,
        'blog_section': blog_section,
        'contact_info': contact_info,
    }
    return render(request, 'index.html', context)  



def about(request):
    site_logo = siteLogo.objects.all()
    hero_section = heroSection.objects.all()
    about_section = aboutSection.objects.all()
    skills_section = SkillsSection.objects.all()
    languages_section = LanguageSection.objects.all()
    for lang in languages_section:
        lang.percent_decimal = lang.language_percent / 100  # new attribute
    timeline_section = Timeline.objects.all()
    timeline_experience_section = TimelineExperience.objects.all()
    presentation_section = PresentationSection.objects.all()
    project_skills_counter_section = ProjectSkillsCounter.objects.all()
    contact_info = ContactInfo.objects.all()
    

    context={
        'site_logo': site_logo,
        'hero_section':hero_section,
        'about_section':about_section,
        'skills_section':skills_section,
        'languages_section':languages_section,
        'timeline_section':timeline_section,
        'timeline_experience_section':timeline_experience_section,
        'presentation_section':presentation_section,
        'project_skills_counter_section':project_skills_counter_section,
        'contact_info': contact_info,
    }
    return render(request, 'about.html', context)  