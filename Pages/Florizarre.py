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

list_capacity = [Tempete_Florale, Danse_Fleurs,Charge,Rugissement,Fouet_Lianes,Croissance,Vampigraine,TranchHerbe,Poudre_Dodo,Poudre_Toxik,Canon_Graine,Belier,Doux_Parfum,Synthese,Soucigraine,Megafouet,Lance_Soleil,Feuille_Magik,Amnesie,Cradovague,Damocles]
Florizarre = Classe_Pokemon.Pokemon("Florizarre",3,[80, 82, 83, 100, 100, 80],list_capacity,"./Pokémon_img/G1/Florizarre.png","Plante","Poison","Engrais","Chlorophylle","None",2,100)

screen = tk.Tk()

name = tk.Label(screen, text=Florizarre.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Florizarre.img))
Label_image = tk.Label(screen,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Florizarre.type1}.png"))
Label_type1 = tk.Label(screen,image=type1)
Label_type1.grid(row=1,column=0)
type2 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Florizarre.type2}.png"))
Label_type2 = tk.Label(screen,image=type2)
Label_type2.grid(row=1,column=1)


Label_skill=tk.Label( screen, text=f"Talents:\n{Florizarre.skill1} | {Florizarre.skill2}")
Label_skill.grid(row=2,column=0)

Label_height_weight = tk.Label(screen, text=f"Taille : {Florizarre.height}m\nPoids : {Florizarre.weight}kg")
Label_height_weight.grid(row=3,column=0)


listbox_capacity = tk.Listbox(screen,width=50)
listbox_capacity.grid(row=4, column=0, columnspan=2)
Florizarre.list_capacity(listbox_capacity)

listbox_stat = tk.Listbox(screen,width=50)
listbox_stat.grid(row=4, column=2, columnspan=2)
Florizarre.list_stat(listbox_stat)


button_return = tk.Button(screen,text="Retour",command=return_page)
button_return.grid(row=5, column=0)
button_modification = tk.Button(screen, text="Modifier", command=modif)
button_modification.grid(row=5, column=1)


screen.title("Florizarre")
screen.geometry("1024x768")
screen.mainloop()

