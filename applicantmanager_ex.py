'''
SD2 Task1 
Application where you can save and sort all the applicants
'''

"""
Imports
"""
from typing import List
from typing import TypeAlias
import random


class Applicant:
    '''
    A class used to represent the Applicants 
    '''
    _id:int = None
    _firstName:str = None
    _secondName:str = None
    _gender:str = None
    _city:str = None
    _age:int = None
    _address:str = None
    _birthday:list = None
    _certificate:bool = None
    _expectedSalary:float = None
    _applicantEntityList:list = None

    def __init__(self):
        self._id = random.randint(0, 10000)
        self._firstName = input("First Name:")
        self._secondName = input("Second Name:")
        self._gender = input("Gender:")
        self._city = input("City:")
        self._age = int(input("Age:")) 
        self._address = input("Address:")
        self._birthday = [int(input("Day")), int(input("Month")), int(input("Year"))]
        self._certificate = bool(input("Certificate:"))
    
    """
    Getter and setter methods section
    """
    def getFirstName(self):
        return self._firstName
    def getSecondName(self):
        return self._secondName
    def getGender(self):
        return self._gender
    def getCity(self):
        return self._city
    def getAge(self):
        return self._age
    def getAddress(self):
        return self._address
    def getBirthday(self):
        return self._birthday
    def getCertificate(self):
        return self._certificate
    #--
    def setFirstName(self, firstName: str):
        self._firstName = firstName
    def setSecondName(self, secondName: str):
        self._secondName = secondName
    def setGender(self, gender):
        self._gender = gender
    def setCity(self, city):
        self._city = city 
    def setAge(self, age: int):
        self._age = age
    def setAddress(self, address: str):
        self._address = address
    def setBirthday(self, birthday: list)
        self._birthday = birthday 
    def setCertificate(self, certificate: bool):
        self._certificate = certificate

class Database:
    '''
    A class used to represent the Database the Applicants will be saved in 
    '''
    _applicantList: List[Applicant] = None

    def __init__(self, applicantList: List[Applicant] = None):
        if applicantList is None:
            applicantList = []
        self._applicantList = applicantList

    '''
    Getter and setter methods section
    '''
    def insertApplicant(self, applicant: Applicant):
        self._applicantList.append(applicant)

    def findApplicant(self, name: str):
        for applicant in self._applicantList:
             if applicant.getFirstName() == name:
                 return applicant


database = Database()
applicantEntityList = Applicant._applicantEntityList
prefix = "created_"
suffix = "_applicant"
var_num = 0

def mainMenu():
    opt = int(input("What do you want: 1. Create Applicant 2. Print all Applicants"))
    return opt

opt = mainMenu()

if opt == 1:
    var_num += 1
    globals()[prefix + str(var_num) + suffix] = Applicant()
    applicantEntityList.append(applicantEntityList)#need a getter for the list <<undone>>
    print(globals()[prefix + str(var_num) + suffix].getFirstName())
    mainMenu()

#add applicant in database
if opt == 2:
    pass

#print all applicants option
if opt == 3:
    mainMenu()
    pass

    


    



#print(f"That's applicant {foundApplicant.getFirstName()} on {foundApplicant.getAddress()} and he is {foundApplicant.getAge()}")








    
    

