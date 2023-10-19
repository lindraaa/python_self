class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("The car is driving")
    def stop(self):
        print("The car is stopping")


from car import Car

car1 = Car("Chevy", "Corvette", 2020, "black")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)

car1.drive()
car1.stop()

