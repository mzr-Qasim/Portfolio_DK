from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.



class siteLogo(models.Model):
    site_logo = models.ImageField(help_text="Site Logo" ,upload_to='images/')
    footer_logo = models.ImageField(help_text="Footer Logo" ,upload_to='images/', null=True)
    fav_icon_ico = models.ImageField(help_text="fav icon ico" ,upload_to='images/', null=True)
    fav_icon_32_png = models.ImageField(help_text="fav icon 32x32 png" ,upload_to='images/', null=True)
    fav_icon_16_png = models.ImageField(help_text="fav icon 16x16 png" ,upload_to='images/', null=True)
    class Meta:
        verbose_name = "Site Logo"
        verbose_name_plural = "Site Logo"


class heroSection(models.Model):
    first_name = models.CharField(max_length=20, help_text="First Name", blank=True, default='')
    last_name = models.CharField(max_length=20, help_text="Last Name", blank=True)
    profession_1 = models.CharField(max_length=30, help_text="Profession_1", blank=True)
    profession_2 = models.CharField(max_length=30, help_text="Profession_2", blank=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True)


    class Meta:
        verbose_name = "Main Hero Section"
        verbose_name_plural = "Main Hero Section"


class aboutSection(models.Model):
    who_i_am = models.TextField(help_text="Who I Am", blank=True, default='')
    what_i_do = models.TextField( help_text="What I Do", blank=True, default='')
    about_picture = models.ImageField(help_text="About Section Image", upload_to='images/')
    learn_more = models.CharField(max_length=40, help_text="learn more link button name", blank=True, default='')
    cv = models.FileField(
        help_text="PDF Format",
        upload_to='cvs/',
        validators=[FileExtensionValidator(['pdf'])], blank=True
        )


    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"


class servicesSection(models.Model):
    service_title = models.CharField(max_length=40, help_text="Service Title", blank=True, default='')
    service_info = models.TextField(help_text="Service Information", blank=True, default='')
    service_img = models.ImageField(upload_to='Service Image')


    class Meta:
        verbose_name = "Services Section"
        verbose_name_plural = "Services Section"






class blogsSection(models.Model):
    author_name = models.CharField(max_length=50, help_text="Blog Author Name", default='')
    created_at = models.DateTimeField(auto_now_add=True)
    blog_title = models.TextField(help_text="Blog Title", default='')
    blog_img = models.ImageField(upload_to='Blog Image', help_text="Blog Image")


    class Meta:
        verbose_name = "Blogs Section"
        verbose_name_plural = "Blogs Section"

class BlogParagraph(models.Model):
    blog = models.ForeignKey(blogsSection, on_delete=models.CASCADE, related_name='paragraphs')
    content = models.TextField(help_text="Blog Paragraph")

    class Meta:
        verbose_name = "Blog Paragraph"
        verbose_name_plural = "Blog Paragraphs"

    def __str__(self):
        return self.content[:50]  # show first 50 chars




class SkillsSection(models.Model):
    skill_name = models.CharField(max_length=60, help_text="Skill Name", blank=True)
    skill_percent = models.PositiveIntegerField(help_text="Skill Percent (0–100)")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class LanguageSection(models.Model):
    language_name = models.CharField(max_length=60, help_text="Language Name", blank=True)
    language_percent = models.PositiveIntegerField(help_text="Language Percent (0–100)")

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


class ContactInfo(models.Model):
    email_address = models.EmailField(
        max_length=254, # Recommended max length for emails
        unique=True,    # Ensures no duplicate emails in the database
        blank=False,    # Makes the field required in forms and admin
        null=False,     # Makes the database column non-nullable
        help_text="Required. A valid email address."
    )
    location_description_1= models.CharField(max_length=350, blank=False, help_text="Add Street, Society")
    location_description_2= models.CharField(max_length=350, blank=False, help_text="Add City, Country" )
    map_location = models.TextField(help_text="Add Google Maps Geolocation")
    contact_availability = models.TextField(help_text="Your Contact Availability Information", null=True)
    linkedin_link = models.TextField(help_text="Add Linkedin Link", null=True)
    instagram_link = models.TextField(help_text="Add Instagram", null=True)
    youtube_link = models.TextField(help_text="Add Youtube Link", null=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"


class Timeline(models.Model):
    start_year = models.PositiveIntegerField(help_text="Starting Year")
    end_year = models.PositiveIntegerField(help_text="Ending Year")
    institute_university_name = models.CharField(max_length=300, help_text="Institute University Name")
    degree_role = models.CharField(max_length=300, help_text="What You Did")


    class Meta:
        verbose_name = "Timeline"
        verbose_name_plural = "Timeline"



class TimelineExperience(models.Model):
    timeline = models.ForeignKey(
        Timeline, 
        on_delete=models.CASCADE, 
        related_name='experiences',
        help_text="Select the timeline this experience belongs to"
    )
    title = models.CharField(max_length=350, help_text="Title of the experience or achievement")
    description = models.TextField(help_text="Describe what you did", blank=True)
    start_year = models.PositiveIntegerField(help_text="Starting Year", null=True)
    end_year = models.PositiveIntegerField(help_text="Ending Year", null=True)

    class Meta:
        verbose_name = "Timeline Experience"
        verbose_name_plural = "Timeline Experiences"

    def __str__(self):
        return self.title



class PresentationSection(models.Model):
    title = models.CharField(max_length=350, help_text="Enter Presentation Title")
    presentation_image = models.ImageField(help_text="Upload Presentation Image", upload_to='images/')
    presentation_link = models.TextField(help_text="Enter Presentation Link")

    class Meta:
        verbose_name = "Presentation Section"
        verbose_name_plural = "Presentation Section"


class ProjectSkillsCounter(models.Model):
    title = models.CharField(max_length=350, help_text="Enter Presentation Title")
    value = models.PositiveIntegerField(help_text="Enter Project/Experience Value")

    class Meta:
        verbose_name = "Project Skills Counter Section"
        verbose_name_plural = "Project Skills Counter Section"



   

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)  # vimeo, youtube, modalbox

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    
    thumbnail = models.ImageField(upload_to='portfolio/thumbs/')
    image = models.ImageField(upload_to='portfolio/images/', blank=True)

    video_url = models.URLField(blank=True)  # vimeo / youtube / soundcloud

    client = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    is_modal = models.BooleanField(default=False)

    def __str__(self):
        return self.title
