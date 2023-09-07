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

    __name = None
    __age = None
    __address = None
    __certificate = None

    def __init__(self, name: str, age: int, address: str, certificate: bool):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__certificate = certificate
    
    """
    ---
    Getter and setter methods section
    ---
    """

    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getAddress(self):
        return self.__address
    
    def getCertificate(self):
        return self.__certificate
    
    def setName(self, name: str):
        self.__name = name
        
    def setAge(self, age: int):
        self.__age = age
    
    def setAddress(self, address: str):
        self.__address = address
    
    def setCertificate(self, certificate: bool):
        self.__certificate = certificate


class Database:

    '''
    ---
    A class used to represent the Database the Applicants will be saved in 
    ---
    '''

    __applicantList: List[Applicant] = None

    def __init__(self, applicantList: List[Applicant] = None):
        if applicantList is None:
            applicantList = []

        self.__applicantList = applicantList

     
    """
    ---
    Getter and setter methods section
    ---
    """

    def getApplicantList(self):
        return self.__applicantList
    
    def insertApplicant(self, applicantList: List[Applicant] = None):
        self.__applicantList = applicantList
        


database = Database()

applicantFirst = Applicant("Simeon", 22, "Musterstr.", True)

database.insertApplicant([applicantFirst])





    
    

