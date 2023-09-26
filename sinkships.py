
#imports
import random

class Main: 
    _generatedField: list = []
    _generatedFieldCopy: list = []
    
    def __init__(self):
        pass

    def generateField(self):
        self.rowAmount: int = int(input("Enter Amount of Rows: "))
        self.columnAmount: int = int(input("Enter Amount of Items on a Row: "))
        
        if(self.rowAmount):
            self._generatedField = [[None]] * self.rowAmount 
            self._generatedFieldCopy = [[None]] * self.rowAmount
        if(self.columnAmount): 
                for i in range(0, self.rowAmount):  
                    self._generatedField[i] = ['x'] * self.columnAmount
                    self._generatedFieldCopy[i] = ['x'] * self.columnAmount
        print(*self._generatedField, sep = "\n")
        
        return self._generatedField, self._generatedFieldCopy
    
    def generateShip(self):
        index: int = 0 #index for the loop so it counts the iterations
        generatedRow: int
        generatedColumn: int 
        generatedPlaces: int = self.rowAmount * self.columnAmount

        self.shipAmount: int = int(input("Enter Amount of Ships: "))

        if self.shipAmount <= generatedPlaces: 
            while self.shipAmount > index: 
                generatedRow = random.randint(0, self.rowAmount - 1)
                generatedColumn = random.randint(0, self.columnAmount - 1)

                self._generatedField[generatedRow][generatedColumn] = "i"
                index += 1
        else:
            print("There are not enough places for the ships.") 
        if index == self.shipAmount: #print the ocean
            #print(*self._generatedField, sep = "\n")
            pass
        
                
        return self._generatedField
    
    def getVariableCont(self):
        shipsCounted: int = 0 
        success: int = 0
        
        '''
        code for counting the ships
        '''
        for indexRow in range(self.rowAmount):
            shipsCounted = shipsCounted + self._generatedField[indexRow].count('i')
            
        while success < shipsCounted:
            print(*self._generatedFieldCopy, sep = "\n")
            
            rowIndexValue:int = int(input("Input Row Number: ")) - 1
            columnIndexValue:int = int(input("Input Column Number: ")) - 1
            
            if type(rowIndexValue) == int and type(columnIndexValue) == int:
                if self._generatedField[rowIndexValue][columnIndexValue]:
                    if self._generatedField[rowIndexValue][columnIndexValue] == 'i':
                        if self._generatedFieldCopy[rowIndexValue][columnIndexValue] != 'i':
                            self._generatedFieldCopy[rowIndexValue][columnIndexValue] = 'i'
                            print(*self._generatedFieldCopy, sep = "\n")
                            success += 1
                            print("That's right!")
                    elif self._generatedField[rowIndexValue][columnIndexValue] == 'x':
                        print("That's wrong.")
                        #print(*self._generatedField, sep = "\n")
   
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
