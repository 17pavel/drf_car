from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
