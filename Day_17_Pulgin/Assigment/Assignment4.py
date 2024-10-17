class Appliance():
    def __init__(self,brand,power_rating):
        self.brand=brand
        self.power_rating=power_rating

    def energy_usage(self,hours):
        energy_consumed=self.power_rating*hours
        energy_consumed_Kwh=energy_consumed/1000

        print(f"Energy Consumed by {self.brand} is {energy_consumed_Kwh} Kwh")

    def display(self):
        print(f"This is a {self.brand} Appliance")

class WashingMachine(Appliance):
    def __init__(self,brand,power_rating,capacity):
        super().__init__(brand,power_rating)
        self.capacity=capacity
    def display(self):
        print(f"This is {self.brand} washing machine with {self.capacity} kg capacity")


class Refrigerator(Appliance):
    def __init__(self, brand, power_rating, volume):
        super().__init__(brand, power_rating)
        self.volume = volume
    def display(self):
        print(f"This is {self.brand} Refrigerator machine with {self.volume} kg capacity")

class Microwave(Appliance):
    def __init__(self, brand, power_rating,power_levels):
        super().__init__(brand, power_rating)
        self.power_levels = power_levels
    def display(self):
        print(f"This is {self.brand} Refrigerator machine with {self.power_levels} power levels")

washing_machine=WashingMachine("Wirpool",5000,8)
Refrigerator=Refrigerator("Panasonic",5000,8)
Microwave=Microwave("LG",500,8)

washing_machine.display()
Refrigerator.display()
Microwave.display()

washing_machine.energy_usage(3)
Refrigerator.energy_usage(5)
Microwave.energy_usage(8)