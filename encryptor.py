import random
import string


def generate_cipher_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)

    cipher_key = dict(zip(alphabet, shuffled))
    return cipher_key


def encrypt_message(message, cipher_key):
    encrypted = ""

    for char in message.upper():
        if char in cipher_key:
            encrypted += cipher_key[char]
        else:
            encrypted += char

    return encrypted


def decrypt_message(encrypted, cipher_key):
    """Decrypt a message using the cipher key"""

    # Create reverse key: if 'A' → 'M', make it 'M' → 'A'
    reverse_key = {v: k for k, v in cipher_key.items()}

    decrypted = ""

    for char in encrypted:
        if char in reverse_key:
            decrypted += reverse_key[char]
        else:
            # Keep spaces, punctuation as-is
            decrypted += char

    return decrypted


def decrypt_with_partial_key(encrypted, partial_key):
    """
    Decrypt using only the letters user has guessed so far.
    Unguessed letters show as underscores.
    Used for the game - shows progress as player guesses.
    """
    result = ""

    for char in encrypted:
        if char in partial_key:
            # User has guessed this letter
            result += partial_key[char]
        elif char.isalpha():
            # Letter not guessed yet - show as underscore
            result += "_"
        else:
            # Keep spaces, punctuation
            result += char

    return result


def analyze_frequency(text):
    """Count how often each letter appears in the text"""
    from collections import Counter

    # Get only letters, make them uppercase
    letters = [c for c in text.upper() if c.isalpha()]

    # Count how many times each letter appears
    freq = Counter(letters)

    # Return them sorted by most common first
    # Returns a list like: [('E', 5), ('T', 3), ('A', 2), ...]
    return freq.most_common()


def generate_puzzle(difficulty="easy"):
    """Generate an encrypted puzzle with solution"""
    import random

    # Library of messages by difficulty
    messages = {
        "easy": [
            "HELLO WORLD",
            "MEET ME AT NOON",
            "THE QUICK BROWN FOX",
            "SECRET MESSAGE",
            "CODE BREAKER",
        ],
        "medium": [
            "TO BE OR NOT TO BE THAT IS THE QUESTION",
            "THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF",
        ],
        "hard": ["IN THE BEGINNING WAS THE WORD AND THE WORD WAS WITH GOD"],
    }

    # Pick a random message for this difficulty
    message = random.choice(messages[difficulty])

    # Generate key and encrypt it
    key = generate_cipher_key()
    encrypted = encrypt_message(message, key)

    # Return everything we need
    return {
        "encrypted": encrypted,
        "solution": message,
        "key": key,
        "difficulty": difficulty,
    }


if __name__ == "__main__":
    print("=" * 50)
    print("TESTING PUZZLE GENERATOR")
    print("=" * 50)

    # Generate an easy puzzle
    puzzle = generate_puzzle("easy")

    print(f"\nDifficulty: {puzzle['difficulty']}")
    print(f"Encrypted:  {puzzle['encrypted']}")
    print(f"Solution:   {puzzle['solution']}")
    print()

    # Show frequency analysis of the puzzle
    print("Frequency Analysis:")
    frequencies = analyze_frequency(puzzle["encrypted"])
    for letter, count in frequencies[:5]:  # Top 5 only
        print(f"  {letter}: {count} times")

# # Test it
# if __name__ == "__main__":
#     # Generate key and encrypt
#     key = generate_cipher_key()
#     message = "HELLO WORLD"
#     encrypted = encrypt_message(message, key)

#     print(f"Original:  {message}")
#     print(f"Encrypted: {encrypted}")
#     print(f"Key: {key}")
#     print()

#     # Full decryption (with complete key)
#     decrypted = decrypt_message(encrypted, key)
#     print(f"Decrypted: {decrypted}")
#     print()

#     # NEW: Test frequency analysis
#     print("Frequency Analysis:")
#     frequencies = analyze_frequency(encrypted)
#     for letter, count in frequencies:
#         print(f"  {letter}: {count} times")

#     # Partial decryption (simulating player guesses)
#     # Let's say player only guessed a few letters
#     partial = {"X": "H", "T": "E"}  # Example: if X was H and T was E
#     progress = decrypt_with_partial_key(encrypted, partial)
#     print(f"Partial decrypt (player's progress): {progress}")
