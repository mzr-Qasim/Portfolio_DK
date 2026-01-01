

# Register your models here.
from django.contrib import admin
from .models import siteLogo, heroSection, aboutSection, servicesSection, blogsSection, BlogParagraph, SkillsSection, LanguageSection, ContactInfo, Timeline, TimelineExperience, PresentationSection, ProjectSkillsCounter, PortfolioItem, PortfolioCategory

# -----------------------------
# Pricing Section Admin
# -----------------------------
@admin.register(siteLogo)
class SiteLogoAdmin(admin.ModelAdmin): 
    list_display = ('site_logo','footer_logo','fav_icon_ico','fav_icon_32_png','fav_icon_16_png')


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




@admin.register(SkillsSection)
class SkillsSectionAdmin(admin.ModelAdmin): 
    list_display = ('skill_name','skill_percent')


@admin.register(LanguageSection)
class LanguageSectionAdmin(admin.ModelAdmin): 
    list_display = ('language_name','language_percent')



@admin.register(ContactInfo)
class LocationSectionAdmin(admin.ModelAdmin): 
    list_display = ('email_address','location_description_1','location_description_2','map_location','contact_availability','linkedin_link','instagram_link','youtube_link')



class TimelineExperienceInline(admin.TabularInline):
    model = TimelineExperience
    extra = 1

@admin.register(Timeline)
class TimelineSectionAdmin(admin.ModelAdmin): 
    list_display = ('start_year','end_year','institute_university_name','degree_role')
    inlines = [TimelineExperienceInline]



@admin.register(PresentationSection)
class PresentationSectionAdmin(admin.ModelAdmin): 
    list_display = ('title','presentation_image','presentation_link')


@admin.register(ProjectSkillsCounter)
class ProjectSkillsCounterAdmin(admin.ModelAdmin): 
    list_display = ('title','value')




admin.site.register(PortfolioCategory)
admin.site.register(PortfolioItem)