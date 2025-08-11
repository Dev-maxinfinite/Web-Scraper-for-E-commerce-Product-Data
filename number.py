import random

def number_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    print("===================================")
    
    # Set the range for the random number
    min_num = 1
    max_num = 100
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"I'm thinking of a number between {min_num} and {max_num}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < min_num or guess > max_num:
                print(f"Please enter a number between {min_num} and {max_num}.")
                continue
                
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    number_guessing_game()
