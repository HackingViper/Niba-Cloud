from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("acceuil", views.acceuil, name="acceuil"),
    path("archives/<str:slug>/", views.archives, name="archives"),
]