from django.db import models
from random import randint
import os

# Create your models here.

def change_img_name(instance,filename):
    counter = randint(1,1000)
    name = instance.type.lower()
    file_extension = filename.split('.')[-1]
    filename = f"{name}_{counter}.{file_extension}"

    if name == "article_thumbnail":
        name = "article"
        filename = f"{name}_thumbnail_{counter}.{file_extension}"

    return os.path.join(f"{name}", filename)


class Image(models.Model):
    TYPE_CHOICES = (
        ("project","Project"),
        ("article","Article"),
        ("article_thumbnail","Article Thumbnail"),
        ("person","Person"),
    )
    type = models.CharField(max_length=50,choices=TYPE_CHOICES,null=False)
    img = models.ImageField(upload_to=change_img_name,null=False)

    def __str__(self) -> str:
        return str(self.img)


class Skill(models.Model):
    name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class ProjectTag(models.Model):
    name = models.CharField(max_length=50,null=False)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100,null=True)
    link = models.CharField(max_length=50,blank=True,null=True)
    desc = models.TextField(max_length=500,verbose_name="Description",null=True)
    images = models.ManyToManyField(Image,blank=True)
    created_at = models.DateField(verbose_name="Careted At",null=True)
    tag = models.ManyToManyField(ProjectTag,blank=True)

    def __str__(self) -> str:
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=50,null=True)
    university = models.CharField(max_length=50,null=True)
    started_at = models.DateField(null=True)
    ended_at = models.DateField(null=True)

    def __str__(self) -> str:
        return f"{self.degree} {self.university}"
    

class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    images = models.ManyToManyField(Image,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    summary = models.CharField(max_length=500,null=True)
    content = models.TextField(max_length=500,null=True)

    def __str__(self) -> str:
        return f"title :{self.title}"
      

class WorkedAt(models.Model):
    title = models.CharField(max_length=100,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    company_name = models.CharField(max_length=50,null=True)
    description = models.TextField(max_length=500,null=True)

    def __str__(self) -> str:
        return f"{self.company_name}"
    

class Person(models.Model):
    fname = models.CharField(max_length=50,verbose_name='first name',null=False)
    lname = models.CharField(max_length=50,verbose_name='last name',null=False)
    email = models.EmailField(max_length=50,unique=True,null=False)

    biography = models.TextField(max_length=500,null=True,blank=True)
    client_number = models.IntegerField(null=True,blank=True)
    years_of_experience = models.IntegerField(null=True,blank=True)
    bdate = models.DateField(verbose_name='birth date',null=True,blank=True)

    skill = models.ManyToManyField(Skill,blank=True)
    project = models.ManyToManyField(Project,blank=True)
    article = models.ManyToManyField(Article,blank=True)
    education = models.ManyToManyField(Education,blank=True)
    worked_at = models.ManyToManyField(WorkedAt,blank=True)
    images = models.ManyToManyField(Image,blank=True)
    
    instagram_link = models.URLField(max_length=200,null=True,blank=True)
    github_link = models.URLField(max_length=200,null=True,blank=True)
    linkedin_link = models.URLField(max_length=200,null=True,blank=True)


    def __str__(self) -> str:
        return self.fname
    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
