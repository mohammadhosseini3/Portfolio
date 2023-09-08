from rest_framework.response import Response
from django.http import JsonResponse
from .models import Person
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
import requests as r
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(["GET","POST"])
def people_list(request):

    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person,many=True)
        return Response({'person':serializer.data})
    

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
@api_view(['GET','PUT','DELETE'])
def person_detail(request,id):

    person = get_object_or_404(Person, pk=id)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET","POST"])
def article_list(request):

    if request.method == 'GET':
        person = Article.objects.all()
        serializer = ArticleSerializer(person,many=True)
        return Response({'article':serializer.data})
    

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def artcile_detail(request,id):

    article = get_object_or_404(Article,pk=id)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(["GET","POST"])
def skill_list(request):

    if request.method == 'GET':
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill,many=True)
        return Response({'skill':serializer.data})
    

    elif request.method == 'POST':
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def skill_detail(request,id):

    skill = get_object_or_404(Skill,pk=id)

    if request.method == 'GET':
        serializer = SkillSerializer(skill)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SkillSerializer(skill,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET","POST"])
def education_list(request):

    if request.method == 'GET':
        skill = Education.objects.all()
        serializer = EducationSerializer(skill,many=True)
        return Response({'education':serializer.data})
    

    elif request.method == 'POST':
        serializer = EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def education_detail(request,id):

    education = get_object_or_404(Education,pk=id)

    if request.method == 'GET':
        serializer = EducationSerializer(education)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EducationSerializer(education,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(["GET","POST"])
def project_list(request):

    if request.method == 'GET':
        skill = Project.objects.all()
        serializer = ProjectSerializer(skill,many=True)
        return Response({'project':serializer.data})
    

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def project_detail(request,id):

    project = get_object_or_404(Project,pk=id)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
