class Person:
    """
    __init__: initializes object with starting values.
    self: self represents the specific object (instance) you're working with. (current object)
    It's the specific object that is calling the method. In the method, python will haveto know which objects data you're refferrign to.
    fName, lName and Age are all protected which has a single "_" underscore.
    social sec num is private so it has doubl "_" underscore.
    """
    def __init__(self, fName, lName, age, ssn):
        self._fName = fName #protected attribute
        self._lName = lName #protected attribute
        self._age = age     #protected attribute
        self.__ssn = ssn    #private attribute

    def get_ssn(self):
        return self.__ssn

#creating an object which will run __init__ automatically since __init__ is called whenever
#an object is created for that class.
#object "p" will have attributes of args given at the time the class was called
#values given will be stored in that object
#P will have the attributes ready to be used
        
p1 = Person("Erica", "Millan", 32, 12345678)
p2 = Person("Nick", "Smith", 45, 123456)

print(p1._fName)
print(p1._lName)
print(p1._age)
print(p1.get_ssn()) #calling method to get private attribute without name mangling

print(p2._fName)
print(p2._lName)
print(p2._age)
print(p2.get_ssn()) #using name mangling to get private attribute



    
