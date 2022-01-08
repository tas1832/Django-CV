
from django.contrib import admin
from .models import  ProfileBasic, ProfileCertification, ProfileEducation, ProfileExperience, ProfileProjects, ProfileSkills
# Register your models here.
admin.site.register(ProfileBasic)
admin.site.register(ProfileEducation)
admin.site.register(ProfileExperience)
admin.site.register(ProfileProjects)
admin.site.register(ProfileCertification)
admin.site.register(ProfileSkills)
