from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "completed")
    list_filter = ("user", "completed")
    search_fields = ("title", "user")
    list_editable = ("completed",)

    def user(self, obj):
        """Get username from foreign key."""
        return obj.user.username
