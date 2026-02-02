import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os


def refound():
    pokemon = listbox_pokemon.get(listbox_pokemon.curselection())
    fenetre.destroy()
    os.system(f"python ../Pokedex/Pages/{pokemon}.py")

def quitter():
    fenetre.quit()

fenetre = tk.Tk()

title = tk.Label(fenetre,text="Bienvenue\nChoisissez le pokémon que vous voulez consulter.")
title.pack()

listbox_pokemon = tk.Listbox(fenetre,width=50)
listbox_pokemon.pack()

listbox_pokemon.insert(tk.END, "Bulbizarre")

button_search = tk.Button(fenetre,text="Rechercher",command=refound)
button_search.pack()

button_quit = tk.Button(fenetre, text="Quitter",command=quitter)
button_quit.pack()

fenetre.geometry("1024x768")
fenetre.mainloop()
