from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle


def show_vehicle_info(vehicle: Vehicle):
    vehicle.display_info()

def main():

    car = Car("Toyota", "Corolla", 2019, 50.0, 5)
    motorcycle = Motorcycle("Honda", "CBR", 2020, 40.0, 250)

    vehicles = [car, motorcycle]

    for vehicle in vehicles:
        show_vehicle_info(vehicle)

if __name__ == "__main__":
    main()

