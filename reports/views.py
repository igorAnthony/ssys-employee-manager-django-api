# reports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from .serializers import AgeReportResponseSerializer, SalaryReportResponseSerializer
from datetime import datetime
from rest_framework.permissions import IsAuthenticated

class AgeReportView(APIView):
    permission_classes = [IsAuthenticated]    

    def get(self, request):
        current_year = datetime.now().year
        employees = Employee.objects.all()
        younger_employee = employees.order_by('-birth_date').first()
        older_employee = employees.order_by('birth_date').first()

        total_age = 0
        total_employees = employees.count() 
        for employee in employees:
            total_age += current_year - employee.birth_date.year
        
        average_age = total_age / total_employees if total_employees > 0 else 0

        younger_employee_data = EmployeeSerializer(younger_employee).data
        older_employee_data = EmployeeSerializer(older_employee).data

        report = {
            "younger": younger_employee_data,
            "older": older_employee_data,
            "average": average_age
        }

        serializer = AgeReportResponseSerializer(data=report)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaryReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        employees = Employee.objects.all()

        lowest_salary_employee = employees.order_by('salary').first()
        highest_salary_employee = employees.order_by('-salary').first()

        total_salary = 0
        total_employees = employees.count()
        for employee in employees:
            total_salary += employee.salary
        
        average_salary = total_salary / total_employees if total_employees > 0 else 0

        lowest_salary_employee_data = EmployeeSerializer(lowest_salary_employee).data
        highest_salary_employee_data = EmployeeSerializer(highest_salary_employee).data

        report = {
            "lowest": lowest_salary_employee_data,
            "highest": highest_salary_employee_data,
            "average": average_salary
        }

        serializer = SalaryReportResponseSerializer(data=report)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)