from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name="dashboard"),
    path('post',views.index, name="post"),
    path('add_post',views.index, name="add_post")
]