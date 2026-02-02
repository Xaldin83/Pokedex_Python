from Classes import Classe_Pokemon
from BDD.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def return_page():
    fenetre.destroy()
    os.system("python ../Pokedex/main.py")

liste_attaque = []
Herbizarre = Classe_Pokemon.Pokemon("Herbizarre",2,[60, 62, 63, 80, 80, 60],liste_attaque,"./Pokémon_img/G1/Herbizarre.png","Plante","Poison","Engrais","Chlorophylle","None",1,13)

fenetre = tk.Tk()

name = tk.Label(fenetre, text=Herbizarre.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Herbizarre.img))
Label_image = tk.Label(fenetre,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Herbizarre.type1}.png"))
Label_type1 = tk.Label(fenetre,image=type1)
Label_type1.grid(row=1,column=0)
type2 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Herbizarre.type2}.png"))
Label_type2 = tk.Label(fenetre,image=type2)
Label_type2.grid(row=1,column=1)


Label_skill=tk.Label( fenetre, text=f"Talents:\n{Herbizarre.skill1} | {Herbizarre.skill2}")
Label_skill.grid(row=2,column=0)

Label_height_weight = tk.Label(fenetre, text=f"Taille : {Herbizarre.height}m\nPoids : {Herbizarre.weight}kg")
Label_height_weight.grid(row=3,column=0)


listbox_capacity = tk.Listbox(fenetre,width=50)
listbox_capacity.grid(row=4, column=0, columnspan=2)
Herbizarre.list_capacity(listbox_capacity)

listbox_stat = tk.Listbox(fenetre,width=50)
listbox_stat.grid(row=4, column=2, columnspan=2)
Herbizarre.list_stat(listbox_stat)


button_return = tk.Button(fenetre,text="Retour",command=return_page)
button_return.grid(row=5, column=0, columnspan=4)


fenetre.title()
fenetre.geometry("1024x768")
fenetre.mainloop()

