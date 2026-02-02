from Classes import Classe_Pokemon
from BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os

def return_page():
    fenetre.destroy()
    os.system("python ../Pokedex/main.py")

liste_attaque = [Charge,Rugissement,Fouet_Lianes,Croissance,Vampigraine,TranchHerbe,Poudre_Dodo,Poudre_Toxik,Canon_Graine,Belier,Doux_Parfum,Synthese,Soucigraine,Megafouet,Lance_Soleil,Feuille_Magik,Amnesie,Cradovague,Damocles]
Bulbizarre = Classe_Pokemon.Pokemon("Bulbizarre",1,[45,49,49,65,65,45],liste_attaque,"./Pokémon_img/G1/Bulbizarre.png","Plante","Poison")

fenetre = tk.Tk()

name = tk.Label(fenetre, text=Bulbizarre.name,font=("Arial",41))
name.grid(row=0,column=0)

image=ImageTk.PhotoImage(Image.open(Bulbizarre.img))
Label_image = tk.Label(fenetre,image=image)
Label_image.grid(row = 0,column=3,rowspan=4)

type1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Bulbizarre.type1}.png"))
Label_type1 = tk.Label(fenetre,image=type1)
Label_type1.grid(row=1,column=0)
type2 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Bulbizarre.type2}.png"))
Label_type2 = tk.Label(fenetre,image=type2)
Label_type2.grid(row=1,column=1)

listbox_capacity = tk.Listbox(fenetre,width=50)
listbox_capacity.grid(row=4, column=0, columnspan=2)
Bulbizarre.list_capacity(listbox_capacity)

listbox_stat = tk.Listbox(fenetre,width=50)
listbox_stat.grid(row=4, column=2, columnspan=2)
Bulbizarre.list_stat(listbox_stat)


button_return = tk.Button(fenetre,text="Retour",command=return_page)
button_return.grid(row=5, column=0)

fenetre.geometry("1024x768")
fenetre.mainloop()

