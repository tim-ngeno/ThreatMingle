from django.urls import path
from . import views

urlpatterns = [
    path("", views.risk_assessment_view, name="risk-assessment"),
    path("results/", views.risk_results_view, name="risk-results"),
]
