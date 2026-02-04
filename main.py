import tkinter as tk
from tkinter import messagebox
import os
import index.index as index
from Fonctions import Global_page


def research():
    generation = field_search.get()
    if(generation == ""):
        index.pokedex.affichage_general(listbox_pokemon)
    else:
        index.pokedex.affichage_generation(generation, listbox_pokemon)

def refound():
    try:
        pokemon = listbox_pokemon.get(listbox_pokemon.curselection())
        if(pokemon[-1]=="\n"):
            pokemon=pokemon[:-1]
        screen.destroy()
        Global_page.main(pokemon)
    except tk.TclError:
        messagebox.showinfo("Erreur","Aucun pokémon sélectionné.")


def add():
    screen.destroy()
    os.system(f"python ./rajout.py")

def leave():
    screen.quit()

screen = tk.Tk()

title = tk.Label(screen,text="Bienvenue\nChoisissez le pokémon que vous voulez consulter.")
title.pack()

listbox_pokemon = tk.Listbox(screen,width=50)
listbox_pokemon.pack()

index.pokedex.affichage_general(listbox_pokemon)

button_display = tk.Button(screen,text="Afficher",command=refound)
button_display.pack()
button_add= tk.Button(screen,text="Ajouter",command=add)
button_add.pack()


search = tk.Label(screen,text="Ecrivez la génération que vous cherchez.")
search.pack()
field_search = tk.Entry(screen)
field_search.pack()
button_search= tk.Button(screen,text="Rechercher",command=research)
button_search.pack()


button_quit = tk.Button(screen, text="Quitter",command=leave)
button_quit.pack()


screen.title("Main")
screen.geometry("1024x768")
screen.mainloop()
