import tkinter as tk
import os


def index():
    with open('index.txt', 'r') as f:
        lignes = f.readlines()  # Retourne une liste

    for ligne in lignes:
        listbox_pokemon.insert(tk.END, ligne)

def refound():
    pokemon = listbox_pokemon.get(listbox_pokemon.curselection())
    print(pokemon)
    if(pokemon[-1]=="\n"):
       pokemon=pokemon[:-1]
    fenetre.destroy()
    os.system(f"python ../Pokedex/Pages/{pokemon}.py")

def ajout():
    fenetre.destroy()
    os.system(f"python ./rajout.py")

def quitter():
    fenetre.quit()

fenetre = tk.Tk()

title = tk.Label(fenetre,text="Bienvenue\nChoisissez le pokémon que vous voulez consulter.")
title.pack()

listbox_pokemon = tk.Listbox(fenetre,width=50)
listbox_pokemon.pack()

index()

button_search = tk.Button(fenetre,text="Afficher",command=refound)
button_search.pack()
button_search = tk.Button(fenetre,text="Ajouter",command=ajout)
button_search.pack()

button_quit = tk.Button(fenetre, text="Quitter",command=quitter)
button_quit.pack()


fenetre.title("Main")
fenetre.geometry("1024x768")
fenetre.mainloop()
