from models.vehicle import Vehicle
from models import Car, Motorcycle
from repository import VehicleRepository

def show_vehicle_info(vehicle: Vehicle):
    vehicle.display_info()

def show_rental_cost(vehicle: Vehicle, rental_days: int):
    print(f"Rental cost for {vehicle.info[0]} for {rental_days} days: ${vehicle.calculate_rental_cost(rental_days):.1f}")

def update_rental_price(vehicle: Vehicle, rental_price: float, vehicle_repository: VehicleRepository):
    vehicle.set_rental_price_per_day(rental_price)
    vehicle_repository.save_vehicle(vehicle)
    print(f"Updated rental price for {vehicle.info[0]}: ${round(vehicle.get_rental_price_per_day())}/day")
    
def main():

    vehicle_repository = VehicleRepository()

    car = vehicle_repository.save_vehicle(Car("Toyota", "Corolla", 2019, 50.0, 5))
    motorcycle = vehicle_repository.save_vehicle(Motorcycle("Honda", "CBR", 2020, 40.0, 250))

    # car = vehicle_repository.get_vehicle_by_id(1)
    # motorcycle = vehicle_repository.get_vehicle_by_id(2)

    vehicles = [car, motorcycle]

    for vehicle in vehicles:
        show_vehicle_info(vehicle)  # show vehicle info
    print()

    rental_duration = [3,5]

    for vehicle, rental_days in zip(vehicles, rental_duration):
        show_rental_cost(vehicle, rental_days)  # show rental cost for rental duration
    print()

    updates = [80.0, 45.0]

    for vehicle, price in zip(vehicles, updates):
        update_rental_price(vehicle, price, vehicle_repository)  # update and print new rental price
    
if __name__ == "__main__":
    main()