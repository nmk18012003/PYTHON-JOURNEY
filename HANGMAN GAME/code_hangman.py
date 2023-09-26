import random
from stages import stage
from words import word_list

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

print("\n")

# word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

# print(chosen_word)

# n = len(chosen_word)
# blank_list = ["_"] * n
# print(blank_list)

lives = 6

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guesses the letter")
    # check guessed letter
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        # print(
        #     f"Current position : {i}\nCurrent letter : {letter}\nGuessed letter : {guess}")
        if letter == guess:
            display[i] = letter
        else:
            continue

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(stage[lives])
        if lives == 0:
            end_of_game = True
            print("You lose!!!")

    print(f"{' '.join(display)}")

if "_" not in display:
    end_of_game = True
    print("You Win!!")
