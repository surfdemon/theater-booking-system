from django import forms
from .models import BookingTable

class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model = BookingTable
        fields = ['numberOfTickets']
        labels = {
            'numberOfTickets': 'Number of tickets',
        }