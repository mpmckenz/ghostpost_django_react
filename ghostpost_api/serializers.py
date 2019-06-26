from rest_framework import serializers
from .models import BoastOrRoast


class BoastOrRoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoastOrRoast
        fields = '__all__'
