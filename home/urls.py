from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('people_list/',views.people_list),
    path('person/<int:id>/',views.person_detail),

    path('article_list/',views.article_list),
    path('article/<int:id>/',views.artcile_detail),

    path('skill_list/',views.skill_list),
    path('skill/<int:id>/',views.skill_detail),

    path('education_list/',views.education_list),
    path('education/<int:id>/',views.education_detail),

    path('project_list/',views.project_list),
    path('project/<int:id>/',views.project_detail)
]