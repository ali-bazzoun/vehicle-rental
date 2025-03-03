from car import Car
from motorcycle import Motorcycle

def main():

    car = Car("Toyota", "Corolla", 2019, 50.0, 5)
    motorcycle = Motorcycle("Honda", "CBR", 2020, 40.0, 250)

    
    car.display_info()
    motorcycle.display_info()

if __name__ == "__main__":
    main()

