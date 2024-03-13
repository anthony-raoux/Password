from tkinter import *
import customtkinter

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

button_valider = customtkinter.CTkButton(root, text="Valider", command="", fg_color="#EEA2AD", font=("Arial", 16))  
button_valider.pack(pady=25)

button_generer_mot_de_passe = customtkinter.CTkButton(root, text="Générer un mot de passe aléatoire", command="", fg_color="#EEA2AD", font=("Arial", 14))  
button_generer_mot_de_passe.pack(pady=25)

button_afficher_mots_de_passe = customtkinter.CTkButton(root, text="Afficher les mots de passe enregistrés", command="", fg_color="#EEA2AD", font=("Arial", 14)) 
button_afficher_mots_de_passe.pack(pady=5)

root.mainloop()