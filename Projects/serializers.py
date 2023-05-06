from rest_framework import serializers
from .models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id','name','type','organisation']
    def create(self,validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance    