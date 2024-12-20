from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, BookingTable
from .forms import UpdateBookingForm
from django.db.models import Sum

# Create your views here.


class EventHome(View):
    """
    View to display the home page with events.
    """
    def get(self, request):
        """
        Handle GET requests and render the home page with events.
        """
        events = Event.objects.all()
        context = {
            'events': events
        }
        return render(request, 'event/home.html', context)


class EventList(generic.ListView):
    """
    Generic class-based view to list all events with pagination.
    """
    model = Event
    template_name = "event/events.html"
    context_object_name = "events"
    paginate_by = 3


class BookEvent(LoginRequiredMixin, View):
    """
    View to handle booking an event.
    """
    def get(self, request, event_id):
        """
        Handle GET requests and render the booking page for a specific event.
        """
        event = Event.objects.get(pk=event_id)
        context = {
            'event': event
        }
        return render(request, 'event/book-event.html', context)

    def post(self, request, event_id):
        """
        Handle POST requests to create a booking for a specific event.
        """
        event = Event.objects.get(pk=event_id)
        user = request.user
        number_of_tickets = request.POST['number_of_tickets']
        booking = BookingTable.objects.create(
                event=event,
                user=user,
                numberOfTickets=number_of_tickets
                )
        booking.save()
        context = {
                   'event': event.name,
                   'number_of_tickets': number_of_tickets,
        }
        return render(request, 'event/booking-success.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for event in context['events']:
            event.tickets_left = event.tickets_left()
        return context


class user_bookings(LoginRequiredMixin, View):
    """
    View to display the user's bookings.
    """
    def get(self, request):
        user_bookings = BookingTable.objects.filter(user=request.user)
        return render(request, 'event/bookings.html', {'user_bookings': user_bookings})


class UpdateBooking(LoginRequiredMixin, View):
    """
    View to handle updating a booking.
    """
    def get(self, request, booking_id):
        """
        Handle GET requests and render the update booking page for a specific booking.
        """
        booking = get_object_or_404(BookingTable, id=booking_id, user=request.user)

        form = UpdateBookingForm(instance=booking)
        return render(request, 'event/update_booking.html', {'form': form, 'booking': booking})

    def post(self, request, booking_id):
        """
        Handle POST requests to update a booking for a specific event.
        """
        booking = get_object_or_404(BookingTable, id=booking_id, user=request.user)
        form = UpdateBookingForm(request.POST, instance=booking)
        if form.is_valid():
            tickets_left = booking.event.tickets_left()
            if form.cleaned_data['numberOfTickets'] > tickets_left:
                form.add_error("numberOfTickets", f"Not enough tickets left for this event.\n Only {tickets_left} tickets left.")
                return render(request, 'event/update_booking.html', {'form': form, 'booking': booking})
            form.save()
            return redirect('user_bookings')
        return render(request, 'event/update_booking.html', {'form': form, 'booking': booking})


class DeleteBooking(LoginRequiredMixin, View):
    """
    View to handle deleting a booking.
    """
    def post(self, request, booking_id):
        """
        Handle POST requests to delete a booking for a specific event.
        """
        booking = get_object_or_404(BookingTable, id=booking_id, user=request.user)
        booking.delete()
        return redirect('user_bookings')
