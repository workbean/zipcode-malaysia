from rest_framework import serializers
from ..models import Zipcode


class ZipcodeSerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='get_state_display')
    class Meta:
        model = Zipcode
        read_only_fields = ('zipcode', 'street', 'city', 'state')


class CitySerializer(serializers.ModelSerializer):
    state = serializers.CharField(source='get_state_display')
    class Meta:
        model = Zipcode
        fields = ('zipcode', 'city', 'state')