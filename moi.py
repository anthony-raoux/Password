import tkinter as tk  # Importation du module Tkinter pour créer une interface graphique
from tkinter import messagebox  # Importation de la boîte de dialogue messagebox
import hashlib  # Module pour le hachage sécurisé des mots de passe
import json  # Module pour manipuler des données au format JSON
import random  # Module pour générer des nombres aléatoires
import string  # Module pour manipuler des chaînes de caractères

def est_mot_de_passe_securise(mot_de_passe):
    """
    Fonction pour vérifier la sécurité d'un mot de passe.
    Elle retourne True si le mot de passe est sécurisé selon les critères spécifiés.
    """
    return (
        len(mot_de_passe) >= 8 and  # Le mot de passe doit avoir au moins 8 caractères
        any(char.isupper() for char in mot_de_passe) and  # Au moins une lettre majuscule
        any(char.islower() for char in mot_de_passe) and  # Au moins une lettre minuscule
        any(char.isdigit() for char in mot_de_passe) and  # Au moins un chiffre
        any(char in "!@#$%^&*" for char in mot_de_passe)  # Au moins un caractère spécial
    )

def crypter_mot_de_passe(mot_de_passe):
    """
    Fonction pour crypter un mot de passe en utilisant l'algorithme de hachage SHA-256.
    """
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()

def sauvegarder_mot_de_passe(nom_utilisateur, mot_de_passe):
    """
    Fonction pour sauvegarder un nom d'utilisateur et son mot de passe dans un fichier JSON.
    """
    donnees = {}
    try:
        with open('mots_de_passe.json', 'r') as fichier:
            donnees = json.load(fichier)
    except FileNotFoundError:
        pass
    if nom_utilisateur in donnees:
        messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà. Choisissez un autre nom.")
    else:
        mot_de_passe_crypte = crypter_mot_de_passe(mot_de_passe)
        donnees[nom_utilisateur] = mot_de_passe_crypte
        with open('mots_de_passe.json', 'w') as fichier:
            json.dump(donnees, fichier)
        messagebox.showinfo("Succès", "Mot de passe enregistré avec succès.")

def generer_mot_de_passe_aleatoire():
    """
    Fonction pour générer un mot de passe aléatoire.
    """
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*"
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(12))
    return mot_de_passe

def valider_mot_de_passe():
    """
    Fonction pour valider le mot de passe saisi par l'utilisateur et le sauvegarder s'il est sécurisé.
    """
    mot_de_passe = entry_mot_de_passe.get()
    if est_mot_de_passe_securise(mot_de_passe):
        sauvegarder_mot_de_passe(entry_nom_utilisateur.get(), mot_de_passe)
        root.destroy()  # Fermer la fenêtre après avoir sauvegardé le mot de passe
    else:
        messagebox.showerror("Erreur", "Le mot de passe ne respecte pas les exigences de sécurité. Veuillez réessayer.")

root = tk.Tk()  # Création de la fenêtre principale de l'interface graphique
root.geometry("500x500")  # Définition de la taille de la fenêtre
root.title("Gestionnaire de mots de passe")  # Définition du titre de la fenêtre

label_nom_utilisateur = tk.Label(root, text="Nom d'utilisateur:")  # Création de l'étiquette pour le nom d'utilisateur
label_nom_utilisateur.pack()  # Affichage de l'étiquette

entry_nom_utilisateur = tk.Entry(root)  # Création du champ d'entrée pour le nom d'utilisateur
entry_nom_utilisateur.pack()  # Affichage du champ d'entrée

label_mot_de_passe = tk.Label(root, text="Mot de passe:")  # Création de l'étiquette pour le mot de passe
label_mot_de_passe.pack()  # Affichage de l'étiquette

entry_mot_de_passe = tk.Entry(root, show="*")  # Création du champ d'entrée pour le mot de passe avec masquage des caractères
entry_mot_de_passe.pack()  # Affichage du champ d'entrée

button_valider = tk.Button(root, text="Valider", command=valider_mot_de_passe)  # Création du bouton Valider
button_valider.pack()  # Affichage du bouton Valider

button_generer_mot_de_passe = tk.Button(root, text="Générer un mot de passe aléatoire", command=generer_mot_de_passe_aleatoire)  # Création du bouton pour générer un mot de passe aléatoire
button_generer_mot_de_passe.pack()  # Affichage du bouton pour générer un mot de passe aléatoire

button_afficher_mots_de_passe = tk.Button(root, text="Afficher les mots de passe enregistrés", command="afficher_mots_de_passe_enregistres")  # Création du bouton pour afficher les mots de passe enregistrés
button_afficher_mots_de_passe.pack()  # Affichage du bouton pour afficher les mots de passe enregistrés

root.mainloop()  # Boucle principale pour maintenir l'interface graphique en cours d'exécution
