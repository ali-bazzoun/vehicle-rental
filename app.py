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
    print()

    rental_duration = [3,5]

    for vehicle, rental_days in zip(vehicles, rental_duration):
        show_rental_cost(vehicle, rental_days)
    print()

    update_message = "Updated rental price for {brand_model}: ${price:.1f}/day"

    car.set_rental_price_per_day(60.0)
    motorcycle.set_rental_price_per_day(45.0)

    for vehicle in vehicles:
        print(update_message.format(
            brand_model=vehicle.info[0],
            price=vehicle.get_rental_price_per_day()
        ))


if __name__ == "__main__":
    main()

