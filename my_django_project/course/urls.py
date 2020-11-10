
from django.urls import path
from . import views
urlpatterns = [
    path('create', views.create, name='course.create'), # localhost:8000/admin/course/create
]