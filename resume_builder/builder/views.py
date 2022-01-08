

from django.forms.formsets import INITIAL_FORM_COUNT, MAX_NUM_FORM_COUNT, TOTAL_FORM_COUNT
from django.forms.models import inlineformset_factory
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
import pdfkit
import io





from builder.models import ProfileBasic, ProfileCertification, ProfileEducation, ProfileExperience, ProfileProjects, ProfileSkills


from .forms import ProfileFormBasic, ProfileFormCertification, ProfileFormEducation, ProfileFormExperience, ProfileFormProjects, ProfileFormSkills, UserRegister
# from .forms import UserForm


# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        username = request.user.username
        context = {'username': username}
    return render(request, 'index.html',context)

def loginPage(request):
    context = {}
    if request.method == 'POST':
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        user = authenticate(request, username = user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "login failed")
            # context = {'messages': messages}
    return render(request, 'login.html', context)

def register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Profile created" + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)

def templatesPage(request):
    return render(request, 'templates.html')

def logoutPage(request):
    logout(request)
    return redirect('home')
def viewProfile(request, pk):
    # print(request.user)
    # user = User.objects.get(username=pk)
    # if request.user.is_authenticated:
    profile = ProfileFormBasic(instance = request.user.profilebasic)
    print(request.user.profilebasic)
    # Education Formset
    # formset_education_class = inlineformset_factory(ProfileBasic,ProfileEducation, form=ProfileFormEducation, can_delete=False, extra=1)
    # # formset_education = formset_education_class(prefix='education', instance=form_basic)
    # formset_education = formset_education_class(prefix='education', instance = profile)
    # print(formset_education)
    # profile_education = ProfileEducation.objects.filter(id = request.user.profilebasic) =
    profile_education =ProfileEducation.objects.filter(person = request.user.profilebasic)

    print(profile_education)

    # # Experience Formset
    # formset_experience_class = inlineformset_factory(ProfileBasic,ProfileExperience, form=ProfileFormExperience, can_delete=False, extra=1,max_num= 4)
    # # formset_experience = formset_experience_class(prefix='experience', instance=form_basic)
    # formset_experience = formset_experience_class(prefix='experience', instance = profile)

    # # Project Formset
    # formset_project_class = inlineformset_factory(ProfileBasic,ProfileProjects, form=ProfileFormProjects, can_delete=False, extra=1,max_num=6)
    # # formset_projects = formset_project_class(prefix='project', instance=request.user)
    # formset_projects = formset_project_class(prefix='project', instance = profile)

    # # Certification Formset
    # formset_certification_class = inlineformset_factory(ProfileBasic,ProfileCertification, form=ProfileFormCertification, can_delete=False, extra=1,max_num=6)
    # # formset_certifications = formset_certification_class(prefix='certification', instance=request.user)
    # formset_certifications = formset_certification_class(prefix='certification', instance = profile)

    # # Skills form
    # formset_skill_class = inlineformset_factory(ProfileBasic,ProfileSkills, form=ProfileFormSkills, can_delete=False, extra=1, max_num=6)
    # # formset_skills = formset_skill_class(prefix='skill', instance=request.user)
    # formset_skills = formset_skill_class(prefix='skill', instance = profile)

    # context = {'pk':pk, 'profile':profile, 'form_education':formset_education, 
    #     'formset_experience':formset_experience, 'formset_projects':formset_projects, 
    #     'formset_certifications':formset_certifications, 'formset_skills': formset_skills}
    return render(request, 'viewProfile.html',  context={'profile':profile, 'profile_education': profile_education})

