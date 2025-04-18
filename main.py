class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5 # Initial hunger level
        self.energy = 5 # Initial energy level
        self.happiness = 5 # Initial happiness level
        self.tricks = [] # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3) # Ensure hunger doesn't go below 0
        self.happiness += 1
        self.happiness = min(10, self.happiness) # cap happiness at 10

    def sleep(self):
        self.energy = min(10, self.energy + 5) # Ensure energy doesn't go above 10


    def play(self):
        self.energy = max(0, self.energy - 2) # Ensure energy doesn't go below 0
        self.happiness = min(10, self.happiness + 2) # Ensure happiness doesn't go above 10
        self.hunger += 1
        self.hunger = min(10, self.hunger) # cap hunger at 10

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s Tricks:")
            for trick in self.tricks:
                print(trick)
        else:
            print(f"{self.name} doesn't know any tricks yet.")


# Method test:
my_pet = Pet("Fluffy")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.sleep()
my_pet.train("fetch")
my_pet.train("roll over")
my_pet.show_tricks()
my_pet.get_status()
