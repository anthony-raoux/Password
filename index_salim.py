## Importation du module tkinter pour créer une interface graphique ##
import tkinter as tk  # Importe le module tkinter et le renomme en 'tk' pour une utilisation plus concise
from tkinter import messagebox  # Importe uniquement la classe 'messagebox' de tkinter pour afficher les boîtes de dialogue
import re  # Importe le module 're' pour utiliser des expressions régulières(********) dans la vérification du mot de passe
import hashlib  # Importe le module 'hashlib' pour le hachage des mots de passe
import json  # Importe le module 'json' pour lire et écrire des données au format JSON
import random  # Importe le module 'random' pour la génération de mots de passe aléatoires

#---------------------------------------------#
## Fonction pour vérifier si le mot de passe respecte les exigences de sécurité ##
def verify_password(password):
    # Vérifier la longueur du mot de passe
    if len(password) < 8:
        return False, "Il doit contenir au moins 8 caractères."
    # Vérifier s'il contient au moins une lettre majuscule
    if not any(char.isupper() for char in password):
        return False, "Il doit contenir au moins une lettre majuscule."
    # Vérifier s'il contient au moins une lettre minuscule
    if not any(char.islower() for char in password):
        return False, "Il doit con tenir au moins une lettre minuscule."
    # Vérifier s'il contient au moins un chiffre
    if not any(char.isdigit() for char in password):
        return False, "Il doit contenir au moins un chiffre."
    # Vérifier s'il contient au moins un caractère spécial
    if not re.search(r'[!@#$%^&*]', password):
        return False, "Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *)."
    # Si toutes les conditions sont satisfaites, le mot de passe est valide
    return True, ""

#---------------------------------------------#
## Fonction pour crypter un mot de passe avec SHA-256 ##
def hash_password(password):  # Définition de la fonction 'hash_password' prenant un paramètre 'password'
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  
    # Utilise l'algorithme de hachage SHA-256 pour hacher le mot de passe fourni.
    # hashlib.sha256() crée un objet de hachage SHA-256.
    # password.encode() convertit le mot de passe en une séquence d'octets.
    # .hexdigest() convertit le résultat haché en une chaîne hexadécimale.
    return hashed_password  # Retourne le mot de passe haché


#---------------------------------------------#
## Fonction pour charger les mots de passe enregistrés depuis un fichier JSON ##
def load_passwords():  # Définition de la fonction 'load_passwords'
    try:  # Essayer d'exécuter le code suivant
        with open("passwords.json", "r") as file:  
            # Ouvre le fichier "passwords.json" en mode lecture ("r") et le renomme en 'file'
            return json.load(file)  
            # Charge les données JSON à partir du fichier 'file' et les retourne
    except FileNotFoundError:  
        # Si le fichier "passwords.json" n'est pas trouvé, une exception FileNotFoundError est levée
        return []  # Retourne une liste vide si le fichier n'est pas trouvé


#---------------------------------------------#
# Fonction pour enregistrer un mot de passe haché dans un fichier JSON
def save_password(username, password_hash):  
    # Définition de la fonction 'save_password' prenant deux paramètres : 'username' et 'password_hash'
    passwords = load_passwords()  
    # Charge les mots de passe enregistrés depuis le fichier JSON
    # passwords contient la liste des mots de passe déjà enregistrés

    # Vérifier si le mot de passe est déjà enregistré
    for entry in passwords:  
        # Parcours chaque entrée (dictionnaire) dans la liste des mots de passe
        if entry['password_hash'] == password_hash:  
            # Vérifie si le mot de passe haché fourni est déjà présent dans la liste
            return False  
            # Si le mot de passe est déjà enregistré, retourne False et quitte la fonction
    
    passwords.append({"username": username, "password_hash": password_hash})  
    # Si le mot de passe n'est pas déjà enregistré, ajoute un nouveau dictionnaire à la liste 'passwords' contenant le nom d'utilisateur et le mot de passe haché
    
    with open("passwords.json", "w") as file:  
        # Ouvre le fichier "passwords.json" en mode écriture ("w") et le renomme en 'file'
        json.dump(passwords, file)  
        # Écrit les données JSON (la liste des mots de passe mise à jour) dans le fichier 'file'
    
    return True  
    # Retourne True pour indiquer que le mot de passe a été enregistré avec succès


