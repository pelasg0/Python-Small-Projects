# create a greeting
# create your word list 
# randomly choose a word
# ask the user to guess the word 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 


import random


class main:


    _greeting: str
    _wordlist: []
    _randWord: str
    _charList: []
    

    def generateWordList(self):

        i: int
        wordListInput: []
        
        i = 3 

        wordListInput = input(f"Give me {i} words: ")
        self._wordlist = wordListInput.split()
        
        while len(self._wordlist) < i or len(self._wordlist) > i:
            wordListInput = input(f"You didn't give me {i} words: ")
            self._wordlist = wordListInput.split()

        if len(self._wordlist) == i:
            print("good")
            for word in self._wordlist:
                print(word)

        return self._wordlist

    def generateACharList(self):
        self._charList = list(self._randWord)

        for char in self._charList:
            print(char)

    def checkAChar(self):
        for char in self._charList:
            pass
    
    def selectAWord(self):
        randNumber = random.randint(0, len(self._wordlist) - 1)
        self._randWord = self._wordlist[randNumber]
        return self._randWord 
    
    def getAWord(self):
        print(self._randWord)


main = main()
main.generateWordList()
main.selectAWord()
main.getAWord()
main.generateACharList()