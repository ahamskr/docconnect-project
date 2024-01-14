from django.db import models
from users.models import User
# Create your models here.


class City(models.Model):
    city_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return str(self.city_name)


class JobCategory(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.BooleanField(default=True, blank=True)

    class Meta:
        db_table = 'job_category'

    def __str__(self):
        return str(self.category_name)


class JobVacancy(models.Model):

    status_choice = (
        ('PENDING', 'pending'),
        ('APPROVED', 'approved'),
        ('EXPIRED', 'expired'),
        ('DELETED', 'deleted')
    )
    organisation_name = models.CharField(max_length=200, blank=True, null=True)
    organisation_logo = models.ImageField(
        upload_to='organisation_logo/', blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    job_category = models.ForeignKey(
        JobCategory, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    functional_area = models.CharField(max_length=200, blank=True, null=True)
    industry_type = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=200, blank=True, null=True)
    perks_and_benifits = models.CharField(
        max_length=200, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    duties = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=100, choices=status_choice, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    salary = models.FloatField(default=0.0, blank=True)
    max_salary = models.FloatField(default=0.0, blank=True)
    description = models.TextField(blank=True, null=True)
    is_part_time = models.BooleanField(default=False)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, blank=True, null=True)
    source_link = models.CharField(max_length=250, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    out_source = models.BooleanField(default=False, blank=True)
    tag = models.TextField(blank=True, null=True)
    is_amount_disclose = models.BooleanField(default=True)

    class Meta:
        db_table = 'job_vacancy'

    def __str__(self):
        return str(self.role) + str("   -   ") + str(self.organisation_name)


class JobApply(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True)
    job_post = models.ForeignKey(
        JobVacancy, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'job_apply'

    def __str__(self):
        return str(self.user) + str(" - ") + str(self.job_post)