#---------------------------------------------#
# Fonction pour vérifier si un mot de passe est déjà enregistré
def is_password_registered(password):  
    # Définition de la fonction 'is_password_registered' prenant un paramètre 'password'

    hashed_password = hash_password(password)  
    # Hache le mot de passe fourni en utilisant la fonction 'hash_password' pour obtenir son haché correspondant

    passwords = load_passwords()  
    # Charge les mots de passe enregistrés depuis le fichier JSON
    # passwords contient la liste des mots de passe déjà enregistrés

    for entry in passwords:  
        # Parcours chaque entrée (dictionnaire) dans la liste des mots de passe
        if entry['password_hash'] == hashed_password:  
            # Vérifie si le mot de passe haché fourni est présent dans la liste des mots de passe
            return True  
            # Si le mot de passe est trouvé, retourne True et quitte la fonction

    return False  
    # Si le mot de passe n'est pas trouvé dans la liste, retourne False


#---------------------------------------------#
# Fonction pour générer un mot de passe aléatoire qui respecte les exigences
def generate_random_password():  
    # Définition de la fonction 'generate_random_password'

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"  
    # Définition d'une chaîne de caractères contenant tous les caractères possibles pour générer un mot de passe aléatoire

    while True:  
        # Boucle infinie pour générer des mots de passe jusqu'à ce qu'un mot de passe valide soit trouvé

        password = ''.join(random.choice(characters) for i in range(12))  
        # Génère une chaîne de 12 caractères en choisissant aléatoirement des caractères de 'characters'
        # La fonction random.choice() est utilisée pour choisir aléatoirement un caractère de 'characters' et la boucle for itère 12 fois pour obtenir une chaîne de longueur 12
        
        if verify_password(password)[0] and not is_password_registered(password):  
            # Vérifie si le mot de passe généré est valide et non déjà enregistré
            # verify_password(password)[0] vérifie si le mot de passe est valide en appelant la fonction verify_password et en accédant au premier élément du tuple retourné
            # is_password_registered(password) vérifie si le mot de passe est déjà enregistré en appelant la fonction is_password_registered
            
            return password  
            # Si le mot de passe est valide et non déjà enregistré, retourne le mot de passe


#---------------------------------------------#
# Fonction pour gérer la soumission du formulaire
def submit_form():  
    # Définition de la fonction 'submit_form'

    username = username_entry.get()  
    # Récupère le contenu de l'entrée 'username_entry' (nom d'utilisateur) et l'assigne à la variable 'username'

    password = password_entry.get()  
    # Récupère le contenu de l'entrée 'password_entry' (mot de passe) et l'assigne à la variable 'password'

    is_valid, error_message = verify_password(password)  
    # Appelle la fonction 'verify_password' pour vérifier si le mot de passe est valide et récupère le résultat dans les variables 'is_valid' et 'error_message'

    if is_valid:  
        # Si le mot de passe est valide (is_valid vaut True)

        hashed_password = hash_password(password)  
        # Hache le mot de passe en utilisant la fonction 'hash_password' pour obtenir son haché correspondant

        if save_password(username, hashed_password):  
            # Appelle la fonction 'save_password' pour enregistrer le nom d'utilisateur et le mot de passe haché dans le fichier JSON
            # Si l'enregistrement est réussi (retourne True)

            success_label = tk.Label(center_frame, text="Mot de passe enregistré avec succès.", fg="green", bg="#000")  
            # Crée un label de succès avec un message spécifique et les couleurs de texte et de fond appropriées

            success_label.pack(pady=5)  
            # Ajoute le label de succès au cadre central avec une marge en bas de 5 pixels

            root.after(5000, root.destroy)  
            # Utilise la méthode after() pour planifier la fermeture de la fenêtre principale après 5000 millisecondes (5 secondes)

        else:  
            # Si le mot de passe est déjà enregistré (retourne False)

            error_message_label.config(text="Ce mot de passe est déjà enregistré.", fg="yellow")  
            # Modifie le texte du label d'erreur pour afficher un message spécifique

    else:  
        # Si le mot de passe n'est pas valide (is_valid vaut False)

        error_label.config(text=error_message, fg="red")  
        # Modifie le texte du label d'erreur pour afficher le message d'erreur retourné par la fonction 'verify_password', avec une couleur de texte rouge


