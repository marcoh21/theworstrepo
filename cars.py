class Vehicle:
    def __init__(self, vehicle_id, make, model):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model

    def calculate_bill(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def __init__(self, vehicle_id, make, model, doors):
        super().__init__(vehicle_id, make, model)
        self.doors = doors

    def calculate_bill(self):
        return 100  # Example cost for fixing a car

class Motorbike(Vehicle):
    def __init__(self, vehicle_id, make, model, engine_cc):
        super().__init__(vehicle_id, make, model)
        self.engine_cc = engine_cc

    def calculate_bill(self):
        return 50  # Example cost for fixing a motorbike

class Truck(Vehicle):
    def __init__(self, vehicle_id, make, model, load_capacity):
        super().__init__(vehicle_id, make, model)
        self.load_capacity = load_capacity

    def calculate_bill(self):
        return 200  # Example cost for fixing a truck

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle_by_id(self, vehicle_id):
        self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]

    def remove_vehicle_by_type(self, vehicle_type):
        self.vehicles = [v for v in self.vehicles if not isinstance(v, vehicle_type)]

    def fix_vehicle(self, vehicle_id):
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return f"Fixing {vehicle.make} {vehicle.model}. Bill: ${vehicle.calculate_bill()}"
        return "Vehicle not found."

    def empty_garage(self):
        self.vehicles.clear()

    def remove_multiple_by_type(self, vehicle_type):
        self.remove_vehicle_by_type(vehicle_type)

    def show_vehicles(self):
        for v in self.vehicles:
            print(f"{v.vehicle_id}: {v.make} {v.model}")

# Example usage
garage = Garage()
garage.add_vehicle(Car(1, "Toyota", "Corolla", 4))
garage.add_vehicle(Motorbike(2, "Yamaha", "R1", 1000))
garage.add_vehicle(Truck(3, "Volvo", "FH16", 30000))

garage.show_vehicles()
print(garage.fix_vehicle(1))  # Fix a car

garage.remove_vehicle_by_type(Motorbike)
garage.show_vehicles()

# Test case for Car class
def test_car():
    car = Car(4, "Honda", "Civic", 4)
    assert car.vehicle_id == 4
    assert car.make == "Honda"
    assert car.model == "Civic"
    assert car.doors == 4
    assert car.calculate_bill() == 100
    print("Car test passed.")

test_car()