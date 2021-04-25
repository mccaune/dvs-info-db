
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('add', views.add, name="add"),
    path('single_object/<object_id>', views.single_object, name="single_object"),
    path('search_objects', views.search_objects, name="search_objects"),
    path('update_object/<object_id>', views.update_object, name="update_object"),
    path('delete_object/<object_id>', views.delete_object, name="delete_object"),
    path('statistics', views.statistics, name="statistics"),
    path('test', views.test, name="test"),
]