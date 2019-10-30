from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.loginPage, name="login"),
    path('log_user',views.loginUser, name="logUser"),
    path('api/get_posts', views.getArticles, name="get_posts"),
    path('api/get_post', views.getArticle, name="get_post"),
    path('api/add_post', views.addArticle, name="add_post")
]