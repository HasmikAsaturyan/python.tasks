import math
class Vehicle:
    vehicle_count = 0
    def __init__(self,make,model):
        self.make = make
        self.model = model
        Vehicle.increment_vehicle_count(self)
    def __repr__(self):
        return f'vehicle class has 2 attributs,{self.make} and {self.model}'
    def increment_vehicle_count(self):
        Vehicle.vehicle_count += 1
    def get_vehicle_count(self):
        return Vehicle.vehicle_count
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self,make,model,number_of_wheels = 4):
        super().__init__(make,model)
        self.number_of_wheels = number_of_wheels
    def __repr__(self):
        return f"number of wheels = {self.number_of_wheels}"
    def start_engine(self):
        print("car engine started")
        super().start_engine()

class ElectricVehicle:
    def __init__(self,battery_capacity):
        self.battery_capacity = battery_capacity

class ElectricCar(Car,ElectricVehicle):
    def __init__(self, make, model,battery_capacity,number_of_wheels=4):
        Car.__init__(make, model,number_of_wheels=4)
        ElectricCar.__init__(self,battery_capacity)

class Polar:
    def __init__(self,radius,angle):
        self.radius = radius
        self.angle = angle

    def __repr__(self):
        return f"radius = {self.radius}, angle = {self.angle}"

    def convert_to_rectangular(self):
        x = self.radius * math.cos(self.angle)
        y = self.radius * math.sin(self.angle)
        
        return x,y
    
    def __add__(self, other):
        x = self.convert_to_rectangular()[0] + other.convert_to_rectangular()[0]
        y = self.convert_to_rectangular()[1] + other.convert_to_rectangular()[1]
        
        r = math.sqrt(x**2 + y**2)
        angle = math.asin(y/r)
        return Polar(r, angle)
    
veh = Vehicle(1990,"bwm")
print(veh.get_vehicle_count())
car = Car(2008,'tesla')
print(veh.get_vehicle_count())
print(car.start_engine())
    
p = Polar(1,0)
p2 = Polar(1,math.pi/2)
print(p.convert_to_rectangular())
print(p2.convert_to_rectangular())
print(p + p2)

