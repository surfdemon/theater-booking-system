from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField()
    available_tickets = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image')

    def tickets_left(self):
        booked_tickets = BookingTable.objects.filter(event=self).count()
        print(f'Booked Tickets: {booked_tickets}')
        return self.available_tickets - booked_tickets

    def __str__(self):
        return self.name


class BookingTable(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    numberOfTickets = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} booking for {self.event.name}'
