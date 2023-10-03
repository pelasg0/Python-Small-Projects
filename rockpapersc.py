'''
imports
'''
import sys,time,random


class Main: 
    _savedUserInput: int
    _generatedPcInput: int 
    _startSymbols: list = [''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', 
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
    
    def genUserInput(self): 
        self._savedUserInput = int(input('__' + '(1): ' + self._startSymbols[0] + '__' +  '(2): ' +  self._startSymbols[1] + '__' +  '(3): ' +  self._startSymbols[2] + 'Which one do you choose? '))
        print(self._startSymbols[self._savedUserInput - 1])
        return self._savedUserInput
    
    def genPcInput(self): 
        self._generatedPcInput = random.randint(1, 3)
        print(self._startSymbols[self._generatedPcInput - 1])
        return self._generatedPcInput
    
    def compareInputs(self):
        if self._savedUserInput == 1 and self._generatedPcInput == 3 or self._savedUserInput == 2 and self._generatedPcInput == 1 or self._savedUserInput == 3 and self._generatedPcInput == 2:
            print("User Won")
        elif self._generatedPcInput == 1 and self._savedUserInput == 3 or self._generatedPcInput == 2 and self._savedUserInput == 1 or self._generatedPcInput == 3 and self._savedUserInput == 2:
            print("Pc Won")
        else:
            print("Draw")

    def getUserInput(self):
        return self._savedUserInput
    
    def getPcInput(self):
        return self._generatedPcInput
    

def play():
    main = Main()
    main.genUserInput()
    main.genPcInput()
    main.compareInputs()

play()
