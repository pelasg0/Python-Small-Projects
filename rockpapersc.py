'''
imports
'''
import sys,time,random


class main: 
    _savedUserInput: int = 1
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
    
    _signs: list = ['rock', 'paper', 'scissors']

    def genUserInput(self): 
        self._savedUserInput = input('__' + '(1): ' + self._startSymbols[0] + '__' +  '(2): ' +  self._startSymbols[1] + '__' +  '(3): ' +  self._startSymbols[2] + 'Which one do you choose? ')
        return self._savedUserInput

    def genPcInput(self): 
        self._generatedPcInput = random.randint(1, 3)
        return self._generatedPcInput
    def compareInputs(self):
        pass
    def getUserInput(self):
        return self._savedUserInput
    
    def getPcInput(self):
        return self._generatedPcInput
    
main = main()
main.genUserInput()
main.genPcInput()


#print(main.getUserInput())




'''
ref link : https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
# Rock Paper Scissors ASCII Art

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
'''