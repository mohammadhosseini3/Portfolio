from rest_framework import serializers
from .models import Person,Skill,Project,Article,Education
from drf_extra_fields.fields import Base64ImageField
from drf_writable_nested import WritableNestedModelSerializer

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


class PersonSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    id = serializers.IntegerField()
    skill = SkillSerializer(many=True)
    project = ProjectSerializer(many=True)
    article = ArticleSerializer(many=True)
    education = EducationSerializer(many=True)
    img = Base64ImageField(use_url=True,required=False)

    class Meta:
        model = Person
        fields = '__all__'
