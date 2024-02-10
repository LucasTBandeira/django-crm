from django.contrib import admin
from django.urls import path, include
from webapp.views import LandingPageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path("webapp/", include("webapp.urls", namespace="webapp")),
]
