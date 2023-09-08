from rest_framework import serializers
from .models import Person,Skill,Project,Article,Education
from drf_extra_fields.fields import Base64ImageField
from django.shortcuts import get_object_or_404

class SkillSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:    
        model = Skill
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    thumbnail = Base64ImageField(use_url=True,required=False)
    class Meta:
        model = Article
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    img = Base64ImageField(use_url=True,required=False)
    class Meta:
        model = Education
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    skill = SkillSerializer(many=True)
    project = ProjectSerializer(read_only=True,many=True)
    article = ArticleSerializer(read_only=True,many=True)
    education = EducationSerializer(read_only=True,many=True)
    img = Base64ImageField(use_url=True,required=False)

    class Meta:
        model = Person
        fields = '__all__'
    

    # def update(self,instance,validated_data):

    #     skills_data = validated_data.pop('skill')
    #     person = get_object_or_404(Person,pk=instance.id)
    #     print(person.skill)
    #     for person_skill in person.skill:
    #         print(person_skill)
    #     return instance
