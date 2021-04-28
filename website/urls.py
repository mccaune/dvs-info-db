
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    path('add', views.add, name="add"),
    path('add_akb/<object_id>', views.add_akb, name="add_akb"),
    path('single_object/<object_id>', views.single_object, name="single_object"),
    path('search_objects', views.search_objects, name="search_objects"),
    path('update_object/<object_id>', views.update_object, name="update_object"),
    path('update_akum<object_id>', views.update_akum, name="update_akum"),
    path('update_rtu<object_id>', views.update_rtu, name="update_rtu"),
    path('update_raa<object_id>', views.update_raa, name="update_raa"),
    path('delete_object/<object_id>', views.delete_object, name="delete_object"),
    path('delete_akum/<object_id>', views.delete_akum, name="delete_akum"),
    path('delete_rtu/<object_id>', views.delete_rtu, name="delete_rtu"),
    path('delete_raa/<object_id>', views.delete_raa, name="delete_raa"),
    path('statistics', views.statistics, name="statistics"),
    path('test', views.test, name="test"),
]