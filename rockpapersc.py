'''
imports
'''
import sys,time,random


class main: 
    _savedInput: int 
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

    def getUserInput(self): 
        self._savedInput: int = input('__' + '(1): ' + self._startSymbols[0] + '__' +  '(2): ' +  self._startSymbols[1] + '__' +  '(3): ' +  self._startSymbols[2] + 'Which one do you choose? ')
        

        return self._savedInput

    def getInput(self):
        return self._savedInput
    
main = main()
sign = main._signs
main.getUserInput()
#print(main.getInput())




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