#Step 5
import os
import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(' '.join(display))
guessed_letter = []
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    os.system('cls')


    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in guessed_letter:
      print(f"You've already guessed \"{guess}\". Choose a new one!")
    #Check if user is wrong.
    elif guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        guessed_letter.append(guess)
        lives -= 1
        print(f"You guessed \"{guess}\" that is not in the word so you lose a life")
        if lives == 0:
            end_of_game = True
            print(f"You lose.\nThe word was {chosen_word}.")
    else:
      guessed_letter.append(guess)
      print(f"You guessed \"{guess}\" correctly!")
      #Check guessed letter
      for position in range(word_length):
          letter = chosen_word[position]
  #        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter



    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
