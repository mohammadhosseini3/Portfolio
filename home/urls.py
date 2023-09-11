from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('people/',views.people_list),
    path('people/<int:id>/',views.person_detail),

    path('articles/',views.article_list),
    path('article/<int:id>/',views.artcile_detail),

    path('skills',views.skill_list),
    path('skills/<int:id>/',views.skill_detail),

    path('education/',views.education_list),
    path('educations/<int:id>/',views.education_detail),

    path('projects/',views.project_list),
    path('projects/<int:id>/',views.project_detail),

    path("worked-at/",views.worked_at),
    path("worked-at/<int:id>/",views.worked_at_detail),

    path("images/",views.image_list),
    path("images/<int:id>/",views.image_detail),
]