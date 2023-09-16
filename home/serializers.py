from rest_framework import serializers
from .models import Person,Skill,Project,Article,Education,WorkedAt,ProjectTag,Image
from drf_extra_fields.fields import Base64ImageField
from drf_writable_nested import WritableNestedModelSerializer


class ImageSerializer(serializers.ModelSerializer):
    img = Base64ImageField(use_url=True)
    class Meta:
        model = Image
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    img = ImageSerializer(many=True,required=False)
    class Meta:    
        model = Skill
        fields = '__all__'


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = "__all__"

class ProjectSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    images = ImageSerializer(many=True,required=False)
    tag = ProjectTagSerializer(many=True,required=False)
    class Meta:
        model = Project
        fields = '__all__'


class ArticleSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    images = ImageSerializer(many=True,required=False)
    class Meta:
        model = Article
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class WorkedAtSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkedAt
        fields = '__all__'


class PersonSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    skill = SkillSerializer(many=True,required=False)
    project = ProjectSerializer(many=True,required=False)
    article = ArticleSerializer(many=True,required=False)
    education = EducationSerializer(many=True,required=False)
    worked_at = WorkedAtSerializer(many=True,required=False)
    images = ImageSerializer(many=True,required=False)

    class Meta:
        model = Person
        fields = '__all__'
