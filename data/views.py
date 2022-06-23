from django.shortcuts import render
from data.serializers import *
from data.models import *
from django.http import JsonResponse
# Create your views here.

def experience(request):
    experience_list = Experience.objects.filter(public=True)
    serializer = ExperienceSerializer(experience_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def projects(request):
    project_list = Project.objects.all()
    serializer = ProjectSerializer(project_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def articles(request):
    article_list = Project.objects.all()
    serializer = ProjectSerializer(article_list, many=True)
    return JsonResponse(serializer.data, safe=False)

def main(request):
    return JsonResponse({"message": "Robert Babaev's Resume Data API"})