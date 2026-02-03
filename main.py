import tkinter as tk
import os
import index


def research():
    generation = champ_search.get()
    index.pokedex.affichage_generation(generation, listbox_pokemon)

def refound():
    pokemon = listbox_pokemon.get(listbox_pokemon.curselection())
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

index.pokedex.affichage_general(listbox_pokemon)

button_display = tk.Button(fenetre,text="Afficher",command=refound)
button_display.pack()
button_add= tk.Button(fenetre,text="Ajouter",command=ajout)
button_add.pack()

champ_search = tk.Entry(fenetre)
champ_search.pack()
button_search= tk.Button(fenetre,text="Rechercher",command=research)
button_search.pack()


button_quit = tk.Button(fenetre, text="Quitter",command=quitter)
button_quit.pack()


fenetre.title("Main")
fenetre.geometry("1024x768")
fenetre.mainloop()