# @login_required
def profilePage(request, pk):
# def profilePage(request):

    # form = ProfileForm()
    context={}
    if request.user.is_authenticated:
        
        firstname = request.user.first_name
    
        form_basic = ProfileFormBasic(instance=request.user.profilebasic)
        # form_basic = ProfileFormBasic()
        # Education Formset
        number_education =ProfileEducation.objects.filter(person = request.user.profilebasic).count()
        profile_education={}
        if number_education== 0:
            # number_education =1
            number_education =0
        else:
            profile_education =ProfileEducation.objects.filter(person = request.user.profilebasic).values()
            # print(profile_education)
        formset_education_class = inlineformset_factory(ProfileBasic,ProfileEducation, form=ProfileFormEducation, can_delete=True, extra=number_education)
        # formset_education = formset_education_class(prefix='education', instance=form_basic)
        formset_education = formset_education_class(initial = profile_education,prefix='education')
        # print(formset_education)

        # Experience Formset
        number_experience =ProfileExperience.objects.filter(person = request.user.profilebasic).count()
        profile_experience={}
        if number_experience== 0:
            # number_experience =1
            number_experience =0
        else:
            profile_experience =ProfileExperience.objects.filter(person = request.user.profilebasic).values()
        formset_experience_class = inlineformset_factory(ProfileBasic,ProfileExperience, form=ProfileFormExperience, can_delete=True, extra=number_experience,max_num= 4)
        # formset_experience = formset_experience_class(prefix='experience', instance=form_basic)
        formset_experience = formset_experience_class(initial = profile_experience,prefix='experience')

        # Project Formset
        number_project =ProfileExperience.objects.filter(person = request.user.profilebasic).count()
        profile_project={}
        if number_project== 0:
            # number_project =1
            number_project =0
        else:
            profile_project =ProfileProjects.objects.filter(person = request.user.profilebasic).values()
        formset_project_class = inlineformset_factory(ProfileBasic,ProfileProjects, form=ProfileFormProjects, can_delete=False, extra=number_project,max_num=6)
        # formset_projects = formset_project_class(prefix='project', instance=request.user)
        formset_projects = formset_project_class(initial = profile_project,prefix='project')

        # Certification Formset
        number_certification =ProfileCertification.objects.filter(person = request.user.profilebasic).count()
        profile_certification={}
        if number_certification== 0:
            # number_certification =1
            number_certification =0
        else:
            profile_certification =ProfileCertification.objects.filter(person = request.user.profilebasic).values()
        formset_certification_class = inlineformset_factory(ProfileBasic,ProfileCertification, form=ProfileFormCertification, can_delete=False, extra=number_certification,max_num=6)
        # formset_certifications = formset_certification_class(prefix='certification', instance=request.user)
        formset_certifications = formset_certification_class(initial = profile_certification, prefix='certification')

        # Skills form
        number_skill =ProfileSkills.objects.filter(person = request.user.profilebasic).count()
        profile_skill={}
        if number_skill== 0:
            # number_skill =1
            number_skill =0
        else:
            profile_skill =ProfileSkills.objects.filter(person = request.user.profilebasic).values()
        formset_skill_class = inlineformset_factory(ProfileBasic,ProfileSkills, form=ProfileFormSkills, can_delete=False, extra=number_skill, max_num=6)
        # formset_skills = formset_skill_class(prefix='skill', instance=request.user)
        formset_skills = formset_skill_class(initial = profile_skill,prefix='skill')
        
        context = {'pk':pk, 'form_basic':form_basic, 'formset_education':formset_education, 'firstname':firstname,
        'formset_experience':formset_experience, 'formset_projects':formset_projects, 
        'formset_certifications':formset_certifications, 'formset_skills': formset_skills}

    if request.method == "POST":
        # print(request.POST.cleaned_data)
        person_form = ProfileFormBasic(request.POST, instance=request.user.profilebasic)
 
        person_education = formset_education_class(request.POST, prefix='education', instance=request.user.profilebasic)
        person_experience = formset_experience_class(request.POST, prefix= 'experience', instance=request.user.profilebasic)
        person_projects = formset_project_class(request.POST, prefix='project', instance=request.user.profilebasic)
        person_certifications = formset_certification_class(request.POST, prefix='certification', instance=request.user.profilebasic)
        person_skills = formset_skill_class(request.POST, prefix='skill', instance=request.user.profilebasic)
        print(person_form.is_valid())
        print(person_education.is_valid())
        print(person_projects.is_valid())
        print(person_certifications.is_valid())
        print(person_skills.is_valid())
        print(person_experience.is_valid())
        print(person_education)

        if all([person_form.is_valid(), person_education.is_valid(), person_experience.is_valid(), person_projects.is_valid(), person_certifications.is_valid(), person_skills.is_valid()]):
            print("=====in the if Statement=======")
            instances_education = person_education.save(commit=False)
            # for instance_education in instances_education:
            #     instance_education.user = request.user.profilebasic
            #     instance_education.save()
            print(person_education)
            # person = person_form.save()
            person_form.save()
            # person_education = formset_education_class(request.POST, prefix='education', instance= person)
            # person_experience = formset_experience_class(request.POST, prefix= 'experience', instance= person)
            # person_projects = formset_project_class(request.POST, prefix='project', instance= person)
            # person_certifications = formset_certification_class(request.POST, prefix='certification', instance= person)
            # person_skills = formset_skill_class(request.POST, prefix='skill', instance= person)
            person_education.save()
            person_experience.save()
            person_projects.save()
            person_certifications.save()
            person_skills.save()

            messages.success(request, "Profile updated" )
            return redirect('home')
        else:
            print("Profile Saving failed")


    return render(request, 'profile.html', context)

