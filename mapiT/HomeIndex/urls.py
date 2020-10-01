from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexHomePageRender, name="IndexHome"),
    path('loginTest')
]
