from rest_framework import serializers
from .models import Projects, Profile
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField()
    class Meta:
        model = Projects
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    #projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_pic', 'bio', 'phone_number', 'projects']

    def create(self, validated_data):
        try:
            projects_data = validated_data.pop('projects')
            profile = Profile.objects.create(**validated_data)
            for project_data in projects_data:
                Projects.objects.create(profile=profile, **project_data)
            return profile
        except KeyError:
            projects_data = None
            profile = Profile.objects.create(**validated_data)
            return profile