from django.urls import path
from . import views

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('templates', views.templatesPage, name='template'),
    path('resume', views.resume, name='resume'),
    path('logout', views.logoutPage, name='logout'),
    path('profile/@<pk>', views.profilePage, name='profile'),
    path('profile/@<pk>/view-profile', views.viewProfile, name='viewProfile'),

]
# urlpatterns += staticfiles_urlpatterns()
