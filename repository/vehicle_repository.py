from database import execute_query
from models import Car
from models import Motorcycle

class VehicleRepository:
    def save_vehicle(self, vehicle: Car | Motorcycle) -> Car | Motorcycle | None: 
        if isinstance(vehicle, Car):
            type_ = 'Car'
            seating = vehicle.seating_capacity
            engine = None
        elif isinstance(vehicle, Motorcycle):
            type_ = 'Motorcycle'
            seating = None
            engine = vehicle.engine_capacity
        else:
            raise ValueError("Invalid vehicle type")

        params = (
            type_,
            vehicle.brand,
            vehicle.model,
            vehicle.year,
            vehicle.get_rental_price_per_day(),
            seating,
            engine,
        )

        if vehicle.vehicle_id:
            # Update existing vehicle
            query = """--sql
                UPDATE vehicles
                SET type = ?, brand = ?, model = ?, year = ?, rental_price_per_day = ?,
                    seating_capacity = ?, engine_capacity = ?
                WHERE id = ?
            """
            params += (vehicle.vehicle_id,)
        else:
            # Insert new vehicle
            query = """--sql
                INSERT INTO vehicles (type, brand, model, year, rental_price_per_day, seating_capacity, engine_capacity)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """

        result = execute_query(query, params, commit=True)
        return self.get_vehicle_by_id(result) if result else None

    def delete_vehicle(self, vehicle_id: int) -> bool:
        query = "DELETE FROM vehicles WHERE id = ?"
        result = execute_query(query, (vehicle_id,), commit=True)
        return True if result else False

    def get_all_vehicles(self):
        query = "SELECT * FROM vehicles"
        rows = execute_query(query, fetch_all=True)
        return [
            vehicle for row in rows 
            if (vehicle := self._row_to_vehicle(row))
        ]

    def get_vehicle_by_id(self, vehicle_id: int) -> Car | Motorcycle | None:
        query = "SELECT * FROM vehicles WHERE id = ?"
        row = execute_query(query, (vehicle_id,), fetch_one=True)
        return self._row_to_vehicle(row) if row else None

    def _row_to_vehicle(self, row) -> Car | Motorcycle | None:
        (id_, type_, brand, model, year, rental_price, seating, engine) = row
        if type_ == 'Car':
            return Car(
                brand=brand,
                model=model,
                year=year,
                rental_price_per_day=rental_price,
                seating_capacity=seating,
                vehicle_id=id_
            )
        elif type_ == 'Motorcycle':
            return Motorcycle(
                brand=brand,
                model=model,
                year=year,
                rental_price_per_day=rental_price,
                engine_capacity=engine,
                vehicle_id=id_
            )
        else:
            return None