from rest_framework import serializers
from .models import Robot

class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = ('model', 'version', 'created')