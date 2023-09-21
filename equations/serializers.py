from equations.models import Vehicle, Parking
from rest_framework import serializers


class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ['max_spaces', 'address']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['parking', 'car_registration', 'color', 'size', 'KMs_for_liter']
