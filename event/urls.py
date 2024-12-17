"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import user_bookings, UpdateBooking, DeleteBooking


urlpatterns = [
    path('', views.EventHome.as_view(), name='event_home'),
    path('events/', views.EventList.as_view(), name="events"),
    path('bookings/', user_bookings.as_view(), name='user_bookings'),
    path('bookings/update/<int:booking_id>/', UpdateBooking.as_view(), name='update_booking'),
    path('bookings/delete/<int:booking_id>/', DeleteBooking.as_view(), name='delete_booking'),
    path(
        'events/book-event/<int:event_id>/',
        views.BookEvent.as_view(),
        name="book_event"
        ),
]
