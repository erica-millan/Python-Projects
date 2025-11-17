#creating the parent class
class Vehicle:
    make = "unknown"
    model = "unknown"
    year = 0
    
    """
    creating method for the parent class
    within class block so it stays on the same indention level
    of class passing in "self" special to classes so you can
    have access to info and methods within the class
    """
    
    def information(self):
        msg = "\n Make: {} \n Model: {}\n Year:{}".format(self.make,self.model,self.year)
        return msg
    
#car class will have access to it's parent information
#will ovverride some of the parent property values
class Car (Vehicle):
    make = "Nissan"
    model = "Altima"
    year = 2025
    num_doors = 4
    mph = 200
    #Polymorphism to override parent class info method
    def information(self):
        msg = "\n Make: {} \n Model: {}\n Year:{}\n Doors: {}\n Miles per hour: {}".format(self.make,self.model,self.year, self.num_doors, self.mph)
        return msg
    
    def steer_right(self):
        msg = "\n {} {} is steering right".format(self.make,self.model)
        return msg

#airplane class will have access to it's parent information
#will ovverride some of the parent info
class Airplane (Vehicle):
    make = "Boeing"
    model = "100"
    year = 2020
    wing_span = 70
    max_altitude = 30000
    #Polymorphism to override parent class info method
    def information(self):
        msg = "\n Make: {} \n Model: {}\n Year:{}\n Wing Span: {}\n Maximum Altitude: {}".format(self.make,self.model,self.year, self.wing_span, self.max_altitude)
        return msg
    
    def take_off(self):
        msg = "\n {} {} is is preparing for take off".format(self.make,self.model)
        return msg

    
if __name__ == "__main__":
    #initializing objects for airplane and car
    #calling in the inherited "information" method for both car and airplane
    ##also calling on their methods
    
    car = Car()
    print(car.information())
    print(car.steer_right())
    
    airplane = Airplane()
    print(airplane.information())
    print(airplane.take_off())