#---------------------------------------------#
# Fonction pour générer et afficher un mot de passe aléatoire
def generate_and_show_random_password():  
    # Définition de la fonction 'generate_and_show_random_password'

    random_password = generate_random_password()  
    # Appelle la fonction 'generate_random_password' pour générer un mot de passe aléatoire et l'assigne à la variable 'random_password'

    password_entry.delete(0, tk.END)  
    # Efface le contenu actuel de l'entrée 'password_entry' en supprimant tous les caractères de la position 0 (début) à la position tk.END (fin)

    password_entry.insert(0, random_password)  
    # Insère le mot de passe aléatoire généré dans l'entrée 'password_entry' à la position 0 (début)


#---------------------------------------------#
# Fonction pour dévoiler ou cacher le mot de passe
def toggle_password_visibility():  
    # Définition de la fonction 'toggle_password_visibility'

    if password_entry.cget("show") == "*":  
        # Vérifie si l'option 'show' de l'entrée 'password_entry' est définie sur '*' (indiquant que le mot de passe est actuellement masqué)

        password_entry.config(show="")  
        # Si le mot de passe est actuellement masqué, configure l'entrée 'password_entry' pour afficher le mot de passe en clair en affectant une chaîne vide à l'option 'show'

        toggle_button.config(text="Cacher le mot de passe")  
        # Change le texte du bouton 'toggle_button' pour indiquer qu'il permet de cacher le mot de passe

    else:  
        # Si l'option 'show' de l'entrée 'password_entry' n'est pas définie sur '*' (indiquant que le mot de passe est actuellement affiché en clair)

        password_entry.config(show="*")  
        # Si le mot de passe est actuellement affiché en clair, configure l'entrée 'password_entry' pour masquer le mot de passe en affectant '*' à l'option 'show'

        toggle_button.config(text="Dévoiler le mot de passe")  
        # Change le texte du bouton 'toggle_button' pour indiquer qu'il permet de dévoiler le mot de passe


#---------------------------------------------#
# Interface graphique avec Tkinter
root = tk.Tk()  
# Crée une instance de la classe Tk() de tkinter, qui représente la fenêtre principale de l'application

root.title("Gestionnaire de mots de passe")  
# Définit le titre de la fenêtre principale comme "Gestionnaire de mots de passe"

root.geometry("500x500")  
# Définit la taille de la fenêtre principale comme 500 pixels de largeur sur 500 pixels de hauteur

root.configure(bg="#000")  
# Configure la couleur de fond de la fenêtre principale en noir (#000)

# Frame pour centrer le contenu
center_frame = tk.Frame(root, bg="#000", padx=5, pady=5)  
# Crée un cadre (Frame) qui servira à centrer le contenu dans la fenêtre principale
# Le cadre a une couleur de fond noire (#000) et des marges de 5 pixels à gauche et en haut

center_frame.place(relx=0.5, rely=0.5, anchor="center")  
# Place le cadre au centre de la fenêtre principale en utilisant les coordonnées relatives relx et rely
# L'ancre (anchor) est définie sur "center" pour centrer le cadre

