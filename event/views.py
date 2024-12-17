from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
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


class BookEvent(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        context = {
            'event': event
        }
        return render(request, 'event/book-event.html', context)

    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        user = request.user
        number_of_tickets = request.POST['number_of_tickets']
        booking = BookingTable.objects.create(
                event=event,
                user=user,
                numberOfTickets=number_of_tickets
                )
        booking.save()
        return render(request, 'event/booking_success.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for event in context['events']:
            event.tickets_left = event.tickets_left()
        return context


class user_bookings(LoginRequiredMixin, View):
    def get(self, request):
        user_bookings = BookingTable.objects.filter(user=request.user)
        return render(request, 'event/bookings.html', {'user_bookings': user_bookings})