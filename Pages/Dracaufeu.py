from Classes import Classe_Pokemon
from BDD.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def modif():
    screen.destroy()
    os.system("python ../Pokedex/modification.py")

def return_page():
    screen.destroy()
    os.system("python ../Pokedex/main.py")


list_capacity = [Lame_dAir,Canicule,Draco_Griffe,Griffe,Rugissement, Flammeche, Brouillard, Draco_Souffle, Crocs_Feu, Tranche, Lance_Flamme, Grimace, Danse_Flammes, Feu_dEnfer,Boutefeu,Charge,Draco_Charge]
Pokemon = Classe_Pokemon.Pokemon("Dracaufeu",6,[78, 84, 78, 109, 85, 100],list_capacity,"./Pokémon_img/G1/Dracaufeu.png","Feu","Vol","Brasier","Force Soleil","None",1.7,90.5)

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


Label_skill=tk.Label(screen, text=f"Talents:\n{Pokemon.skill1} | {Pokemon.skill2}")
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
button_modification = tk.Button(screen, text="Modifier", command=modif)
button_modification.grid(row=5, column=1)


screen.title("Dracaufeu")
screen.geometry("1024x768")
screen.mainloop()

