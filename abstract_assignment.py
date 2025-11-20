#importing tools from Python to make abstract classes
from abc import ABC, abstractmethod

#template class "Delivery", it's a class that other classes can build from.
class Delivery(ABC):
    #regular method that prints yor chosen delivery
    def chosenDelivery(self, delivery):
        print("Your chosen delivery is: ", delivery)
    #This function is telling us to pass in an argument but we wont tell you
    #how or what kind of data it will be
    @abstractmethod
    def amountDue(self, distance):
        pass
    
#Same day, two day and three day all use the delivery template and have to define amountDue
 
class sameDay(Delivery):
    #defining amount due for sameDay
    def amountDue(self, distance):
        total = distance * 4
        print('For same day delivery of {} miles your total will be ${}\n'.format(distance, total))


class twoDay(Delivery):
    #defining amount due for twoDay
    def amountDue(self, distance):
        total = distance * 3
        print('For two day delivery of {} miles your total will be ${}\n'.format(distance, total))


class threeDay(Delivery):
    #defining amount due for threeDay
    def amountDue(self, distance):
        total = distance * 2
        print('For three day delivery of {} miles your total will be ${}\n'.format(distance, total))


#Creates an object of the same day class
obj = sameDay()
#calls method from parent class (delivery) and prints your chosen delivery
obj.chosenDelivery("OneDay")
#calls the child class of delivery (sameday) which gets features of parent but adds its own features 
obj.amountDue(10)

obj = twoDay()
obj.chosenDelivery("TwoDay")
obj.amountDue(10)

obj = threeDay()
obj.chosenDelivery("ThreeDay")
obj.amountDue(10)
