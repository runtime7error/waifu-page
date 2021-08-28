from rest_framework import serializers
from core.models import Waifu


class WaifuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waifu
        fields = '__all__'
