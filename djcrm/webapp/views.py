from django.shortcuts import render
from .models import Lead


def home(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "webapp/index.html", context)
