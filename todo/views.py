from django.http import Http404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from todo.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import TodoCreateForm


class TaskList(LoginRequiredMixin, ListView):
    """Task list view."""

    model = Task
    context_object_name = "tasks"
    template_name = "todo/todo_list.html"
    form_class = TodoCreateForm

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    """Create a new task."""

    model = Task
    fields = ["title"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set user field from current suer
        return super(TaskCreate, self).form_valid(form)


class TaskComplete(LoginRequiredMixin, View):
    """Complete a task."""

    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, *args, **kwargs):
        user: User = self.request.user
        object: Task = get_object_or_404(self.model, pk=kwargs.get("pk"))
        if object.user == user:
            object.completed = True
            object.save()
            return redirect(self.success_url)
        else:
            return Http404


class TaskDelete(LoginRequiredMixin, View):
    """Delete a task."""

    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, *args, **kwargs):
        user: User = self.request.user
        object: Task = get_object_or_404(self.model, pk=kwargs.get("pk"))
        if object.user == user:
            object.delete()
            return redirect(self.success_url)
