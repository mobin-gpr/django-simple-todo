from django.urls import path
from .views import TaskList, TaskCreate, TaskComplete, TaskDelete

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create", TaskCreate.as_view(), name="task_create"),
    path("completed/<int:pk>", TaskComplete.as_view(), name="task_completed"),
    path("delete/<int:pk>", TaskDelete.as_view(), name="task_delete"),
]
