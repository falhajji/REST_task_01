from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from flights.models import Flight
from flights.serializer import FlightSerializer, BookingSerializer
from datetime	import date

class FlightsListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class=FlightSerializer


class BookingsListView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=date.today())
    serializer_class=BookingSerializer