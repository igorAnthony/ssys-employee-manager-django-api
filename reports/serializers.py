from rest_framework import serializers

from employees.serializers import EmployeeSerializer

class AgeReportResponseSerializer(serializers.Serializer):
    younger = EmployeeSerializer()
    older = EmployeeSerializer()
    average = serializers.FloatField()

    def validate_average(self, value):
        return round(value, 2)

class SalaryReportResponseSerializer(serializers.Serializer):
    lowest = EmployeeSerializer()
    highest = EmployeeSerializer()
    average = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_average(self, value):
        return round(value, 2)