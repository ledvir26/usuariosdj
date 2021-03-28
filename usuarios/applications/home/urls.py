from django.contrib import admin
from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path('panel/', views.HomePages.as_view(), name='panel'),
    path('mixin/', views.TemplatePruebaView.as_view(), name='mixin'),
]
