from rest_framework import serializers
from .models import Servers

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servers
        fields = "__all__"
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance    