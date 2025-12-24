from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
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
    about_picture = models.ImageField(upload_to='images/', blank=True)
    learn_more = models.CharField(max_length=40, help_text="learn more link button name", blank=True, default='')
    cv = models.FileField(
        help_text="PDF Format",
        upload_to='cvs/',
        validators=[FileExtensionValidator(['pdf'])], blank=True
        )


    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"