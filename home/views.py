from rest_framework.response import Response
from django.http import JsonResponse
from .models import Person
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status

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

@api_view(['GET','PUT','DELETE'])
def person_detail(request,id):
    try:
        person = Person.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
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