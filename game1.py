import random

def play_game():
    print("🎮 Welcome to the Number Guessing Game! 🎮")
    print("I'm thinking of a number between 1 and 20.")
    print("You have exactly 3 attempts. Let's begin!\n")

    number = random.randint(1, 20)
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        # Input validation loop
        while True:
            try:
                mynumber = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
                # Check if the number is actually within the given range
                if 1 <= mynumber <= 20:
                    break
                else:
                    print("⚠️ Please stick to the rules! Enter a number between 1 and 20.")
            except ValueError:
                # This prevents the game from crashing if the user types a letter instead of a number
                print("⚠️ Invalid input! Please enter a whole number.")
        
        if mynumber == number:
            print(f"\n🎉 EXCELLENT! YOU GOT IT in {attempt} tries! 🎉")
            break
        elif mynumber > number:
            print("📉 Oh no! The original number is LOWER than your guess.")
        else:
            print("📈 Oops! The original number is HIGHER than your guess.")
            
        print("-" * 35) # Adds a clean visual separator between attempts
         
    else:
        # The 'else' block on a 'for' loop triggers only if the loop doesn't 'break'
        print(f"\n💀 GAME OVER! 💀 The correct number was: {number}")

# Main game loop allows the user to replay without restarting the script
while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay not in ('yes', 'y'):
        print("Thanks for playing! Goodbye. 👋")
        break
