from django.http import HttpResponse
from django_excel_to_response import ExcelResponse
from .models import Robot
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RobotSerializer

@api_view(['POST'])
def create_robot(request):
    serializer = RobotSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def generate_excel_report(request):
    robot_data = get_weekly_production_summary()


    summary_dict = {}
    for robot in robot_data:
        model = robot['model']
        version = robot['version']
        count = robot['count']

        if model not in summary_dict:
            summary_dict[model] = []

        summary_dict[model].append({'version': version, 'count': count})


    excel_data = []
    for model, versions in summary_dict.items():
        sheet_data = [['Модель', 'Версия', 'Количество за неделю']]
        for version_info in versions:
            sheet_data.append([model, version_info['version'], version_info['count']])

        excel_data.append({
            'sheet_name': model,  # Имя страницы
            'data': sheet_data  # Данные для страницы
        })

    response = ExcelResponse(excel_data, output_name='weekly_production_summary.xlsx')


    response['Content-Disposition'] = 'attachment; filename=weekly_production_summary.xlsx'

    return response


def get_weekly_production_summary():

    data = [
        {'model': 'R2', 'version': 'D2', 'count': 32},
        {'model': 'R2', 'version': 'A1', 'count': 41},
        # И тд...
    ]
    return data