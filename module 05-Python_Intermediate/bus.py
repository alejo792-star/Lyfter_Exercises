# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).
class Person:
    def __init__(self, name):
        self.name = name
class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers(self, person):
        
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("the bus is FULL sorry ")
    def remove_passenger (self,person):
        if person in self.passengers:
            self.passengers.remove(person)
        else:
            print("The person is no on the bus")

    def show_space_bus(self):
        print(f"max_passengers: {self.max_passengers} persons and at the moment the bus have {len(self.passengers)} persons")


def main():
    bus = Bus(2)
    person_1 = Person("Jefferson")
    person_2 = Person("Alejandro")
    person_3 = Person("Ana")
    bus.add_passengers(person_1)
    bus.add_passengers(person_2)
    bus.add_passengers(person_3) 
    bus.remove_passenger(person_2)
    bus.add_passengers(person_3)  
    bus.show_space_bus()

if __name__ == "__main__":
    main()



