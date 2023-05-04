from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','name','type','organisation']
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance    