from vehicle import Vehicle

class Car(Vehicle):

    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            rental_price_per_day: float,
            seating_capacity: int,
    ):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity
        self.info.insert(-1, f"Seats: {self.seating_capacity}")

    def display_info(self):
        print("Car: " + ", ".join(self.info))