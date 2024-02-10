from django.urls import path
from .views import lead_detail, lead_list, lead_create, lead_update, lead_delete

app_name = "webapp"

urlpatterns = [
    path("", lead_list),
    path("create/", lead_create),
    path("<int:pk>", lead_detail),
    path("<int:pk>/update/", lead_update),
    path("<int:pk>/delete/", lead_delete),
]
