from Classes import Classe_Pokemon
from BDD.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def return_page():
    screen.destroy()
    os.system("python ../Pokedex/main.py")

list_capacity = [Croissance, Feuille_Magik, Vampigraine, Synthese,Doux_Parfum,Calinerie, Soucigraine, Champ_Herbu, Eco_Sphere,Doux_Baiser, Voeu_Soin,Fulmigraine]
Pokemon = Classe_Pokemon.Pokemon("Shaymin",492,[100, 100, 100, 100, 100, 100],list_capacity,"./Pokémon_img/G4/Shaymin.png","Plante","None","Médic Nature","","None",0.2,2.1)

screen = tk.Tk()

name = tk.Label(screen, text=Pokemon.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Pokemon.img))
Label_image = tk.Label(screen,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type1}.png"))
Label_type1 = tk.Label(screen,image=type1)
Label_type1.grid(row=1,column=0)



Label_skill=tk.Label(screen, text=f"Talents:\n{Pokemon.skill1}")
Label_skill.grid(row=2,column=0)

Label_height_weight = tk.Label(screen, text=f"Taille : {Pokemon.height}m\nPoids : {Pokemon.weight}kg")
Label_height_weight.grid(row=3,column=0)


listbox_capacity = tk.Listbox(screen,width=50)
listbox_capacity.grid(row=4, column=0, columnspan=2)
Pokemon.list_capacity(listbox_capacity)

listbox_stat = tk.Listbox(screen,width=50)
listbox_stat.grid(row=4, column=2, columnspan=2)
Pokemon.list_stat(listbox_stat)


button_return = tk.Button(screen,text="Retour",command=return_page)
button_return.grid(row=5, column=0, columnspan=4)


screen.title("Shaymin")
screen.geometry("1024x768")
screen.mainloop()