# Création des éléments de l'interface

error_message_label = tk.Label(center_frame, text="", fg="yellow", bg="#000")  
# Crée une étiquette (Label) pour afficher les messages d'erreur
# L'étiquette a un texte vide au départ, une couleur de texte jaune (fg) et un fond noir (#000)

error_message_label.pack(pady=(25, 5))  
# Place l'étiquette dans le cadre avec une marge de 25 pixels en haut et de 5 pixels en bas

username_label = tk.Label(center_frame, text="Nom d'utilisateur:", fg="#fff", bg="#000")  
# Crée une étiquette pour afficher le texte "Nom d'utilisateur"
# L'étiquette a une couleur de texte blanche (fg) et un fond noir (#000)

username_label.pack(pady=(0, 5))  
# Place l'étiquette dans le cadre avec une marge de 5 pixels en bas

username_entry = tk.Entry(center_frame)  
# Crée une entrée (Entry) pour que l'utilisateur saisisse son nom d'utilisateur

username_entry.pack(pady=(5, 5))  
# Place l'entrée dans le cadre avec une marge de 5 pixels en bas

password_label = tk.Label(center_frame, text="Mot de passe:", fg="#fff", bg="#000")  
# Crée une étiquette pour afficher le texte "Mot de passe"
# L'étiquette a une couleur de texte blanche (fg) et un fond noir (#000)

password_label.pack(pady=(25, 5))  
# Place l'étiquette dans le cadre avec une marge de 25 pixels en bas

password_entry = tk.Entry(center_frame, show="*")  
# Crée une entrée (Entry) pour que l'utilisateur saisisse son mot de passe
# L'option 'show' est définie sur '*' pour masquer les caractères du mot de passe

password_entry.pack(pady=(0, 5))  
# Place l'entrée dans le cadre avec une marge de 5 pixels en bas

# Bouton pour dévoiler ou cacher le mot de passe
toggle_button = tk.Button(center_frame, text="Dévoiler le mot de passe", command=toggle_password_visibility, bg="#fff")  
# Crée un bouton pour permettre à l'utilisateur de dévoiler ou de cacher le mot de passe
# Le bouton a un texte spécifique, une commande associée pour basculer la visibilité du mot de passe et un fond blanc (#fff)

toggle_button.pack(pady=(5, 5))  
# Place le bouton dans le cadre avec une marge de 5 pixels en bas

generate_password_button = tk.Button(center_frame, text="Générer un mot de passe aléatoire", command=generate_and_show_random_password, bg="#fff")  
# Crée un bouton pour permettre à l'utilisateur de générer un mot de passe aléatoire
# Le bouton a un texte spécifique, une commande associée pour générer et afficher le mot de passe aléatoire et un fond blanc (#fff)

generate_password_button.pack(pady=(25, 5))  
# Place le bouton dans le cadre avec une marge de 5 pixels en bas

submit_button = tk.Button(center_frame, text="Valider", command=submit_form, bg="#fff")  
# Crée un bouton pour permettre à l'utilisateur de valider le formulaire
# Le bouton a un texte spécifique, une commande associée pour soumettre le formulaire et un fond blanc (#fff)

submit_button.pack(pady=(25, 0))  
# Place le bouton dans le cadre avec une marge de 50 pixels en bas

error_label = tk.Label(center_frame, text="", fg="red", bg="#000")  
# Crée une étiquette pour afficher les messages d'erreur
# L'étiquette a un texte vide au départ, une couleur de texte rouge (fg) et un fond noir (#000)

error_label.pack(pady=(0, 5))  
# Place l'étiquette dans le cadre avec une marge de 5 pixels en bas

# Lancer l'interface
root.mainloop()  
# Lance la boucle principale de l'interface graphique pour afficher la fenêtre et répondre aux événements de l'utilisateur







