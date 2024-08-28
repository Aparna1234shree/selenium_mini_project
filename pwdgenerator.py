# password_generator.py
import random
import string


def generate_password(length=12, use_special_chars=True):
    """Generate a random password.

    Args:
        length (int): Length of the password.
        use_special_chars (bool): Whether to include special characters.

    Returns:
        str: Randomly generated password.
    """
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    # Create a pool of characters to choose from
    char_pool = letters + digits + special_chars

    # Ensure the password includes at least one character from each set
    if use_special_chars:
        password = [
            random.choice(letters),
            random.choice(digits),
            random.choice(special_chars)
        ]
    else:
        password = [
            random.choice(letters),
            random.choice(digits)
        ]

    # Fill the rest of the password length with random choices from the pool
    password += random.choices(char_pool, k=length - len(password))

    # Shuffle the list to ensure randomness and join into a string
    random.shuffle(password)
    return ''.join(password)
