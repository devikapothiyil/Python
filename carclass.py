class Car:
    def __init__(self,brand,model,year,mileage):
        self.brand=brand
        self.model=model
        self.year=year
        self.mileage=mileage

    def  display_info(self):
        print(f"Your Car is {self.model} model of brand {self.brand} released on {self.year} with a mileage of {self.mileage}.")

    def drive(self,km):
        self.mileage+=km
        print(f"Modified mileage is {self.mileage}")

car1=Car("Ford","Mustang",2025,20)
car1.display_info()
car1.drive(10)