from django.shortcuts import render

from rest_framework import generics
from .models import *
from .serializers import *

class DepartmentListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

  


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'

class SubDepartmentListView(generics.ListCreateAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer

class SubDepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
    lookup_field = 'pk'

class ReportListView(generics.ListCreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'

class SubReportListView(generics.ListCreateAPIView):
    queryset = ReportSubDepartment.objects.all()
    serializer_class = ReportsSubDepartmentSerializer

class SubReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReportSubDepartment.objects.all()
    serializer_class = ReportsSubDepartmentSerializer
    lookup_field = 'pk'

class SubDepartmentListCreate(generics.ListCreateAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer

class SubDepartmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubDepartment.objects.all()
    serializer_class = SubDepartmentSerializer
    lookup_field = 'pk'


