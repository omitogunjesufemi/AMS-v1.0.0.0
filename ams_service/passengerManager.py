from ams_models.passenger import Passenger
class PassengerManager:
    user = []
    def createUser(self, name, idNo, email, address):
        passenger = Passenger(name, idNo, email, address)
        self.user.append(passenger)
        print(f'Passenger {name} with REG-ID {idNo} was created successfully')

    def showUser(self, passenger):
        print(passenger)


    def findUser(self, idNo):
        for passenger in self.user:
            if passenger.idNo == idNo:
                return passenger

    def findUserName(self, idNo):
        for passenger in self.user:
            if passenger.idNo == idNo:
                return passenger.name

    def findUserID(self, idNo):
        for passenger in self.user:
            if passenger.idNo == idNo:
                return passenger.idNo

    def retrieveUser(self, idNo):
        retrieve = self.findUser(idNo)
        if retrieve == False:
            print(f"No passenger with the Passenger-ID {idNo} exist")
        else:
            print(f'NAME        PASSENGER-ID       ADDRESS      EMAIL')
            return self.showUser(retrieve)

    def updateUser(self, name, idNo, email, address):
        try:
            update = self.findUser(idNo)
            update.name = name
            update.email = email
            update.address = address
            print("The Passenger'\s details were updated successfully!")
        except:
            print("No Passenger with the Passenger-ID exist")

    def deleteUser(self, idNo):
        try:
            delete = self.findUser(idNo)
            self.user.remove(delete)
            print(f"The passenger with PASS-ID:{idNo} was deleted successfully!")
        except:
            print(f"No craft with the Registration-ID {idNo} exist")

    def printUser(self):
        print(f'NAME        PASSENGER-ID       ADDRESS      EMAIL')
        for passenger in self.user:
            self.showUser(passenger)

