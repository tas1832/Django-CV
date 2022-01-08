# from typing_extensions import Required
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.dispatch import receiver  # add this
from django.db.models.signals import post_save  # add this


class ProfileBasic(models.Model):
    # gender
    female = "F"
    male = "M"
    other = "Other"
    # Name
    # user_name = models.CharField(max_length=12,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=[(
        female, "Female"), (male, "Male"), (other, "Other")])

    # Contact Information
    street_address = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=40)
    zip = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    # later modify code to divide phone area in area code, country code etc
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ProfileBasic.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profilebasic.save()


class ProfileEducation(models.Model):
    # Education
    # later improve it to dynamically add another field

    education = models.CharField(max_length=200)
    degree_name = models.CharField(max_length=150)
    year_graduated = models.CharField(max_length=4, blank=True, null=True)
    gpa = models.DecimalField(
        max_digits=3, decimal_places=2, blank=True, null=True)
    person = models.ForeignKey(ProfileBasic, on_delete=CASCADE)


class ProfileExperience(models.Model):
    company_name = models.CharField(max_length=200)
    position_name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    responsibilities = models.TextField(max_length=300, blank=True, null=True)
    person = models.ForeignKey(ProfileBasic, on_delete=CASCADE)


class ProfileProjects(models.Model):
    project_title = models.CharField(max_length=150)
    project_description = models.TextField(max_length=300)
    tools_used = models.TextField(max_length=200)
    person = models.ForeignKey(ProfileBasic, on_delete=CASCADE)


class ProfileCertification(models.Model):
    certificate_title = models.CharField(max_length=150)
    person = models.ForeignKey(ProfileBasic, on_delete=CASCADE)


class ProfileSkills(models.Model):
    area = models.CharField(max_length=100)
    tools = models.TextField(max_length=250)
    person = models.ForeignKey(ProfileBasic, on_delete=CASCADE)
