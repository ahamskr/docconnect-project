from django.urls import path
from job.views import *


urlpatterns = [


    path('job-post/', JobVacancyList.as_view()),
    path('job-post/<pk>/', JobVacancyDetailed.as_view()),
    path('category/', CategoryList.as_view()),
    path('category/<pk>/', CategoryDetailed.as_view()),
    path('city/', CityList.as_view()),
    path('city/<pk>/', CityDetailed.as_view()),
    path('job-post-get/<pk>/', JobPostGet.as_view()),
    path('job-apply/', JobApplyList.as_view()),
    path('job-apply/<pk>/', JobApplyDetailed.as_view()),

    path('applicants-recieved/', ApplicantsRecieved.as_view()),

]
