from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
# from django.forms import fields
from .models import ProfileBasic, ProfileCertification, ProfileEducation, ProfileExperience, ProfileProjects, ProfileSkills

class UserRegister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1','password2']
        # fields = '__all__'

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields ='__all__'
#         labels = ['First Name','Middle Name', 'Last Name', 'Gender', 'Address Line', 'City', 'State', 'Zip', 'Country',
#             'phone', 'E-mail', 'Education', 'Work Experience', 'Projects', 'Certifications'

#         ]

class ProfileFormBasic(forms.ModelForm):
    class Meta:
        model = ProfileBasic
        exclude =['user']
        # fields ='__all__'
        labels = {'first_name':'First Name','middle_name': 'Middle Name', 'last_name':'Last Name', 'gender':'Gender',
         'street_address':'Address Line', 'city':'City','state': 'State','zip': 'Zip','country': 'Country',
         'phone':'Phone', 'email':'E-mail'}

class ProfileFormEducation(forms.ModelForm):
    class Meta:
        model = ProfileEducation
        fields =('education', 'degree_name', 'year_graduated', 'gpa',)

        labels =  {'education':'School', 'degree_name':'Degree', 'year_graduated':'Graduation Year', 'gpa':'GPA'}

class ProfileFormExperience(forms.ModelForm):
    class Meta:
        model = ProfileExperience
        fields =['company_name', 'position_name', 'date_start', 'date_end', 'responsibilities',]

        labels =  {'company_name':'Company', 'position_name':'Position', 'date_start':'Start Date', 'date_end':'End Date','responsibilities':'Activities'}
        

class ProfileFormProjects(forms.ModelForm):
    class Meta:
        model = ProfileProjects
        fields =['project_title', 'project_description', 'tools_used',]

        labels =  {'project_title':'Project Title', 'project_description':'Project Description', 'tools_used':'Tools'}

class ProfileFormCertification(forms.ModelForm):
    class Meta:
        model = ProfileCertification
        fields =['certificate_title',]

        labels =  {'certificate_title':'Certification'}

class ProfileFormSkills(forms.ModelForm):
    class Meta:
        model = ProfileSkills
        fields =['area', 'tools',]

        # labels =  {'programming_language':'Programming Languages', 'databases':'Databases', 'front_end':'Front End','backend':'Backend', 'version_control':'Version Control' }
        labels =  {'area':'Area', 'tools': 'Tools'}

