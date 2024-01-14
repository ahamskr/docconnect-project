from rest_framework import serializers
from job.models import *
from profiles.models import Organisation
from users.serializers import UserSerializerGet
# from doctodo_connect.settings import MEDIA_URL


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = JobCategory
        fields = ('id', 'category_name', 'status')


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('__all__')


class JobVacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = JobVacancy
        fields = ('__all__')


class JobVacancyGetSerializer(serializers.ModelSerializer):
    job_category = CategorySerializer()
    city = CitySerializer()
    user = UserSerializerGet()
    organisation = serializers.SerializerMethodField()

    class Meta:
        model = JobVacancy
        fields = ('__all__')

    def get_organisation(self, obj):
        try:
            org = Organisation.objects.filter(user=obj.user.id).values()
            # if org and obj.out_source == False:
            #     # if 'logo' in org[0]:
            #     #     if org[0]['logo'] is not None:
            #     #         org[0]['logo'] = MEDIA_URL + org[0]['logo']
            return org[0]
            # else:
            #     return {}
        except:
            return {}


class JobApplySerializer(serializers.ModelSerializer):
    job_post = JobVacancyGetSerializer()

    class Meta:
        model = JobApply
        fields = ('__all__')


class JobApplyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApply
        fields = ('__all__')
