class Car:
    def __init__(self, model, brand, color, price):
        self.model = model
        self.brand = brand
        self.color = color
        self.price = price
        self.mileage = 0
    def get_name(self):
        return self.brand,self.model
    def get_model(self):
        return self.model
    def get_brand(self):
        return self.brand
    def get_color(self):
        return self.color
    def get_price(self):
        return self.price
    def set_mileage(self, km):
        self.mileage += km
    def get_info(self):
        print(f"{self.color} {self.model} {self.brand} is ${self.price} with {self.mileage}km")


class Car_dealership:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cars = []

    def get_name(self):
        return self.name
    def get_location(self):
        return self.location
    def get_cars(self):
        return [f"{c.get_color()}, {c.get_model()}, {c.get_brand()} is {c.get_price()} with {c.mileage}" for c in self.cars]

    def add_car(self, car):
        self.cars.append(car)

    def give_info(self):
        a = [f"{c.get_brand()} {c.get_model()}" for c in self.cars]
        print(f"{self.name}, located in {self.location}, has these car models: {', '.join(a)}")


car1 = Car("I5", "BMW", "Red", 89000)
car1.set_mileage(90900)
car2 = Car("911","Porsche","Black",90000)
car2.set_mileage(12005)
car3 = Car("CLS 63","Mercedes","Dark Blue",130000)
dealership = Car_dealership("Fast Wheels", "Tashkent")
dealership.add_car(car1)
dealership.add_car(car2)
dealership.add_car(car3)
dealership.give_info()
car3.get_info()
car1.get_info()
car2.get_info()





