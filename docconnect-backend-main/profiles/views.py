from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EducationSerializer
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.renderers import JSONRenderer

# Create your views here.


class EducationList(ListAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['start_date', 'end_date', 'college_name', 'degree']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Education.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationDetailed(APIView):

    def get_object(self, pk, user):
        try:
            return Education.objects.get(pk=pk, user=user)
        except Education.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        eduaction = self.get_object(pk, self.request.user.id)
        serializer = EducationSerializer(eduaction)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        eduaction = self.get_object(pk, self.request.user.id)
        serializer = EducationSerializer(
            eduaction, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        eduaction = self.get_object(pk, self.request.user.id)
        eduaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ConferenceLicenseList(ListAPIView):
    serializer_class = ConferenceLicenseSerializer
    queryset = ConferenceLicense.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['start_date', 'end_date',
                        'title', 'issuing_organisation']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = ConferenceLicense.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ConferenceLicenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConferenceLicenseDetailed(APIView):

    def get_object(self, pk, user):
        try:
            return ConferenceLicense.objects.get(pk=pk, user=user)
        except ConferenceLicense.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        conference_license = self.get_object(pk, self.request.user.id)
        serializer = ConferenceLicenseSerializer(conference_license)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        conference_license = self.get_object(pk, self.request.user.id)
        serializer = ConferenceLicenseSerializer(
            conference_license, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        conference_license = self.get_object(pk, self.request.user.id)
        conference_license.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExperienceList(ListAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'employment_type',
                        'start_date', 'end_date', 'location', 'company_name']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Experience.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExperienceDetailed(APIView):

    def get_object(self, pk, user):
        try:
            return Experience.objects.get(pk=pk, user=user)
        except Experience.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        experience = self.get_object(pk, self.request.user.id)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        experience = self.get_object(pk, self.request.user.id)
        serializer = ExperienceSerializer(
            experience, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        experience = self.get_object(pk, self.request.user.id)
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrganisationList(ListAPIView):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['registered_name', 'contact']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Organisation.objects.all().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganisationDetailed(APIView):

    def get_object(self, pk):
        try:
            return Organisation.objects.get(pk=pk)
        except Organisation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Organisation = self.get_object(pk)
        serializer = OrganisationSerializer(Organisation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Organisation = self.get_object(pk)
        serializer = OrganisationSerializer(
            Organisation, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Organisation = self.get_object(pk)
        Organisation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResumeList(ListAPIView):
    serializer_class = ResumeSerializer
    queryset = Resume.objects.all()
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['created_at', 'id']

    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        queryset = Resume.objects.filter(
            user=self.request.user.id).order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResumeDetailed(APIView):

    def get_object(self, pk, user):
        try:
            return Resume.objects.get(pk=pk, user=user)
        except Resume.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        resume = self.get_object(pk, self.request.user.id)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        resume = self.get_object(pk, self.request.user.id)
        serializer = ResumeSerializer(
            resume, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        resume = self.get_object(pk, self.request.user.id)
        resume.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
