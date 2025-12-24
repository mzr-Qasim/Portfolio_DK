

# Register your models here.
from django.contrib import admin
from .models import heroSection, aboutSection

# -----------------------------
# Pricing Section Admin
# -----------------------------
@admin.register(heroSection)
class MainHeroSectionAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'profession_1', 'profession_2', 'profile_picture')



@admin.register(aboutSection)
class AboutSectionAdmin(admin.ModelAdmin): 
    list_display = ('who_i_am', 'what_i_do', 'about_picture', 'learn_more', 'cv')