def resume(request):
    path_wkhtmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
    form_basic = ProfileFormBasic(instance=request.user.profilebasic)
    # form_basic = ProfileFormBasic()
    # Education Formset
    number_education =ProfileEducation.objects.filter(person = request.user.profilebasic).count()
    # print("education number ", number_education)
    profile_education={}
    if number_education!= 0:
  
        profile_education =ProfileEducation.objects.filter(person = request.user.profilebasic).values()
    #     # print(profile_education)
    formset_education_class = inlineformset_factory(ProfileBasic,ProfileEducation, form=ProfileFormEducation, can_delete=True, extra=number_education)
    # formset_education = formset_education_class(prefix='education', instance=form_basic)
    formset_education = formset_education_class(initial = profile_education,prefix='education')
    # print(formset_education)

    # Experience Formset
    number_experience =ProfileExperience.objects.filter(person = request.user.profilebasic).count()
    profile_experience={}
    if number_experience== 0:
        # number_experience =1
        number_experience =0
    else:
        profile_experience =ProfileExperience.objects.filter(person = request.user.profilebasic).values()
    formset_experience_class = inlineformset_factory(ProfileBasic,ProfileExperience, form=ProfileFormExperience, can_delete=True, extra=number_experience,max_num= 4)
    # formset_experience = formset_experience_class(prefix='experience', instance=form_basic)
    formset_experience = formset_experience_class(initial = profile_experience,prefix='experience')

    # Project Formset
    number_project =ProfileExperience.objects.filter(person = request.user.profilebasic).count()
    profile_project={}
    if number_project== 0:
        # number_project =1
        number_project =0
    else:
        profile_project =ProfileProjects.objects.filter(person = request.user.profilebasic).values()
    formset_project_class = inlineformset_factory(ProfileBasic,ProfileProjects, form=ProfileFormProjects, can_delete=False, extra=number_project,max_num=6)
    # formset_projects = formset_project_class(prefix='project', instance=request.user)
    formset_projects = formset_project_class(initial = profile_project,prefix='project')

    # Certification Formset
    number_certification =ProfileCertification.objects.filter(person = request.user.profilebasic).count()
    profile_certification={}
    if number_certification== 0:
        # number_certification =1
        number_certification =0
    else:
        profile_certification =ProfileCertification.objects.filter(person = request.user.profilebasic).values()
    formset_certification_class = inlineformset_factory(ProfileBasic,ProfileCertification, form=ProfileFormCertification, can_delete=False, extra=number_certification,max_num=6)
    # formset_certifications = formset_certification_class(prefix='certification', instance=request.user)
    formset_certifications = formset_certification_class(initial = profile_certification, prefix='certification')

    # Skills form
    number_skill =ProfileSkills.objects.filter(person = request.user.profilebasic).count()
    profile_skill={}
    if number_skill== 0:
        # number_skill =1
        number_skill =0
    else:
        profile_skill =ProfileSkills.objects.filter(person = request.user.profilebasic).values()
    formset_skill_class = inlineformset_factory(ProfileBasic,ProfileSkills, form=ProfileFormSkills, can_delete=False, extra=number_skill, max_num=6)
    # formset_skills = formset_skill_class(prefix='skill', instance=request.user)
    formset_skills = formset_skill_class(initial = profile_skill,prefix='skill')
        
    context = {'form_basic':form_basic, 'formset_education':formset_education,
    'formset_experience':formset_experience, 'formset_projects':formset_projects, 
    'formset_certifications':formset_certifications, 'formset_skills': formset_skills}
    template = loader.get_template('resume.html')
    html = template.render(context)
    print(html)
    options = {
        'page-size':'Letter',
        'encoding': 'UTF-8',
    }
    
    pdf =pdfkit.from_string(html, False, options, configuration=config)
    
    response = HttpResponse(pdf, content_type='application/pdf')
   
    response['Content-Disposition']='attachment'
    filename='resume.pdf'
    return response

