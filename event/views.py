from django.shortcuts import render
from django.views import generic, View
from .models import Event, BookingTable

# Create your views here.


class EventHome(View):
    def get(self, request):
        return render(request, 'event/home.html')


class EventList(generic.ListView):
    model = Event
    template_name = "event/events.html"
    context_object_name = "events"
    paginate = 6