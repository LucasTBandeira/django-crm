from django.urls import path
from .views import lead_detail, lead_list, lead_create

app_name = "webapp"

urlpatterns = [
    path("", lead_list),
    path("create/", lead_create),
    path("<int:pk>", lead_detail),
]
