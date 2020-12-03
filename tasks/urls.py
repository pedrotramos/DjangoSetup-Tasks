from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_post),
    path("<int:task_id>", views.get_put_del),
]
