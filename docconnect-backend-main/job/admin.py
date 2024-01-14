from django.contrib import admin
from job.models import *

# Register your models here.
admin.site.register(JobVacancy)
admin.site.register(JobCategory)
admin.site.register(City)
admin.site.register(JobApply)
