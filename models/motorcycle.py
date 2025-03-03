from models.vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        rental_price_per_day: float,
        engine_capacity: int,
        vehicle_id: int | None = None
    ):
        super().__init__(brand, model, year, rental_price_per_day, vehicle_id)
        self.engine_capacity = engine_capacity
        self.info.insert(-1, f"Engine: {self.engine_capacity}cc")

    def display_info(self):
        print("Bike: " + ", ".join(self.info))