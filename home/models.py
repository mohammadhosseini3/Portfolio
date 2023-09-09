from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=100,null=True)
    link = models.CharField(max_length=50,blank=True,null=True)
    desc = models.TextField(verbose_name="Description",null=True)
    img = models.ImageField(upload_to='project/',blank=True,null=True)
    created_at = models.DateField(verbose_name="Careted At",null=True)

    def __str__(self) -> str:
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=50,null=True)
    university = models.CharField(max_length=50,null=True)
    started_at = models.DateField(null=True)
    ended_at = models.DateField(null=True)
    img = models.ImageField(upload_to='education/',blank=True,null=True)


    def __str__(self) -> str:
        return f"{self.degree} {self.university}"
    

class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    thumbnail = models.ImageField(upload_to='article/thumbnail/',null=True,blank=True)
    summary = models.CharField(max_length=500,null=True)
    content = models.TextField(max_length=500,null=True)

    def __str__(self) -> str:
        return f"title :{self.title}"
      

class Person(models.Model):
    fname = models.CharField(max_length=50,verbose_name='first name',blank=True,null=True)
    lname = models.CharField(max_length=50,verbose_name='last name',blank=True,null=True)
    email = models.EmailField(max_length=50,unique=True,null=True)
    bdate = models.DateField(verbose_name='birth date',null=True)
    skill = models.ManyToManyField(Skill,blank=True)
    project = models.ManyToManyField(Project,blank=True)
    article = models.ManyToManyField(Article,blank=True)
    education = models.ManyToManyField(Education,blank=True)
    img = models.ImageField(upload_to='person/',blank=True,null=True)


    def __str__(self) -> str:
        return self.fname
    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'