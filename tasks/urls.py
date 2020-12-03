from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_tasks, name="TaskList"),
    path("<int:task_id>", views.get_task, name="Task"),
    path("", views.add_task, name="AddTask"),
    path("<int:task_id>", views.alter_task, name="AlterTask"),
    path("<int:task_id>", views.remove_task, name="RemoveTask"),
]
