from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from restapi.models import Company,Employee
from restapi.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        company=self.get_object()
        employees=Employee.objects.filter(company=company)
        serializer=EmployeeSerializer(employees,many=True,context={'request': request})
        return Response(serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 