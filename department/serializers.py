from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDepartment
        fields = '__all__'
    def to_representation(self, instance):
        rep = super(SubDepartmentSerializer, self).to_representation(instance)
        rep['department'] = instance.department.name
        return rep


class ReportSerializer(serializers.ModelSerializer):
    # department = serializers.CharField(source='department.name', read_only=True)
    class Meta:
        model = Reports
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(ReportSerializer, self).to_representation(instance)
        rep['department'] = instance.department.name
        return rep

class ReportsSubDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportSubDepartment
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super(ReportsSubDepartmentSerializer, self).to_representation(instance)
        rep['sub_department'] = instance.sub_department.name
        return rep

        

