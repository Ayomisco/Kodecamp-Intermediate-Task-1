class Vehicle:
    def __init__(self, name, vehicle_type, vehicle_no, place_made, year_made) -> None:
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicle_no = vehicle_no
        self.place_made = place_made
        self.year_made = year_made
    
    def __str__(self):
        return f"Name: {self.name}, Vehicle Type: {self.vehicle_type}, Place Made: {self.place_made}, Vehicle No.: {self.vehicle_no}, Year Made: {self.year_made}"

    

class Car(Vehicle):
    
    def request(self):
        pass

toyota = Car("Toyota Camry", "Toyota", "Russia", "002332200", "2016")

print(toyota)




