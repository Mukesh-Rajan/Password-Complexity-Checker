import re

def assess_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = bool(re.match(r'^[\W_]+$', password))  # Matches special characters

    # Calculate score based on criteria
    score = 0
    if length >= 8:
        score += 1
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digit:
        score += 1
    if special_char:
        score += 1
    
    # Determine strength based on score
    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Moderate"
    elif score <= 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return strength

# Example usage:
password = input("Enter your password: ")
strength = assess_password_strength(password)
print("Password Strength:", strength)
