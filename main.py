import tkinter as tk
import os
import index


def research():
    generation = field_search.get()
    if(generation == ""):
        index.pokedex.affichage_general(listbox_pokemon)
    else:
        index.pokedex.affichage_generation(generation, listbox_pokemon)

def refound():
    pokemon = listbox_pokemon.get(listbox_pokemon.curselection())
    if(pokemon[-1]=="\n"):
       pokemon=pokemon[:-1]
    screen.destroy()
    os.system(f"""python "../Pokedex/Pages/{pokemon}.py"\n""")

def ajout():
    screen.destroy()
    os.system(f"python ./rajout.py")

def quitter():
    screen.quit()

screen = tk.Tk()

title = tk.Label(screen,text="Bienvenue\nChoisissez le pokémon que vous voulez consulter.")
title.pack()

listbox_pokemon = tk.Listbox(screen,width=50)
listbox_pokemon.pack()

index.pokedex.affichage_general(listbox_pokemon)

button_display = tk.Button(screen,text="Afficher",command=refound)
button_display.pack()
button_add= tk.Button(screen,text="Ajouter",command=ajout)
button_add.pack()


search = tk.Label(screen,text="Ecrivez la génération que vous cherchez.")
search.pack()
field_search = tk.Entry(screen)
field_search.pack()
button_search= tk.Button(screen,text="Rechercher",command=research)
button_search.pack()


button_quit = tk.Button(screen, text="Quitter",command=quitter)
button_quit.pack()


screen.title("Main")
screen.geometry("1024x768")
screen.mainloop()
