from django.db import models
from users.models import User

# Create your models here.


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    college_name = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=200, blank=True, null=True)
    field_of_study = models.CharField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='education/', blank=True, null=True)

    class Meta:
        db_table = 'eduaction'

    def __str__(self):
        return str(self.user)


class ConferenceLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    issuing_organisation = models.CharField(
        max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'conference_license'

    def __str__(self):
        return str(self.user)


class Experience(models.Model):
    employment_type_choice = (
        ('full-time', 'FULL-TIME'),
        ('part-time', 'PART-TIME'),
        ('self-employed', 'SELF-EMPLOYED'),
        ('internship', 'INTERNSHIP'),
        ('trainee', 'TRAINEE'),
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    title = models.CharField(max_length=200)
    employment_type = models.CharField(
        max_length=100, choices=employment_type_choice, default='full-time')
    company_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'experience'

    def __str__(self):
        return str(self.user)


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        db_table = 'resume'

    def __str__(self):
        return str(self.user)


class Organisation(models.Model):
    registered_name = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(
        upload_to='organisation_logo/', blank=True, null=True)
    complete_address = models.TextField()
    contact = models.CharField(max_length=100)
    contact2 = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, null=True, blank=True, related_name='organisation')

    class Meta:
        db_table = 'organisation'

    def __str__(self):
        return str(self.registered_name)
