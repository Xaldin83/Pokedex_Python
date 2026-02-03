from Classes import Classe_Pokemon
from BDD.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def screen_form():
    screen.destroy()
    os.system("python ./Pages/Shaymin.py")

def modif():
    screen.destroy()
    os.system("python ../Pokedex/modification.py")

def return_page():
    screen.destroy()
    os.system("python ../Pokedex/main.py")

list_capacity = [Croissance, Feuille_Magik, Vampigraine, Vive_Attaque,Doux_Parfum,Calinerie, Soucigraine, Lame_dAir, Eco_Sphere,Doux_Baiser, Tempete_Verte,Fulmigraine]
Pokemon = Classe_Pokemon.Pokemon("Shaymin",492,[100, 103,75,120,75,127],list_capacity,"./Pokémon_img/Formes/Shaymin (Forme Céleste).png","Plante","Vol","Sérénité","None","None",0.4,5.2)

screen = tk.Tk()

name = tk.Label(screen, text=Pokemon.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Pokemon.img))
Label_image = tk.Label(screen,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type1}.png"))
Label_type1 = tk.Label(screen,image=type1)
Label_type1.grid(row=1,column=0)
type2 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type2}.png"))
Label_type2 = tk.Label(screen,image=type2)
Label_type2.grid(row=1,column=1)



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
button_return.grid(row=5, column=0)

button_form = tk.Button(screen, text= "Afficher la forme Terrestre", command=screen_form)
button_form.grid(row=1,column=5)

button_modification = tk.Button(screen, text="Modifier", command=modif)
button_modification.grid(row=5, column=3)


screen.title("Shaymin")
screen.geometry("1024x768")
screen.mainloop()

