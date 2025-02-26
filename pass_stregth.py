import re

def check_password_strengt;h(password):
    strength = 0
    suggestions = []
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make it at least 8 characters long.")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")
    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Add at least one number.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Include special characters like @, #, $.")

    if strength == 4:
        return "Strong Password!", suggestions
    elif strength == 3:
        return "Medium Password.", suggestions
    else:
        return "Weak Password!", suggestions
password = input("Enter your password: ")
strength, tips = check_password_strength(password)

print(f"Password Strength: {strength}")
if tips:
    print("Suggestions to improve:")
    for tip in tips:
        print(f"- {tip}")