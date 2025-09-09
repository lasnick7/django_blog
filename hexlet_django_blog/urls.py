"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.views import IndexPageView
from hexlet_django_blog import views
from django.views.generic.base import TemplateView

handler404 = 'hexlet_django_blog.views.page_not_found_view'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('articles/', include('hexlet_django_blog.articles.urls'), name='articles'),
    path('redirect/', views.redirect, name='index_redirect'),
    path('categories/', include('hexlet_django_blog.categories.urls'), name='categories'),
    path('admin/', admin.site.urls),
]
