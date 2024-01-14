from rest_framework.decorators import api_view
from rest_framework.response import Response
from job.serializers import *
from job.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


class JobVacancyList(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = JobVacancyGetSerializer
    queryset = JobVacancy.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['role', 'functional_area',
    #                     'industry_type', 'city', 'is_part_time', 'job_category', 'salary', 'max_salary']

    filterset_fields = {
        'salary': ['gte', 'exact'],
        'max_salary': ['gte', 'lte', 'exact'],
        'role': ['exact'],
        'functional_area': ['exact'],
        'industry_type': ['exact'],
        'is_part_time': ['exact'],
        'job_category': ['exact'],
        'city': ['exact'],

    }

    # renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = JobVacancy.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = JobVacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user,
                            organisation_name=self.request.user.name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobVacancyDetailed(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk, user):
        try:
            return JobVacancy.objects.get(pk=pk, user=user)
        except JobVacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job_post = self.get_object(pk, self.request.user.id)
        serializer = JobVacancyGetSerializer(job_post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job_post = self.get_object(pk, self.request.user.id)
        serializer = JobVacancySerializer(
            job_post, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job_post = self.get_object(pk, self.request.user.id)
        job_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer
    queryset = JobCategory.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category_name', 'status']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = JobCategory.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailed(APIView):

    def get_object(self, pk):
        try:
            return JobCategory.objects.get(pk=pk)
        except JobCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CityList(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CitySerializer
    queryset = City.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city_name', 'status']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = City.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CityDetailed(APIView):

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(
            city, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JobPostGet(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return JobVacancy.objects.get(pk=pk)
        except JobVacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job_post = self.get_object(pk)
        serializer = JobVacancyGetSerializer(job_post)
        return Response(serializer.data)


class JobApplyList(ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = JobApplySerializer
    queryset = JobApply.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['job_post', 'id']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = JobApply.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = JobApplyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobApplyDetailed(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk, user):
        try:
            return JobApply.objects.get(pk=pk, user=user)
        except JobApply.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        job_apply = self.get_object(pk, self.request.user.id)
        serializer = JobApplySerializer(job_apply)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job_apply = self.get_object(pk, self.request.user.id)
        serializer = JobApplyCreateSerializer(
            job_apply, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job_apply = self.get_object(pk, self.request.user.id)
        job_apply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicantsRecieved(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        org = self.request.query_params.get('org', None)
        applicants = JobApply.objects.filter(job_post__user=org).values(
            'id', 'user', 'user__name', 'user__email', 'user__contact', 'job_post__organisation_name', 'job_post__job_category__category_name', 'created_at', 'job_post__user__organisation__registered_name', 'job_post__role')

        return Response(applicants, status=status.HTTP_200_OK)
