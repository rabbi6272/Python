
#the hangman game
import random
import art
import words 
endOfGame = False
lives = 6
selected_word = random.choice(words.word_list)

length = len(selected_word)

print(art.logo)

blank = []
for x in range(length):
  blank.append("_")
print(f"{" ".join(blank)}")

while not endOfGame:
  input_letter = input("Guess a letter: ").lower()

  if input_letter in blank:
    print("You gussed a letter which already exists.")
  else:
    for position in range(length):
      current_letter = selected_word[position]
      if input_letter == current_letter:
        blank[position] = input_letter
        print("You gussed a letter correctly.")

  if input_letter not in selected_word:
    lives -= 1
    print("You gussed a letter that is not in the word. You loose a life")
    print(art.stages[lives])

  print(f"{" ".join(blank)}")

  if lives==0 and "_" in blank:
    endOfGame = True
    print("You loose.")

  if "_" not in blank:
    endOfGame = True
    print("You win.")
  
    


