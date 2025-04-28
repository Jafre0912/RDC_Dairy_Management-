from django.shortcuts import render
from .models import Cattle, Report

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def cattle_view(request):
    cattle = Cattle.objects.all()
    return render(request, 'dashboard/cattle.html', {'cattle': cattle})

def reports_view(request):
    reports = Report.objects.all()
    return render(request, 'dashboard/reports.html', {'reports': reports})
