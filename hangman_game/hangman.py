import random
from hangman_art import stages, logo
from hangman_wordlist import word_list

word=random.choice(word_list)
print(logo)
# print(word)
health=len(word)
guessed_word=['_']*len(word)
win_flag=False

def disp_hangman(char):
    print(' '.join(guessed_word))
    if char :
        print(f"You guessed {char}, that's not in the word. You lose a life.")
    print(stages[health])
# 
def add_char(char):
    for i in range(0,len(word)):
        if char == word[i]:
            guessed_word[i]=word[i]
    return True if '_' not in guessed_word else False

while not win_flag:
    # try :
        current_char=input("Guess a letter: ").lower()
        if current_char in guessed_word: 
            print(f"{current_char}, Already guessed Character!")
        elif current_char in word:
            win_flag=add_char(current_char)
            disp_hangman(char=None)
        else :
            health-=1
            if health <= 0 : 
                break
            disp_hangman(char=current_char)
        if win_flag:
            print("You won")
            break
    # except :
    #     print("Something is wrong")

if not win_flag: print("You Lose")

