from django.urls import path
from . import views

urlpatterns = [
    path("", views.learning_view, name="learning-view"),
]
