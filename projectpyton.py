# Toi la tu me fait honte , "pyton" comment ? 😂😂
import json
import os
import tkinter as tk
from tkinter import ttk

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "livres.json")
livres = []

def ajouter_livre():
    titre = entry_titre.get()
    auteur = entry_auteur.get()
    genre = entry_genre.get()
    isbn = entry_isbn.get()
    if titre and auteur and genre and isbn:
        livre = {
            "titre": titre,
            "auteur": auteur,
            "genre": genre,
            "isbn": isbn
        }
        livres.append(livre)
        liste_livres.insert(tk.END, f"{titre} - {auteur}")
        entry_titre.delete(0, tk.END)
        entry_auteur.delete(0, tk.END)
        entry_genre.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)
        sauvegarder_livres()

def supprimer_livre():
    selection = liste_livres.curselection()
    if selection:
        index = selection[0]
        liste_livres.delete(index)
        if index < len(livres):
            livres.pop(index)
            sauvegarder_livres()

def sauvegarder_livres():
    with open(json_path, "w") as file:
        json.dump(livres, file)

def rechercher_livre():
    recherche = entry_recherche.get().lower()
    liste_livres.delete(0, tk.END)
    for livre in livres:
        if recherche in livre["titre"].lower() or recherche in livre["auteur"].lower() or recherche in livre["isbn"].lower():
            liste_livres.insert(tk.END, f"{livre['titre']} - {livre['auteur']}")

fenetre = tk.Tk()
fenetre.title("GESTIONNAIRE DE BIBLIOTHEQUE")
fenetre.geometry("600x600")

style = ttk.Style()
style.configure("TButton", padding=(10, 5), font='Helvetica 10 bold')

frame_ajout = tk.Frame(fenetre)
frame_ajout.pack(pady=10)

placeholder_titre = tk.Label(frame_ajout, text="Titre du livre:")
placeholder_titre.grid(row=0, column=0, padx=10, pady=5)
entry_titre = tk.Entry(frame_ajout)
entry_titre.grid(row=0, column=1, padx=10, pady=5)

placeholder_auteur = tk.Label(frame_ajout, text="Auteur du livre:")
placeholder_auteur.grid(row=1, column=0, padx=10, pady=5)
entry_auteur = tk.Entry(frame_ajout)
entry_auteur.grid(row=1, column=1, padx=10, pady=5)

placeholder_genre = tk.Label(frame_ajout, text="Genre du livre:")
placeholder_genre.grid(row=2, column=0, padx=10, pady=5)
entry_genre = tk.Entry(frame_ajout)
entry_genre.grid(row=2, column=1, padx=10, pady=5)

placeholder_isbn = tk.Label(frame_ajout, text="ISBN du livre:")
placeholder_isbn.grid(row=3, column=0, padx=10, pady=5)
entry_isbn = tk.Entry(frame_ajout)
entry_isbn.grid(row=3, column=1, padx=10, pady=5)

bouton_ajout = ttk.Button(frame_ajout, text="Ajouter Livre", command=ajouter_livre)
bouton_ajout.grid(row=4, column=0, columnspan=2, pady=10)

frame_gestion = tk.Frame(fenetre)
frame_gestion.pack(pady=10)

liste_livres = tk.Listbox(frame_gestion, bg="#E0D8EE", width=50, height=10)
liste_livres.pack(pady=10)

bouton_supp = ttk.Button(frame_gestion, text="Supprimer Livre", command=supprimer_livre)
bouton_supp.pack(pady=5)

frame_recherche = tk.Frame(fenetre)
frame_recherche.pack(pady=10)

placeholder_recherche = tk.Label(frame_recherche, text="Rechercher Livre:")
placeholder_recherche.grid(row=0, column=0, padx=10, pady=5)
entry_recherche = tk.Entry(frame_recherche)
entry_recherche.grid(row=0, column=1, padx=10, pady=5)

bouton_recherche = ttk.Button(frame_recherche, text="Rechercher", command=rechercher_livre)
bouton_recherche.grid(row=0, column=2, padx=10, pady=5)

try:
    with open(json_path, "r") as file:
        livres = json.load(file)
        for livre in livres:
            liste_livres.insert(tk.END, f"{livre['titre']} - {livre['auteur']}")
except (FileNotFoundError, json.JSONDecodeError):
    pass

fenetre.mainloop()
