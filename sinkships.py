
#imports
import random

class Main: 
    _generatedField: list = []
    #listIndex:int = 0
    
    def __init__(self):
        pass

    def generateField(self, _generatedField: list):
        self.rowAmount: int = int(input("Enter Amount of Rows: "))
        self.columnAmount: int = int(input("Enter Amount of Items on a Row: "))
        
        if(self.rowAmount):
            self._generatedField = [[None]] * self.rowAmount 
        if(self.columnAmount): 
                for i in range(0, self.rowAmount):  
                    self._generatedField[i] = ['x'] * self.columnAmount
        print(*self._generatedField, sep = "\n")
        return self._generatedField
    
        #return print(f"We have {str(self.columnAmount)} and {str(self.rowAmount)}")

    def generateShip(self):
        index: int = 0 #index for the loop so it counts the iterations
        generatedRow: int
        generatedColumn: int 
        generatedPlaces: int

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
            print(*self._generatedField, sep = "\n")
        
    def getField(self):
        return self._generatedField
        
    def getIndex(self): 
        return self.listIndex


main = Main()
savedField = main.getField()
main.generateField(savedField)
main.generateShip()
