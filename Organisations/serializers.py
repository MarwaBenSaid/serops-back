from rest_framework import serializers
from .models import Orgnisation

class OrgnisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orgnisation
        fields = ['name','website']
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance    