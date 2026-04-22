from rest_framework import serializers
from .models import Commend

class CommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commend
        fields = '__all__'