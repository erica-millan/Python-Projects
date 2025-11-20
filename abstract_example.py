#importing tools from Python to make abstract classes
from abc import ABC, abstractmethod

#template class, it's a class that other classes can build from.

class car(ABC):
    #regular method that just prints amount you're spending
    def payslip(self, amount):
        print("Your purchase amount: ", amount)
    """
    This function is telling us to pass in an argument, but we wont tell you how or what kind
    of data it will be.
    """
    #abstract method, any class that inherits from this method has to
    #write their own version of payment
    @abstractmethod
    def payment(self, amount):
        pass


    #debit card payment uses car template and has to define payment
class DebitCardPayment(car):
    #defining how to implement the payment function from its parent payslip class
    def payment(self, amount):
        print('Your purchase amount of {} exceeds your 100 limit.'.format(amount))


obj = DebitCardPayment()
obj.payslip("$400")
obj.payment("$400")

















