import random
words = ["python","java","html","css","php"]
selected_words= random.choice(words)
hidden = []
for letter in selected_words:
    hidden.append("-")
print(hidden)
lives = 6

while lives > 0:
    guess = input("Guess a letter: ")
    
    if guess in selected_words:
        print("Correct!")
        for i in range(len(selected_words)):
            if selected_words[i] == guess:
                hidden[i] = guess
        print(hidden)
        if "-" not in hidden:
            print("You Win!")
            print(f"Word was: {selected_words}")
            break
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
        if lives == 0:
            print("Game Over!")