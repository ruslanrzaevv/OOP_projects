class Car:
    def __init__(self, make, model, year, mileage) -> None:
        self.make = make 
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self) -> str:
        print(f'{self.year} {self.make} {self.model} Mileage: {self.mileage}')

class Fleet:
    def __init__(self,) -> None:
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f'Remove car: {car}')
        print('Car not found in fleet.')

    def display_cars(self):
        if not self.cars:
            print('No cars in the fleet')

        else:
            for car in self.cars:
                print(car)

car1 = Car('BMW', 'e34', 1990, 1000000)

flleet = Fleet()

flleet.add_car(car1)

print(car1.model)