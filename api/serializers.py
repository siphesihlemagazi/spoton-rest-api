from rest_framework import serializers
from api.models import subjects, grades, Material


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
