from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('people_list/',views.people_list),
    path('person/<int:id>/',views.person_detail)
]