import tkinter.ttk as ttk
import tkinter

app = tkinter.Tk()
app.geometry("400x350")

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
