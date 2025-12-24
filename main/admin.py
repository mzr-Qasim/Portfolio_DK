

# Register your models here.
from django.contrib import admin
from .models import siteLogo, heroSection, aboutSection, servicesSection, blogsSection, BlogParagraph

# -----------------------------
# Pricing Section Admin
# -----------------------------
@admin.register(siteLogo)
class SiteLogoAdmin(admin.ModelAdmin): 
    list_display = ('site_logo',)


@admin.register(heroSection)
class MainHeroSectionAdmin(admin.ModelAdmin): 
    list_display = ('first_name', 'last_name', 'profession_1', 'profession_2', 'profile_picture')



@admin.register(aboutSection)
class AboutSectionAdmin(admin.ModelAdmin): 
    list_display = ('who_i_am', 'what_i_do', 'about_picture', 'learn_more', 'cv')




@admin.register(servicesSection)
class ServiceSectionAdmin(admin.ModelAdmin): 
    list_display = ('service_title', 'service_info', 'service_img')


class BlogParagraphInline(admin.TabularInline):
    model = BlogParagraph
    extra = 1  # show 1 empty paragraph by default
    min_num = 1 # optional, enforce at least one paragraph
    verbose_name = "Paragraph"
    verbose_name_plural = "Paragraphs"


@admin.register(blogsSection)
class BlogSectionAdmin(admin.ModelAdmin): 
    list_display = ('author_name', 'created_at', 'blog_title', 'blog_img')
    inlines = [BlogParagraphInline]




