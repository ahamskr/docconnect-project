from rest_framework import serializers
from profiles.models import *


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = ('__all__')


class ConferenceLicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConferenceLicense
        fields = ('__all__')


class ExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ('__all__')


class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = ('__all__')


class ResumeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = ('__all__')
