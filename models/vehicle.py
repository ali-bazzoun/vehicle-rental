class Vehicle:
    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            rental_price_per_day: float,
            vehicle_id: int | None = None,
    ):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day
        self.info = [
            f"{self.brand} {self.model}",
            f"Year: {self.year}",
            f"Rental Price: ${round(self.__rental_price_per_day)}/day"
        ]

    def get_rental_price_per_day(self) -> float:
        return self.__rental_price_per_day
    
    def set_rental_price_per_day(self, rental_price_per_day: float):
        if self.__rental_price_per_day < 0:
            raise ValueError("Rental price per day cannot be negative.")
        self.__rental_price_per_day = rental_price_per_day

    def calculate_rental_cost(self, days: int) -> float:
        return self.get_rental_price_per_day() * days
    
    def display_info(self):
        print(", ".join(self.info))