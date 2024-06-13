from django.views.generic import ListView
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin, ListView):
    """Task list view."""
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        self.model.objects.filter(user=self.request.user)