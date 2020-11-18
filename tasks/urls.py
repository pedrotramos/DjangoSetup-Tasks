from django.urls import path
from . import views

urlpatterns = [
    path("listAll", views.get_tasks, name="TaskList"),
    path("<int:task_id>", views.get_task, name="Task"),
    path("add", views.add_task, name="AddTask"),
    path("alter/<int:task_id>", views.alter_ask, name="AlterTask"),
    path("remove/<int:task_id>", views.remove_task, name="RemoveTask"),
]
