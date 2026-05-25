import random
words = ["python", "hangman", "random", "string"]
word = random.choice(words)
guessed = ["_"]*len(word)
attempts = 6
used_letters = []
print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))
while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    used_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess:", "".join(guessed))
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")
        print("Word:", " ".join(guessed))
if "_" not in guessed:
    print("Congratulations! You guessed the word:",word)
else:
    print("Game Over1 The word was:",word)