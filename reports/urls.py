from django.urls import path
from .views import AgeReportView, SalaryReportView

urlpatterns = [
    path('employees/age/', AgeReportView.as_view(), name='age-report'),
    path('employees/salary/', SalaryReportView.as_view(), name='salary-report')
]