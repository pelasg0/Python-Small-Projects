
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
                    self._generatedField[i] = ['~'] * self.columnAmount
                    self._generatedFieldCopy[i] = ['~'] * self.columnAmount
        print(*self._generatedField, sep = "\n")
            
        return self._generatedField, self._generatedFieldCopy
        
    '''
        generetes ships that are marked as '𓊝' in the 'ocean' 
        index: int - index that counts the iterations of the loop
        generatedRow: int - where the random row position of the ship is saved
        generatedColumn: int - where the random column position of the ship is saved
        generatedPlaces: int - the amount of places in our ocean, if it's smaller than ship amoung -> else:
    '''
    def generateShip(self):

        generatedRow: int
        generatedColumn: int 
        shipLength: int 
        generatedShipDirection: int
        iterationIndex: int = 0
        directionChoice: list = ['genRow', 'genColumn']
        maxSymbols: int = 5
        
        shipAmount: int = int(input('Amount of Ships: '))
        index = 0 

        if shipAmount < self.rowAmount * self.columnAmount:
            while shipAmount > index:
                '''
                    -5 so i make sure that the ships dont come out of the bondary for now
                    not a permanent solution i promis :D 
                '''
                generatedRow = random.randint(0, self.rowAmount - 5)
                generatedColumn = random.randint(0, self.columnAmount - 5)
                
                generatedShipDirection = random.choice(directionChoice)
            
                if generatedShipDirection == 'genRow':
                    iterationIndex = 0
                    shipLength = random.randint(0, maxSymbols)
                    while iterationIndex < shipLength: 
                        self._generatedField[generatedRow + iterationIndex][generatedColumn] = '𓊝'
                        iterationIndex += 1
                if generatedShipDirection == 'genColumn':
                    #print(iterationIndex)
                    iterationIndex = 0
                    shipLength = random.randint(0, maxSymbols)
                    while iterationIndex < shipLength:
                        self._generatedField[generatedRow][generatedColumn + iterationIndex] = '𓊝' 
                        iterationIndex += 1

                index += 1
        else: 
            print('Too many ships.')
                
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
            shipsCounted = shipsCounted + self._generatedField[indexRow].count('𓊝')
            
        while success < shipsCounted:
            print(*self._generatedField, sep = "\n")
            
            rowIndexValue:int = int(input("Input Row Number: ")) - 1
            columnIndexValue:int = int(input("Input Column Number: ")) - 1
            

            if self._generatedField[rowIndexValue][columnIndexValue] == '𓊝':
                if self._generatedFieldCopy[rowIndexValue][columnIndexValue] != '𓊝':
                    self._generatedFieldCopy[rowIndexValue][columnIndexValue] = '𓊝'
                    print(*self._generatedField, sep = "\n")
                    success += 1
                    print("That's right!")
                else: 
                    print("That's wrong.")
            elif self._generatedField[rowIndexValue][columnIndexValue] == '~':
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
