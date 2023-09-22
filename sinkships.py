

class Main: 
    _generatedField:[]
    listIndex:int = 0
    
    def __init__(self):
        pass

    def generateField(self):
        self.columnAmount = input("Enter Amount of Items on a Row: ")
        self.rowAmount = input("Enter Amount of Rows: ")
        
        return print(f"We have {self.columnAmount} and {self.rowAmount}")
        
    def getField(self):
        return self._generatedField


main = Main()
print(main.generateField())
