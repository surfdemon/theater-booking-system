from django.contrib import admin
from .models import Signup

# Register your models here.


@admin.register(Signup)
class Signup(admin.ModelAdmin):
    """
    Admin view for the Signup model.
    """
    list_display = ['fname', 'email', 'created_at']
    search_fields = ['fname', 'email']
    ordering = ['-created_at']
