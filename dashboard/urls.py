from django.urls import path
from .views import dashboard_view, cattle_view, reports_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('cattle/', cattle_view, name='cattle'),
    path('reports/', reports_view, name='reports'),
]