

class Main: 
    _generatedField:[] = [["x"]]
    listIndex:int = 0
    
    def __init__(self) :
        pass

    def generateField(self):
        sideA:int = int(input("How many rows?"))
        sideB:int = int(input("How many columns?"))

        while len(self._generatedField) < sideA:
            self._generatedField.append(globals()["list_" + str(self.listIndex) + "_"])
            self.listIndex += 1 
        while len(globals()["list_" + str(self.listIndex) + "_"]) < sideB:
            globals()["list_" + str(self.listIndex) + "_"].append("x")
    
    
    def getField(self):
        return self._generatedField
    '''
    def getIndex(self):
        return self.listIndex
    '''

main = Main()
main.generateField()
print(main.getField())

