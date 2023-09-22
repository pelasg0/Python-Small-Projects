

class Main: 
    _generatedField = []
    listIndex:int = 0
    
    def __init__(self):
        pass

    def generateField(self, _generatedField):
        self.columnAmount = int(input("Enter Amount of Items on a Row: "))
        self.rowAmount = int(input("Enter Amount of Rows: "))
        
        while self.columnAmount > len(self._generatedField):
            self._generatedField = [None] * self.columnAmount
            self._generatedField[self.listIndex] = "x"
            self.listIndex += 1
            print("yes")
        
        return print(f"We have {str(self.columnAmount)} and {str(self.rowAmount)}")
        
    def getField(self):
        return self._generatedField
        
    def getIndex(self): 
        return self.listIndex


main = Main()
savedField = main.getField()
main.generateField(savedField)
