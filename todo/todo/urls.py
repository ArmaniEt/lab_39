"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from webapp.views import task_view, create_view, delete_view, edit_view, edit_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_view, name='index'),
    path('create', create_view, name='create'),
    path('task/<int:task_pk>/delete', delete_view, name='delete'),
    path('task/<int:task_pk>/edit', edit_view, name='edit'),
    path('task/<int:task_pk>/edit_task', edit_task, name='edit_task')
]
