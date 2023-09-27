
'''
imports
'''
import random

'''
class representing the whole game
'''
class Main: 
    '''
    _generatedField: list - the list that stores all the 'ships'
    _generatedFieldCopy: list - the list that acts as an 'overlay' so you cannot see where the ships are 
    '''
    _generatedField: list = []
    _generatedFieldCopy: list = []
    
    '''
    in case we need a constructor
    '''
    def __init__(self):
        pass

    '''
    generates an empty 'ocean'
    rowAmount: int - how many rows does the field have
    columnAmount: int - how many columns does the field have
    '''
    def generateField(self):
        self.rowAmount: int = int(input("Enter Amount of Rows: "))
        self.columnAmount: int = int(input("Enter Amount of Items on a Row: "))
        
        if(self.rowAmount and isinstance(self.rowAmount, int)):
            self._generatedField = [[None]] * self.rowAmount 
            self._generatedFieldCopy = [[None]] * self.rowAmount
        if(self.columnAmount and isinstance(self.columnAmount, int)): 
                for i in range(0, self.rowAmount):  
                    self._generatedField[i] = ['x'] * self.columnAmount
                    self._generatedFieldCopy[i] = ['x'] * self.columnAmount
        print(*self._generatedField, sep = "\n")
            
        return self._generatedField, self._generatedFieldCopy
        
    '''
    generetes ships that are marked as 'i' in the 'ocean' 
    index: int - index that counts the iterations of the loop
    generatedRow: int - where the random row position of the ship is saved
    generatedColumn: int - where the random column position of the ship is saved
    generatedPlaces: int - the amount of places in our ocean, if it's smaller than ship amoung -> else:
    '''
    def generateShip(self):
        index: int = 0 #index for the loop so it counts the iterations and generates ships that are equal to the ships amount
        generatedRow: int
        generatedColumn: int 
        generatedPlaces: int = self.rowAmount * self.columnAmount
        shipLength: int 
        generatedShipDirection: int 
        iterationIndex: int = 0
        directionChoice: list = ['genRow', 'genColumn']
        

        self.shipAmount: int = int(input("Enter Amount of Ships: "))

        if self.shipAmount <= generatedPlaces: 
            while self.shipAmount > index: 
                generatedRow = random.randint(0, self.rowAmount - 1)
                generatedColumn = random.randint(0, self.columnAmount - 1)
                
                #ships gotta take multiple places
                self._generatedField[generatedRow][generatedColumn] = "O"
                generatedShipDirection = random.choice(directionChoice)
            
                if generatedShipDirection == 'genRow':
                    shipLength = random.randint(0, self.rowAmount)
                    while iterationIndex < shipLength: 
                        self._generatedField[generatedRow + 1][generatedColumn] = "O"
                        iterationIndex += 1
                        print(shipLength)
                if generatedShipDirection == 'genColumn':
                    shipLength = random.randint(0, self.columnAmount)
                    while iterationIndex < shipLength:
                        self._generatedField[generatedRow][generatedColumn + 1] = "O"
                        iterationIndex += 1
                        print(shipLength)
                        
                index += 1
        else:
            print("There are not enough places for the ships.") 
            
        return self._generatedField
    
    
    '''
    checks if there's a ship or not 
    shipsCounted: int - the amount of ships in the 'ocean' 
    success: int - the amount of found ships 
    '''
    def getVariableCont(self):
        shipsCounted: int = 0 
        success: int = -1
        
        '''
        code for counting the ships
        '''
        for indexRow in range(self.rowAmount):
            shipsCounted = shipsCounted + self._generatedField[indexRow].count('i')
            
        while success < shipsCounted:
            print(*self._generatedField, sep = "\n")
            
            rowIndexValue:int = int(input("Input Row Number: ")) - 1
            columnIndexValue:int = int(input("Input Column Number: ")) - 1
            

            if self._generatedField[rowIndexValue][columnIndexValue] == 'i':
                if self._generatedFieldCopy[rowIndexValue][columnIndexValue] != 'i':
                    self._generatedFieldCopy[rowIndexValue][columnIndexValue] = 'i'
                    print(*self._generatedField, sep = "\n")
                    success += 1
                    print("That's right!")
            elif self._generatedField[rowIndexValue][columnIndexValue] == 'x':
                print("That's wrong.")
    
    '''
    getter and setter functions used for debugging or testing purposes mostly
    '''
    def getField(self):
        return self._generatedField
    def getCopy(self): 
        return self._generatedFieldCopy
    def getIndex(self): 
        return self.listIndex


main = Main()
main.generateField()
main.generateShip()
main.getVariableCont()
