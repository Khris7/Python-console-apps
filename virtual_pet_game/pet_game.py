import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 10)
        print(f"You fed {self.name}. Hunger is now {self.hunger}.")

    def play(self):
        self.happiness = min(100, self.happiness + 10)
        print(f"You played with {self.name}. Happiness is now {self.happiness}.")

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100\n")

    def pass_time(self):
        self.hunger = min(100, self.hunger + random.randint(5, 15))
        self.happiness = max(0, self.happiness - random.randint(5, 15))

def main():
    name = input("What would you like to name your pet? ")
    pet = VirtualPet(name)

    while True:
        pet.status()
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Do nothing")
        print("4. Quit")

        choice = input("> ")

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            print("You let time pass...")
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid choice. Try again.")

        pet.pass_time()
        time.sleep(1)

if __name__ == "__main__":
    main()
