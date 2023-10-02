from django.urls import path
from .views import create_robot
from .views import generate_excel_report

urlpatterns = [
    path('create-robot/', create_robot, name='create-robot'),
    path('generate-excel-report/', generate_excel_report, name='generate-excel-report'),
]