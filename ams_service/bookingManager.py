from ams_models.booking import Booking
class BookingManager():
    bookings = []
    seatNumber = 0
    def __init__(self, passengerManager, flightManager):
        self.passengerManager = passengerManager
        self.flightManager = flightManager

    def createBooking(self, passenger, flight, ticketType, ticketClass):
        name = self.passengerManager.findUserName(passenger)
        regNo = self.flightManager.findFlightID(flight)
        passID = self.passengerManager.findUserID(passenger)
        idNo = self.passengerManager.findUser(passenger)
        aircraft = self.flightManager.findFlight(flight)
        if idNo == None or aircraft == None:
            print('This passenger cannot be booked a flight as it has no PASS-ID or assigned flight!')
        else:
            self.seatNumber += 1
            ticketID = (f"{passID}/{regNo}/{self.seatNumber}")
            booking = Booking(passenger, flight, ticketType, ticketClass, self.seatNumber)
            self.bookings.append(booking)
            print(f"""A booking for {name} with Flight-ID:{regNo} was made.
                      Your seat number is {self.seatNumber}. The Ticket ID is {ticketID}""")

    def showBooking(self, booking):
        print(booking)

    def findBooking(self, seatNumber):
        self.seatNumber = seatNumber
        for booking in self.bookings:
            if booking.seatNumber == seatNumber:
                return booking

    def retrieveBooking(self, seatNumber):
        self.seatNumber = seatNumber
        retrieve = self.findBooking(seatNumber)
        return self.showBooking(retrieve)

    def updateBooking(self, passenger, flight, ticketType, ticketClass, seatNumber):
        self.seatNumber = seatNumber
        try:
            update = self.findBooking(seatNumber)
            update.passenger = passenger
            update.flight = flight
            update.ticketType = ticketType
            update.ticketClass = ticketClass
            print("The Booking details were updated successfully!")
        except:
            print(f"No Booking with the seat number: {seatNumber} exist")

    def deleteBooking(self, seatNumber):
        self.seatNumber = seatNumber
        try:
            delete = self.findBooking(seatNumber)
            self.bookings.remove(delete)
            print(f"The Booking with the seat number: {seatNumber} was deleted successfully!")
        except:
            print(f"No Booking with the seat number: {seatNumber}  exist")

    def printBooking(self):
        print(f'PASGR-ID        AIRCRAFT-ID       TICKET-TYPE      SEAT-NO      TICKET-CLASS')
        for booking in self.bookings:
            self.showBooking(booking)

