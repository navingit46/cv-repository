from django.urls import path,include
from cv_app import views


urlpatterns = [
    #path('',views.home,name='home'),
    path('skills/',views.skills,name='skills'),
    path('exp/',views.experience,name='experience'),
    path('about/',views.about,name='about'),
]
