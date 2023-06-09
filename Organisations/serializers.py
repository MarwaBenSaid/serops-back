from rest_framework import serializers
from .models import Organisations

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        fields = ['name','website']
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance    