from rest_framework import serializers
from data.models import *

class ExperienceSARSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceSAR
        fields = ['index', 'statement']

class ExperienceSerializer(serializers.ModelSerializer):
    experience_sars = ExperienceSARSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = ['company', 'title', 'start_date', 'end_date', 'designation', 'experience_sars']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project