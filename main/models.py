from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.



class siteLogo(models.Model):
    site_logo = models.ImageField(help_text="Site Logo" ,upload_to='images/')
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