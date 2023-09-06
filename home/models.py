from django.db import models


# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length=50,verbose_name='first name')
    lname = models.CharField(max_length=50,verbose_name='last name')
    email = models.EmailField(max_length=50,unique=True,null=True)
    bdate = models.DateField(verbose_name='birth date',null=True)
    img = models.ImageField(upload_to='media/person/',null=True)

    def __str__(self) -> str:
        return self.fname
    
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

class Project(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    link = models.CharField(max_length=50,null=True)
    desc = models.TextField(verbose_name="Description",null=True)
    created_at = models.DateField(verbose_name="Careted At",null=True)
    img = models.ImageField(upload_to='media/project/',null=True)

    def __str__(self) -> str:
        return self.user.fname + self.name

class Education(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE,null=True)
    degree = models.CharField(max_length=50,null=True)
    university = models.CharField(max_length=50,null=True)
    started_at = models.DateField(null=True)
    ended_at = models.DateField(null=True)
    img = models.ImageField(upload_to='media/education/',null=True)
    

    def __str__(self) -> str:
        return f"{self.user.fname} {self.university}"
    

class Skill(models.Model):
    user = models.ForeignKey(Person,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='media/skill/',null=True)


    def __str__(self) -> str:
        return f"{self.user} {self.name}"