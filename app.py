from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle


def show_vehicle_info(vehicle: Vehicle):
    vehicle.display_info()

def show_rental_cost(vehicle: Vehicle, rental_days: int):
    print(f"Rental cost for {vehicle.info[0]} for {rental_days} days: ${vehicle.calculate_rental_cost(rental_days):.1f}")

def main():

    car = Car("Toyota", "Corolla", 2019, 50.0, 5)
    motorcycle = Motorcycle("Honda", "CBR", 2020, 40.0, 250)

    vehicles = [car, motorcycle]

    for vehicle in vehicles:
        show_vehicle_info(vehicle)

    rental_duration = [3,5]

    for vehicle, rental_days in zip(vehicles, rental_duration):
        show_rental_cost(vehicle, rental_days)


if __name__ == "__main__":
    main()

