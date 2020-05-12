from rest_framework import serializers
from .models import cart,cart_item


class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields='__all__'