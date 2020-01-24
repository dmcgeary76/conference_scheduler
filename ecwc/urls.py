"""ecwc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from ecwc_sessions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home_view'),
    path('home/', views.home_view, name='home_view'),
    path('create/', views.create_session_view, name='create_session_view'),
    path('list/', views.list_all_view, name='list_all_view'),
    path('list/<ts>', views.list_all_view, name='list_all_view'),
    path('details/', views.details_view, name='details_view'),
    path('details/<int:pk>', views.details_view, name='details_view'),
    path('delete/<int:pk>', views.delete_choice_view, name='delete_choice_view'),
    path('delete_session/<int:pk>', views.delete_session_view, name='delete_session_view'),
    path('edit/', views.edit_session_view, name='edit_session_view'),
    path('edit/<int:pk>', views.edit_session_view, name='edit_session_view'),
    path('accounts/', include('django.contrib.auth.urls'))
]
