from django.contrib import admin
from django.urls import path, include
from webapp.views import landing_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', landing_page, name='landing-page'),
    path("webapp/", include("webapp.urls", namespace="webapp")),
]
