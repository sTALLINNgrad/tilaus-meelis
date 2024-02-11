from django.urls import path
from tilaus import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]