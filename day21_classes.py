# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 23:07:49 2020

@author: rekha
"""
#Question 21: Create a Parent Class “Vehicle” and 3 child classes “Bus”, “Car” and “Motorcycle”. All child classes should inherit all the properties of parent class and also has its own specific properties. Print one specific brand in each vehicle with specific property values.
#Vehicle Properties:
#Name:
#No of seats:
#Number of tyres:

#Child Class specific property:
#Brand:
class Vehicle:
    def __init__(self , name , seats , tyres):
        self.Vname = name
        self.Vseats = seats
        self.Vtyres = tyres
class Bus(Vehicle):
    def __init__(self, name , seats , tyres , brand):
        super().__init__(name , seats , tyres)
        self.VBrand = brand
    def printBus(self):
        print("Name :" , self.Vname , "\nType:" , type(self).__name__ ,"\nBrand:" , self.VBrand , "\nNo of seats:" , self.Vseats , "\nNo of tyres:" , self.Vtyres ,"\n")
class Car(Vehicle):
    def __init__(self, name , seats , tyres , brand):
        super().__init__(name , seats , tyres)
        self.VBrand = brand
    def printCar(self):
        print("Name :" , self.Vname , "\nType:" , type(self).__name__ ,"\nBrand:" , self.VBrand , "\nNo of seats:" , self.Vseats , "\nNo of tyres:" , self.Vtyres,"\n")
        
class Motorcycle(Vehicle):
    def __init__(self, name , seats , tyres , brand):
        super().__init__(name , seats , tyres)
        self.VBrand = brand
    def printmotorcycle(self):
        print("Name :" , self.Vname , "\nType:" , type(self).__name__ ,"\nBrand:" , self.VBrand , "\nNo of seats:" , self.Vseats , "\nNo of tyres:" , self.Vtyres,"\n")
bus = Bus("Traveller" , 28 , 6 ,"Volvo" ) 
car = Car("Swift" , 5 , 4 ,"Maruti" ) 
MC = Motorcycle("Pulsar" , 2 , 2 ,"Bajaj" ) 

bus.printBus()
car.printCar()
MC.printmotorcycle()