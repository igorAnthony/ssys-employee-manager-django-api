from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%d-%m-%Y", input_formats=["%Y-%m-%d", "%d-%m-%Y"])
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department', 'salary', 'birth_date']