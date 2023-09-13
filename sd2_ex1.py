'''
SD2 Task1 
Application where you can save and sort all the applicants
'''

"""
Imports
"""
from typing import List
from typing import TypeAlias


class Applicant:
    '''
    ---
    A class used to represent the Applicants 
    ---
    '''
    _name = None
    _age = None
    _address = None
    _certificate = None

    def __init__(self, name: str, age: int, address: str, certificate: bool):
        self._name = name
        self._age = age
        self._address = address
        self._certificate = certificate
    
    """
    ---
    Getter and setter methods section
    ---
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
    ---
    A class used to represent the Database the Applicants will be saved in 
    ---
    '''

    _applicantList: List[Applicant] = None

    def __init__(self, applicantList: List[Applicant] = None):
        if applicantList is None:
            applicantList = []

        self._applicantList = applicantList
     
    """
    ---
    Getter and setter methods section
    ---
    """

    def insertApplicant(self, applicant: Applicant):
        self._applicantList.append(applicant)
    
    def findApplicant(self, name: str):
        for applicant in self._applicantList:
             if applicant.getName() == name:
                 return applicant
        return None
        
        


database = Database()

applicantFirst = Applicant("Simeon", 22, "Musterstr.", True)
applicantSecond = Applicant("Kek", 23, "Musterstr.", False)

database.insertApplicant(applicantFirst)
database.insertApplicant(applicantSecond)

applicantList = database._applicantList


foundApplicant = database.findApplicant(input())
print("That's applicant {} and he is {} years old.".format(foundApplicant.getName(), foundApplicant.getAge()))








    
    

