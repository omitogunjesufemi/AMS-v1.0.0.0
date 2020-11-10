from ams_models.passenger import Passenger
class Booking:
    def __init__(self, passenger, flight, ticketType, ticketClass, seatNumber):
        self.passenger = passenger
        self.flight = flight
        self.ticketType = ticketType
        self.ticketClass = ticketClass
        self.seatNumber = seatNumber


    def __str__(self):
        return f"{self.passenger:<8s}{self.flight:<13s}{self.ticketType:<12s}{self.seatNumber}{self.ticketClass}"