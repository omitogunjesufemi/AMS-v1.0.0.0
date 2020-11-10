from ams_models.aircraft import Aircraft


class AircraftManager:
    airplane = []
    def createCraft(self, name, model, capacity, regNo):
        a = Aircraft(name, model, capacity, regNo)
        self.airplane.append(a)
        print(f'Aircraft {name} with REG-ID {regNo} was created successfully')

    def showCraft(self, a):
        print(a)

    def findCraftID(self, regNo):
        for a in self.airplane:
             if a.regNo == regNo:
                return a.regNo

    def findCraft(self, regNo):
        for a in self.airplane:
            if a.regNo == regNo:
                return a

    def printCraft(self):
        print(f'NAME    MODEL       CAPACITY    REGISTRATION-ID')
        for a in self.airplane:
            self.showCraft(a)

    def updateCraft(self, name, model, capacity, regNo):
        try:
            a = self.findCraft(regNo)
            a.name = name
            a.model = model
            a.capacity = capacity
            print("The Craft details were updated successfully!")
        except:
            print("No craft with the Registration-ID exist")

    def retrieveCraft(self, regNo):
        a = self.findCraft(regNo)
        if a == False:
            print(f"No craft with the Registration-ID {regNo} exist")
        else:
            print(f'NAME    MODEL       CAPACITY    REGISTRATION-ID')
            return self.showCraft(a)


    def deleteCraft(self, regNo):
        try:
            a = self.findCraft(regNo)
            self.airplane.remove(a)
            print(f"The craft with REG-ID:{regNo} was deleted successfully!")
        except:
            print(f"No craft with the Registration-ID {regNo} exist")

