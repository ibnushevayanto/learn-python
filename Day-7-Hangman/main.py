import random

word_list = ["ardvark", "baboon", "camel"]
word = word_list[random.randint(0, len(word_list) - 1)]
savedGuessWord=[]
wrongCount=0

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                           
''')

asciiHangman = ['''
___________.._______
| .__________))______|
| | / /      
| |/ /       
| | /        
| |/         
| |          
| |          
| |        
| |        
| |       
| |      
| |     
| |     
| |     
| |     
| |     
| |         
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : : 
. .          `'       . .
''',
'''
___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         
| |        
| |       
| |      
| |     
| |     
| |     
| |     
| |     
| |     
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
''',
'''
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\
| |       // |   | \\
| |      //  | . |  \\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : : 
. .          `'       . .
''']

for idx in range(0, len(word)):
    savedGuessWord.append("_")
print("Can you guess the word: " + " ".join(savedGuessWord) + "\n")

def validateTheWord(theGuessWord):
    print("\n")
    index_theword_list = []
    # Mencari index dari kata, dengan membandingkan kata yang diinput
    for idx in range(0, len(word)):
        if theGuessWord == word[idx]:
            index_theword_list.append(idx)

    if len(index_theword_list) > 0:
        # Meletakkan kata, menggantikan kata yang kosong agar user mudah menebak selanjutnya
        for item in index_theword_list:
            savedGuessWord[item] = theGuessWord
        print(" ".join(savedGuessWord))
        print("Congratulation, you guessed it\n")
        return True
    else:
        return False

while True:
    theGuessWord = input("Guess a letter: ").lower()
    isValidate = validateTheWord(theGuessWord)
    if isValidate: 
        if("".join(savedGuessWord) == word):
            break
    else:
        print(f"You guessed {theGuessWord}, that's not in the word. You lose a life\n")
        print(asciiHangman[wrongCount])
        wrongCount += 1
        if wrongCount == 3:
            break

if wrongCount < 3:
    print("Congratulation you won!")
else:
    print("Oh no, you die")