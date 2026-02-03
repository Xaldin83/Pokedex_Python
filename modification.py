import tkinter as tk
from tkinter import messagebox
import fonctions_ajouts
import os


def return_page():
    screen.destroy()
    os.system("python ../Pokedex/main.py")

screen = tk.Tk()

def modif():
    nm = name.get()
    verification = True
    with open('index.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # Retourne une liste

    for line in lines:
        if(nm in line):
            verification=False
    if(not verification):
        nb = int(number.get())
        stat = [int(hp.get()),int(attack.get()),int(defense.get()),int(special_attack.get()),int(special_defense.get()),int(speed.get())]
        t1 = type1.get()
        t2 = type2.get()
        if (t2==""):
            t2=None
        s1 = skill1.get()
        s2 = skill2.get()
        if (s2==""):
            s2=None
        s3 = skil31.get()
        if (s3==""):
            s3=None
        h = height.get()
        w = weight.get()
        generation = listbox.get(listbox.curselection())
        c = capacity.get()
        fonctions_ajouts.modif_pkm(nm,nb,stat,t1,t2,s1,s2,s3,h,w,generation,c)
        messagebox.showinfo("Information", "Pokémon modifié.")
    else:
        messagebox.showinfo("Information", "Page non existante.")

title = tk.Label(screen,text="Modifier un Pokémon")
title.pack()


name_label = tk.Label(screen,text="Nom")
name_label.pack()
name = tk.Entry(screen)
name.pack()

number_label = tk.Label(screen,text="Numéro Pokédex")
number_label.pack()
number = tk.Entry(screen)
number.pack()

listbox = tk.Listbox(screen)
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

stat_label = tk.Label(screen,text="hp | ATK | DEF | ATK_S | DEF_S | VIT")
stat_label.pack()
hp = tk.Entry(screen)
attack = tk.Entry(screen)
defense = tk.Entry(screen)
special_attack = tk.Entry(screen)
special_defense = tk.Entry(screen)
speed = tk.Entry(screen)
hp.pack()
attack.pack()
defense.pack()
special_attack.pack()
special_defense.pack()
speed.pack()

type_label = tk.Label(screen,text="Type(s) du pokémon")
type_label.pack()
type1 = tk.Entry(screen)
type2 = tk.Entry(screen)
type1.pack()
type2.pack()

skills_label = tk.Label(screen,text="Talent(s) du pokémon")
skills_label.pack()
skill1 = tk.Entry(screen)
skill2 = tk.Entry(screen)
skil31 = tk.Entry(screen)

skill1.pack()
skill2.pack()
skil31.pack()

height_weight_label = tk.Label(screen,text="Taille et poids du pokémon")
height_weight_label.pack()
height = tk.Entry(screen)
weight = tk.Entry(screen)
height.pack()
weight.pack()

capacity_label = tk.Label(screen,text="Attaques du pokémon")
capacity_label.pack()
capacity = tk.Entry(screen)
capacity.pack()

button = tk.Button(screen,text="Modifier",command=modif)
button.pack()

button_return = tk.Button(screen,text="Retour",command=return_page)
button_return.pack()

screen.title("Modification")
screen.geometry("1024x768")
screen.mainloop()
