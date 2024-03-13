
import tkinter as tk
from tkinter import messagebox
import re
import json
import random
import string


def check_password_strength(password):
    if len(password) < 8:
        return "Le mot de passe doit contenir au moins 8 caractères."
    elif not any(char.isupper() for char in password):
        return "Le mot de passe doit contenir au moins une lettre majuscule."
    elif not any(char.islower() for char in password):
        return "Le mot de passe doit contenir au moins une lettre minuscule."
    elif not any(char.isdigit() for char in password):
        return "Le mot de passe doit contenir au moins un chiffre."
    elif not re.search(r'[!@#$%^&*]', password):
        return "Le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)."
    else:
        return "Le mot de passe est valide."
    

def generate_random_password(length=12):
    if length < 8:
        print("Length should be at least 8 characters.")
        return

    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Use random.choice to generate a password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    print(password)

# Example: Generate a random password with a default length of 12 characters
generate_random_password()


# validation du password
def validate_password():
    password = password_entry.get()
    result = check_password_strength(password)
    if result == "Le mot de passe est valide.":
        messagebox.showinfo("Validation", result)
    else:
        messagebox.showerror("Validation", result)




root = tk.Tk()
root.geometry("800x500")
root.title("Password Window")
label = tk.Label(root, text="Enter your password", font=('Arial', 18))
label.pack(padx=20, pady=20)

# box pour metre le password
password_entry = tk.Entry(root, font = ("Arial", 12), show="*")  # Usar show="*" para ocultar o texto inserido
password_entry.pack(padx=10, pady=10)

# Button pour rentrer le password
button = tk.Button(root, text="Click here", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()