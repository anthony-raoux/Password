from tkinter import *
import customtkinter
import hashlib
import json
import random
import string
from CTkMessagebox import CTkMessagebox
from customtkinter import CTkButton, CTk

# Fonction pour vérifier la sécurité du mot de passe

def est_mot_de_passe_securise(mot_de_passe):
    return (
        len(mot_de_passe) >= 8 and
        any(char.isupper() for char in mot_de_passe) and
        any(char.islower() for char in mot_de_passe) and
        any(char.isdigit() for char in mot_de_passe) and
        any(char in "!@#$%^&*" for char in mot_de_passe)
    )

# Fonction pour crypter un mot de passe

def crypter_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

#fonction pour doublons

def comparer_mots_de_passe(mdp1, mdp2):
    return mdp1 == mdp2

# Fonction pour sauvegarder un nom d'utilisateur et son mot de passe dans un fichier JSON

def sauvegarder_mot_de_passe(nom_utilisateur, mot_de_passe):
    donnees = {}
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        pass

    if nom_utilisateur in donnees:
        CTkMessagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà \u2764 Choisissez un autre nom.")
    else:
        for nom_utilisateur, mdp in donnees.items():
            if comparer_mots_de_passe(mdp, crypter_mot_de_passe(mot_de_passe)):
                CTkMessagebox.showerror("Erreur", "Ce mot de passe existe déjà \u2764 Choisissez un autre mot de passe.")
                return

        mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
        donnees[nom_utilisateur] = mot_de_passe_crypte
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(donnees, fichier)
        CTkMessagebox.showinfo("Mot de passe enregistré", "Bravo !")

# Fonction pour générer un mot de passe aléatoire

def generer_mot_de_passe_aleatoire():
    chiffre = random.choice(string.digits)
    caractere_special = random.choice("!@#$%^&*")
    majuscule = random.choice(string.ascii_uppercase)
    minuscule = random.choice(string.ascii_lowercase)

    caracteres = string.digits + "!@#$%^&*" + string.ascii_uppercase + string.ascii_lowercase
    mot_de_passe = chiffre + caractere_special + majuscule + minuscule + ''.join(random.choice(caracteres) for _ in range(4))
    
    mot_de_passe = ''.join(random.sample(mot_de_passe, len(mot_de_passe)))
    
    return mot_de_passe

# Fonction pour valider le mot de passe saisi par l'utilisateur et sauvegarder s'il est sécurisé

def valider_mot_de_passe():
    mot_de_passe = entry_mot_de_passe.get()
    if est_mot_de_passe_securise(mot_de_passe):
        sauvegarder_mot_de_passe(entry_nom_utilisateur.get(), mot_de_passe)
        root.destroy()
    else:
        CTkMessagebox.showerror(">o<", "Mot de passe invalide, fais un effort \u2764 ")

# Fonction pour générer un mot de passe aléatoire et l'afficher dans l'entrée de texte

def generer_mot_de_passe_aleatoire_et_afficher():
    mot_de_passe_aleatoire = generer_mot_de_passe_aleatoire()
    entry_mot_de_passe.delete(0, tk.END)
    entry_mot_de_passe.insert(0, mot_de_passe_aleatoire)

# Fonction pour afficher les mots de passe enregistrés

def afficher_mots_de_passe_enregistres():
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees_cryptees = json.load(fichier)
            if donnees_cryptees:
                donnees = (donnees_cryptees)
                message = "Mots de passe enregistrés :\n"
                for utilisateur, mdp in donnees.items():
                    message += f"{utilisateur}: {mdp}\n"
                CTkMessagebox.showinfo("Mots de passe enregistrés", message)
            else:
                CTkMessagebox.showinfo("Aucun mot de passe enregistré", "Aucun mot de passe n'est actuellement enregistré.")
    except FileNotFoundError:
        CTkMessagebox.showinfo("Aucun mot de passe enregistré", "Aucun mot de passe n'est actuellement enregistré.")

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title('Gestionnaire de mots de passe')
root.iconbitmap()
root.geometry('600x450')

label = customtkinter.CTkLabel(root, text="Bienvenue, j'espère que vous passez une bonne journée !", font=("Helvetica", 14))
label.pack(pady=10)

label_nom_utilisateur = customtkinter.CTkLabel(root, text="Nom d'utilisateur :", font=("Arial", 18)) 
label_nom_utilisateur.pack(pady=10)

entry_nom_utilisateur = customtkinter.CTkEntry(root)
entry_nom_utilisateur.pack(pady=10)

label_mot_de_passe = customtkinter.CTkLabel(root, text="Mot de passe :", font=("Arial", 18)) 
label_mot_de_passe.pack(pady=10)

entry_mot_de_passe = customtkinter.CTkEntry(root)
entry_mot_de_passe.pack(pady=10)

button_valider = customtkinter.CTkButton(root, text="Valider", command=valider_mot_de_passe, fg_color="#EEA2AD", font=("Arial", 16))  
button_valider.pack(pady=25)

button_generer_mot_de_passe = customtkinter.CTkButton(root, text="Générer un mot de passe aléatoire", command=generer_mot_de_passe_aleatoire_et_afficher, fg_color="#EEA2AD", font=("Arial", 14))  
button_generer_mot_de_passe.pack(pady=25)

button_afficher_mots_de_passe = customtkinter.CTkButton(root, text="Afficher les mots de passe enregistrés", command=afficher_mots_de_passe_enregistres, fg_color="#EEA2AD", font=("Arial", 14)) 
button_afficher_mots_de_passe.pack(pady=5)

root.mainloop()