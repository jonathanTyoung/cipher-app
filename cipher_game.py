from encryptor import (
    generate_puzzle,
    decrypt_with_partial_key,
    analyze_frequency
)

def play_game():
    """Play the cipher-breaking game"""
    
    print("\n" + "="*60)
    print("     🔐 CIPHER BREAKER GAME 🔐")
    print("="*60)
    print("\nCan you crack the code?\n")
    
    # Generate a puzzle
    puzzle = generate_puzzle('easy')
    encrypted = puzzle['encrypted']
    solution = puzzle['solution']
    
    # Track what the player has guessed
    user_guesses = {}  # Will be like: {'X': 'H', 'Q': 'E', ...}
    attempts = 0
    
    # Show the encrypted message
    print(f"Encrypted message:")
    print(f">>> {encrypted} <<<\n")
    
    # Show frequency hints
    print("Letter frequencies (top 5):")
    freq = analyze_frequency(encrypted)
    for letter, count in freq[:5]:
        print(f"  {letter}: {count} times")
    
    print("\n💡 Hint: In English, the most common letters are")
    print("   E, T, A, O, I, N, S, H, R")
    print()
    
    # Main game loop
    while True:
        print("="*60)
        
        # Show current progress
        progress = decrypt_with_partial_key(encrypted, user_guesses)
        print(f"\nYour progress:")
        print(f">>> {progress} <<<\n")
        
        # Check if solved
        if progress == solution:
            print("\n🎉 CONGRATULATIONS! YOU CRACKED IT! 🎉")
            print(f"You solved it in {attempts} guesses!")
            break
        
        # Show menu
        print("What do you want to do?")
        print("  1 - Make a guess (example: X=E)")
        print("  2 - See frequencies again")
        print("  3 - Give up and see answer")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "1":
            # Get their guess
            guess = input("Enter guess (like X=E): ").strip().upper()
            
            # Validate the guess
            if '=' not in guess:
                print("❌ Use format: X=E")
                continue
            
            parts = guess.split('=')
            if len(parts) != 2:
                print("❌ Use format: X=E")
                continue
            
            encrypted_letter = parts[0].strip()
            actual_letter = parts[1].strip()
            
            if len(encrypted_letter) != 1 or len(actual_letter) != 1:
                print("❌ Enter exactly one letter on each side")
                continue
            
            if not encrypted_letter.isalpha() or not actual_letter.isalpha():
                print("❌ Use only letters")
                continue
            
            # Save their guess
            user_guesses[encrypted_letter] = actual_letter
            attempts += 1
            print(f"✓ You mapped: {encrypted_letter} → {actual_letter}")
            
        elif choice == "2":
            # Show frequencies again
            print("\nAll letter frequencies:")
            for letter, count in freq:
                print(f"  {letter}: {count} times")
            print()
            
        elif choice == "3":
            # Give up
            print(f"\n💡 The answer was: {solution}")
            print("Better luck next time!")
            break
            
        else:
            print("❌ Please enter 1, 2, or 3")

# Run the game
if __name__ == "__main__":
    play_game()