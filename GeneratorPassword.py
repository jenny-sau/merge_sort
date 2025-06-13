import re
import secrets
import string
from tkinter.ttk import Combobox


def generate_password(length, nums, special_chars, uppercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]')
        ]

        # Check constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break

    return password

def copier_mot_de_passe():
    mot_de_passe = result_label.cget("text")  # Récupère le texte affiché
    if "Mot de passe" in mot_de_passe:
        mot_de_passe = mot_de_passe.replace("Mot de passe : ", "")  # Nettoie le texte
    fenetre.clipboard_clear()  # Vide le presse-papier
    fenetre.clipboard_append(mot_de_passe)  # Ajoute le mot de passe
    fenetre.update()  # Nécessaire pour certains systèmes

import tkinter as tk
from tkinter import ttk

#couleur = 7d4f50, f9eae1, cc8b86

fenetre = tk.Tk()
fenetre.configure(bg='#f9eae1')
fenetre.title("Generator Password")
fenetre.geometry("700x700")

#Titre
frame_titre = tk.Frame(fenetre)
frame_titre.pack(pady=20
                 )
label= tk.Label(frame_titre, text="Generator Password",  font=("Arial", 40),  fg="#f9eae1", bg='#7d4f50')
label.pack()

#Instruction + liste déroulante
#Longueur:
frame_contenu=tk.Frame(fenetre, bg='#f9eae1')
frame_contenu.pack(pady=20)

selected_length= tk.StringVar()
label_length= tk.Label(frame_contenu, text="longueur total du mot de passe",  font=("Arial", 10),  fg="#f9eae1", bg='#7d4f50')
label_length.grid(row=1, column=0, pady=10)
options_length = list (range(5, 13))
combo = ttk.Combobox(frame_contenu, values=options_length, textvariable=selected_length)
combo.current(3)
combo.grid(row=1, column=2)


#Chiffre:
selected_nums= tk.StringVar()
label_nums= tk.Label(frame_contenu, text="Nombre de chiffre",  font=("Arial", 10),  fg="#f9eae1", bg='#7d4f50')
label_nums.grid(row=2, column=0, pady=10)
options_nums = list (range(1, 3))
combo = ttk.Combobox(frame_contenu, values=options_nums, textvariable=selected_nums)
combo.current(1)
combo.grid(row=2, column=2)


#Majuscule:
selected_uppercase= tk.StringVar()
label_uppercase= tk.Label(frame_contenu, text="Nombre de majuscule",  font=("Arial", 10),  fg="#f9eae1", bg='#7d4f50')
label_uppercase.grid(row=3, column=0, pady=10)
options_uppercase = list (range(1, 3))
combo = ttk.Combobox(frame_contenu, values=options_uppercase, textvariable=selected_uppercase)
combo.current(0)
combo.grid(row=3, column=2)

#Caractère spéciaux:
selected_special_chars= tk.StringVar()
label_special_chars= tk.Label(frame_contenu, text="Nombre de caractere spéciaux",  font=("Arial", 10),  fg="#f9eae1", bg='#7d4f50')
label_special_chars.grid(row=4, column=0, pady=10)
options_special_chars = list (range(1, 3))
combo = ttk.Combobox(frame_contenu, values=options_special_chars, textvariable=selected_special_chars)
combo.current(1)
combo.grid(row=4, column=2)

#Générer mot de passe
frame_mdp= tk.Frame(fenetre, bg='#cc8b86')
frame_mdp.pack(fill=tk.X)

button = tk.Button(frame_mdp, text="Générer mot de passe",     command=lambda: result_label.config(
    text=generate_password(
        int(selected_length.get()),
        int(selected_nums.get()),
        int(selected_special_chars.get()),
        int(selected_uppercase.get()))
    ), font=("Arial", 15),  fg="#f9eae1", bg='#7d4f50')
button.pack(pady=20)

result_label = tk.Label(frame_mdp, text="Votre mot de passe s'affichera ici.", font=("Arial", 12), fg="#cc8b86")
result_label.pack(pady=10)

btn_copier = tk.Button(
    frame_mdp,
    text="Copier le mot de passe",
    command=copier_mot_de_passe,
    font=("Arial", 12),
    fg="#f9eae1",
    bg='#7d4f50'
)
btn_copier.pack(pady=10)

fenetre.mainloop()