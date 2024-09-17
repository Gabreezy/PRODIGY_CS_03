import re
def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 0.5
    else:
        feedback.append("Password is too short. Should be at least 8 characters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 0.5
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 0.5
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 0.5
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"\W", password):
        strength += 0.5
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback based on strength
    if strength == 2.5:
        return "Password is strong!", feedback
    elif strength >= 1.5:
        return "Password is moderate.", feedback
    else:
        return "Password is weak.", feedback

def main():
    password = input("Enter a password: ")
    strength, feedback = assess_password_strength(password)
    print(strength)
    for item in feedback:
        print(item)

if __name__ == "__main__":
    main()
