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
    _birthday:List[int]
    _certificate:bool = None
    _expectedSalary:float = None

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
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def getAddress(self):
        return self._address
    
    def getCertificate(self):
        return self._certificate
    
    def setName(self, name: str):
        self._name = name
        
    def setAge(self, age: int):
        self._age = age
    
    def setAddress(self, address: str):
        self._address = address
    
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
    """
    Getter and setter methods section
    """
    def insertApplicant(self, applicant: Applicant):
        self._applicantList.append(applicant)
    def findApplicant(self, name: str):
        for applicant in self._applicantList:
             if applicant.getName() == name:
                 return applicant
        return None

database = Database()
prefix = "created_"
suffix = "_applicant"
var_num = 0

def mainMenu():
    opt = int(input("What do you want: 1. Create Applicant"))
    return opt

opt = mainMenu()

if opt == 1:
    var_num += 1
    globals()[prefix + str(var_num) + suffix] = Applicant()
    print(globals()[prefix + str(var_num) + suffix].getName())
    mainMenu()

    


    



#print(f"That's applicant {foundApplicant.getName()} on {foundApplicant.getAddress()} and he is {foundApplicant.getAge()}")








    
    

