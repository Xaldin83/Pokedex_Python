import tkinter as tk
from tkinter import messagebox
import fonctions_ajouts
import os


def return_page():
    fenetre.destroy()
    os.system("python ../Pokedex/main.py")

fenetre = tk.Tk()

def ajout():
    nm = name.get()
    verification = True
    with open('index.py', 'r', encoding='utf-8') as f:
        lignes = f.readlines()  # Retourne une liste

    for ligne in lignes:
        if(nm in ligne):
            verification=False
    if(verification):
        nb = int(number.get())
        stat = [int(pv.get()),int(attack.get()),int(defense.get()),int(special_attack.get()),int(special_defense.get()),int(speed.get())]
        t1 = type1.get()
        t2 = type2.get()
        if (t2==""):
            t2=None
        s1 = skill1.get()
        s2 = skill2.get()
        s3 = skil31.get()
        if (s3==""):
            s3=None
        h = height.get()
        w = weight.get()
        generation = listbox.get(listbox.curselection())
        c = capacity.get()
        fonctions_ajouts.ajout_index(nm,nb,generation)
        fonctions_ajouts.ajout_pkm(nm,nb,stat,t1,t2,s1,s2,s3,h,w,generation,c)
        messagebox.showinfo("Information", "Pokémon rajouté.")
    else:
        messagebox.showinfo("Information", "Pokémon déjà disponible.")

title = tk.Label(fenetre,text="Rajouter un Pokémon")
title.pack()


name_label = tk.Label(fenetre,text="Nom")
name_label.pack()
name = tk.Entry(fenetre)
name.pack()

number_label = tk.Label(fenetre,text="Numéro Pokédex")
number_label.pack()
number = tk.Entry(fenetre)
number.pack()

listbox = tk.Listbox(fenetre)
listbox.pack()

#Ajout d'éléments à la liste déroulante
listbox.insert(tk.END, "G1")
listbox.insert(tk.END, "G2")
listbox.insert(tk.END, "G3")
listbox.insert(tk.END, "G4")
listbox.insert(tk.END, "G5")
listbox.insert(tk.END, "G6")
listbox.insert(tk.END, "G7")
listbox.insert(tk.END, "G8")
listbox.insert(tk.END, "G9")
listbox.insert(tk.END, "Gigamax")
listbox.insert(tk.END, "Mega")
listbox.insert(tk.END, "Formes")

stat_label = tk.Label(fenetre,text="PV | ATK | DEF | ATK_S | DEF_S | VIT")
stat_label.pack()
pv = tk.Entry(fenetre)
attack = tk.Entry(fenetre)
defense = tk.Entry(fenetre)
special_attack = tk.Entry(fenetre)
special_defense = tk.Entry(fenetre)
speed = tk.Entry(fenetre)
pv.pack()
attack.pack()
defense.pack()
special_attack.pack()
special_defense.pack()
speed.pack()

type_label = tk.Label(fenetre,text="Type(s) du pokémon")
type_label.pack()
type1 = tk.Entry(fenetre)
type2 = tk.Entry(fenetre)
type1.pack()
type2.pack()

skills_label = tk.Label(fenetre,text="Talent(s) du pokémon")
skills_label.pack()
skill1 = tk.Entry(fenetre)
skill2 = tk.Entry(fenetre)
skil31 = tk.Entry(fenetre)

skill1.pack()
skill2.pack()
skil31.pack()

height_weight_label = tk.Label(fenetre,text="Taille et poids du pokémon")
height_weight_label.pack()
height = tk.Entry(fenetre)
weight = tk.Entry(fenetre)
height.pack()
weight.pack()

capacity_label = tk.Label(fenetre,text="Attaques du pokémon")
capacity_label.pack()
capacity = tk.Entry(fenetre)
capacity.pack()

button = tk.Button(fenetre,text="Ajouter",command=ajout)
button.pack()

button_return = tk.Button(fenetre,text="Retour",command=return_page)
button_return.pack()

fenetre.title("Rajout")
fenetre.geometry("1024x768")
fenetre.mainloop()
