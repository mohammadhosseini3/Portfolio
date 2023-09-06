from django.contrib import admin
from .models import Person,Project,Education,Skill

# Register your models here.
admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
