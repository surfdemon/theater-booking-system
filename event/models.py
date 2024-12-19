from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models import Sum

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    available_tickets = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', blank=True, null=True, default=None)

    def tickets_left(self):
        '''Returns the number of tickets left for the event'''
        bookings_for_event = BookingTable.objects.filter(event=self)
        booked_tickets = bookings_for_event.aggregate(total=Sum('numberOfTickets'))['total']
        if booked_tickets is None:
            booked_tickets = 0
        return self.available_tickets - booked_tickets

    def __str__(self):
        return self.name


class BookingTable(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    numberOfTickets = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} booking for {self.event.name}'
