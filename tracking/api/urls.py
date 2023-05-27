from django.urls import path
from .views import CompanyList,CompanytDetail,EmployeeList,EmployeetDetail,DeviceList,DeviceDetail

urlpatterns = [
    path('company/', CompanyList.as_view(), name='company-list'),
    path('company/<int:pk>/', CompanytDetail.as_view(), name='company-detail'),
    path('employee/', EmployeeList.as_view(), name='employee-list'),
    path('employee/<int:pk>/', EmployeetDetail.as_view(), name='employee-detail'),
    path('device/', DeviceList.as_view(), name='device-list'),
    path('device/<int:pk>/', DeviceDetail.as_view(), name='device-detail'),
]