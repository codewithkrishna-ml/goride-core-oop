#PROJECT-GoRide Core
class User:
    def __init__(self , user_id , name , phone , rating=5.0):
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.rating = rating

    def display_profile(self):
        print(f"Name: {self.name} | Phone: {self.phone} | Rating: {self.rating}/5.0")

class Rider(User):
    def __init__(self, user_id_, name, phone, rating=5.0 ,wallet_balance=0.0 , current_location=None):
        super().__init__(user_id_, name, phone, rating)
        self.wallet_balance = wallet_balance
        self.current_location = current_location

    def add_money(self , amount):
        if amount > 0:
            self.wallet_balance +=amount
            print(f"Amount {amount} added successfully. Current wallet Balance: {self.wallet_balance}")
        else:
            print("Error: Amount must be greater than 0!")

    def book_ride(self ,pickup_location , drop_location):
        print(f"\n[Booking Request] {self.name} wants a ride from '{pickup_location}' to '{drop_location}'")
        if self.wallet_balance < 50:
            print("Booking Failed Insufficient wallet balance. Please add money")
            return False
        else:
            self.current_location = pickup_location
            print("Booking Approved: Searching for nearby drivers...")
            return True

class Driver(User):
    def __init__(self, user_id_, name, phone , license_number, rating=5.0 ,is_available=True, current_vehicle=None):
        super().__init__(user_id_, name, phone, rating)
        self.license_number = license_number
        self.is_available = is_available
        self.current_vehicle = current_vehicle

    def accept_ride(self):
        if self.is_available:
            self.is_available = False
            print(f"Driver {self.name} has accepted the ride status: BUSY")
            return True
        else:
            print(f"Driver {self.name} is busy with another passenger")
            return False

    def complete_ride(self):
        self.is_available = True
        print(f"Driver {self.name} completed the ride. Status: AVAILABLE")

class Vehicle:
    def __init__(self , vehicle_number, model):
        self.vehicle_number = vehicle_number
        self.model = model

    def get_vehicle_details(self):
        print(f"Vehicle number: {self.vehicle_number}| Model: {self.model}")

    def calculate_fare(self ,distance):
        return 0

class Bike(Vehicle):
    def calculate_fare(self , distance):
        return distance * 5.0

class Sedan(Vehicle):
    def calculate_fare(self,distance):
        return distance * 12.0

class SUV(Vehicle):
    def calculate_fare(self,distance):
        return distance * 18.0

if __name__ == "__main__":
    print("==== TESTING RIDECRAFT PROJECT ====\n ")

    print("-------Creating Rider-------")
    rider1 = Rider("R101" , "Krishna" , "9876543210" , rating=4.8 , wallet_balance=30.0)
    rider1.display_profile()

    rider1.book_ride("Nagra" , "Jhansi station")

    rider1.add_money(200)
    rider1.book_ride("Nagra" , "Jhansi station")

    print("\n------- Creating Driver & Vehicle ----------")
    my_bike = Bike("UP-93-AB-1234" , "Splender plus")
    driver1 = Driver("D501" , "Amit kumar" , "9988776655" , rating=4.9 , license_number="DL-56789")

    driver1.current_vehicle = my_bike
    driver1.display_profile()
    my_bike.get_vehicle_details()

    distance_km = 10
    fare = driver1.current_vehicle.calculate_fare(distance_km)
    print(f"Calculated fore for {distance_km}km via bike: {fare}")

    print("\n------- Testing Driver Status Changes ---------")
    driver1.accept_ride()
    driver1.accept_ride()
    driver1.complete_ride()
