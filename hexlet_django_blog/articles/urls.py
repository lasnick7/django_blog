from django.urls import path

from hexlet_django_blog.articles import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:article_id>/", views.show_article, name='show_article')
]