from Classes import Classe_Pokemon
from BDD.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def return_page():
    fenetre.destroy()
    os.system("python ../Pokedex/main.py")

liste_attaque = [Griffe,Rugissement, Flammeche, Brouillard, Draco_Souffle, Crocs_Feu, Tranche, Lance_Flamme, Grimace, Danse_Flammes, Feu_dEnfer,Boutefeu,Charge,Draco_Charge]
Pokemon = Classe_Pokemon.Pokemon("Reptincel",5,[58, 64, 58, 80, 65, 80],liste_attaque,"./Pokémon_img/G1/Reptincel.png","Feu","None","Brasier","Force Soleil","None",1.1,19)

fenetre = tk.Tk()

name = tk.Label(fenetre, text=Pokemon.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Pokemon.img))
Label_image = tk.Label(fenetre,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type1}.png"))
Label_type1 = tk.Label(fenetre,image=type1)
Label_type1.grid(row=1,column=0)



Label_skill=tk.Label(fenetre, text=f"Talents:\n{Pokemon.skill1} | {Pokemon.skill2}")
Label_skill.grid(row=2,column=0)

Label_height_weight = tk.Label(fenetre, text=f"Taille : {Pokemon.height}m\nPoids : {Pokemon.weight}kg")
Label_height_weight.grid(row=3,column=0)


listbox_capacity = tk.Listbox(fenetre,width=50)
listbox_capacity.grid(row=4, column=0, columnspan=2)
Pokemon.list_capacity(listbox_capacity)

listbox_stat = tk.Listbox(fenetre,width=50)
listbox_stat.grid(row=4, column=2, columnspan=2)
Pokemon.list_stat(listbox_stat)


button_return = tk.Button(fenetre,text="Retour",command=return_page)
button_return.grid(row=5, column=0, columnspan=4)


fenetre.title("Reptincel")
fenetre.geometry("1024x768")
fenetre.mainloop()

