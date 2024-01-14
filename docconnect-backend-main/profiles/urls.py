from django.urls import path
from .views import *


urlpatterns = [

    path('eduaction/', EducationList.as_view()),
    path('eduaction/<pk>/', EducationDetailed.as_view()),
    path('conference-license/', ConferenceLicenseList.as_view()),
    path('conference-license/<pk>/', ConferenceLicenseDetailed.as_view()),
    path('experience/', ExperienceList.as_view()),
    path('experience/<pk>/', ExperienceDetailed.as_view()),
    path('orgainsation/', OrganisationList.as_view()),
    path('orgainsation/<pk>/', OrganisationDetailed.as_view()),
    path('resume/', ResumeList.as_view()),
    path('resume/<pk>/', ResumeDetailed.as_view()),


]
