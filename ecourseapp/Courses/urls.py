from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from Courses import views

r = routers.DefaultRouter()
r.register('categories', views.CategoryViewSet, basename='categories')
r.register('courses', views.CourseViewSet, basename='courses')
r.register('lessons', views.LessonViewSet, basename='lessons')
r.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(r.urls))
]