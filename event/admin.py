from django.contrib import admin
from .models import Event, BookingTable

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin view for the Event model.
    """
    list_display = ['name', 'datetime', 'available_tickets', 'price']
    search_fields = ['name', 'datetime']
    list_filter = ['datetime']
    date_hierarchy = 'datetime'
    ordering = ['datetime']


@admin.register(BookingTable)
class EventBookingTable(admin.ModelAdmin):
    """
    Admin view for the BookingTable model.
    """
    list_display = ['event', 'user', 'numberOfTickets']
    search_fields = ['event', 'user']
    list_filter = ['event', 'user']
    ordering = ['event']