
import tkinter as tk  # Importation du module Tkinter pour créer une interface graphique
from tkinter import messagebox  # Importation de la boîte de dialogue messagebox

import tkinter.ttk as ttk
import tkinter

import tkinter.ttk as ttk
import tkinter

app = tkinter.Tk()
app.geometry("400x350")


import hashlib  # Module pour le hachage sécurisé des mots de passe
import json  # Module pour manipuler des données au format JSON
import random  # Module pour générer des nombres aléatoires
import string  # Module pour manipuler des chaînes de caractères

# Fonction pour vérifier la sécurité d'un mot de passe
def est_mot_de_passe_securise(mot_de_passe):
    return (
        len(mot_de_passe) >= 8 and
        any(char.isupper() for char in mot_de_passe) and
        any(char.islower() for char in mot_de_passe) and
        any(char.isdigit() for char in mot_de_passe) and
        any(char in "!@#$%^&*" for char in mot_de_passe)
    )

# Fonction pour hacher un mot de passe
def hacher_mot_de_passe(mot_de_passe):
    mot_de_passe_hache = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return mot_de_passe_hache

# Fonction pour crypter un mot de passe
def crypter_mot_de_passe(mot_de_passe):
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

# Fonction pour sauvegarder un nom d'utilisateur et son mot de passe dans un fichier JSON
def sauvegarder_mot_de_passe(nom_utilisateur, mot_de_passe):
    donnees = {}
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        pass

    if nom_utilisateur in donnees:
        messagebo.showerror("Erreur", "Ce nom d'utilisateur existe déjà. Choisissez un autre nom.")
    else:
        mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
        donnees[nom_utilisateur] = mot_de_passe_crypte
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(donnees, fichier)
        messagebox.showinfo("Succès", "Mot de passe enregistré avec succès.")

# Fonction pour générer un mot de passe aléatoire
def generer_mot_de_passe_aleatoire():
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(12))
    return mot_de_passe

# Fonction pour valider le mot de passe saisi par l'utilisateur et sauvegarder s'il est sécurisé
def valider_mot_de_passe():
    mot_de_passe = entry_mot_de_passe.get()
    if est_mot_de_passe_securise(mot_de_passe):
        sauvegarder_mot_de_passe(entry_nom_utilisateur.get(), mot_de_passe)
        root.destroy()  # Fermer la fenêtre après avoir sauvegardé le mot de passe
    else:
        messagebox.showerror("Erreur", "Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")


# Fonction pour sauvegarder un nom d'utilisateur et son mot de passe dans un fichier JSON
def sauvegarder_mot_de_passe(nom_utilisateur, mot_de_passe):
    donnees = {}
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        pass

    if any(mdp == mot_de_passe for mdp in donnees.values()):
        messagebox.showerror("Erreur", "Ce mot de passe est déjà enregistré.")
    else:
        mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
        donnees[nom_utilisateur] = mot_de_passe_crypte
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(donnees, fichier)
        messagebox.showinfo("Succès", "Mot de passe enregistré avec succès.")


# Fonction pour générer un mot de passe aléatoire et l'afficher dans l'entrée de texte
def generer_mot_de_passe_aleatoire_et_afficher():
    mot_de_passe_aleatoire = generer_mot_de_passe_aleatoire()
    entry_mot_de_passe.delete(0, tk.END)
    entry_mot_de_passe.insert(0, mot_de_passe_aleatoire)

# Fonction pour décrypter les mots de passe à partir du fichier JSON
def decrypter_mots_de_passe(donnees_cryptees):
    return {utilisateur: mot_de_passe for utilisateur, mot_de_passe in donnees_cryptees.items()}

# Fonction pour afficher les mots de passe enregistrés
def afficher_mots_de_passe_enregistres():
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees_cryptees = json.load(fichier)
            if donnees_cryptees:
                donnees = decrypter_mots_de_passe(donnees_cryptees)
                message = "Mots de passe enregistrés:\n"
                for utilisateur, mdp in donnees.items():
                    message += f"{utilisateur}: {mdp}\n"
                    
                messagebox.showinfo("Mots de passe enregistrés", message)
            else:
                messagebox.showinfo("Aucun mot de passe enregistré", "Aucun mot de passe n'est actuellement enregistré.")
    except FileNotFoundError:
        messagebox.showinfo("Aucun mot de passe enregistré", "Aucun mot de passe n'est actuellement enregistré.")

def button_function():
    print("button pressed")

s = ttk.Style()
s.configure("TRadiobutton", fg="red")

y_padding = 6

frame_1 = tkinter.Frame(master=app, width=300, height=260, bg="lightgray")
frame_1.pack(padx=60, pady=20, fill="both", expand=True)

# Label
label_1 = tkinter.Label(master=frame_1, text="Nom d'utilisateur", bg="lightgray")
label_1.pack(pady=y_padding, padx=10)
entry_1 = tkinter.Entry(master=frame_1, highlightbackground="lightgray", width=40)
entry_1.pack(pady=y_padding, padx=10)

# Label
label_2 = tkinter.Label(master=frame_1, text="Mot de passe", bg="lightgray")
label_2.pack(pady=y_padding, padx=10)
entry_2 = tkinter.Entry(master=frame_1, highlightbackground="lightgray", width=40)
entry_2.pack(pady=y_padding, padx=10)

button_1 = tkinter.Button(master=frame_1, command=button_function, text="Valide", highlightbackground="lightgray")
button_1.pack(pady=y_padding, padx=10)


button_2 = tkinter.Button(master=frame_1, command=button_function, text="Générer un mot de passe", highlightbackground="lightgray")
button_2.pack(pady=y_padding, padx=10)

button_3 = tkinter.Button(master=frame_1, command=button_function, text="Afficher les mots de passe enregistrer", highlightbackground="lightgray")
button_3.pack(pady=y_padding, padx=10)


app.mainloop()