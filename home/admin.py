from django.contrib import admin
from .models import Person,Project,Education,Skill,Article,ProjectTag,Image,WorkedAt

# Register your models here.
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Article)
admin.site.register(ProjectTag)
admin.site.register(WorkedAt)
admin.site.register(Image)
