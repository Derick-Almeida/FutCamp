from rest_framework import serializers
from .models import Coach

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'

    def create(self,validated_data):
        return Coach.objects.create(**validated_data)
        


    