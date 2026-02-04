import tkinter as tk
from tkinter import messagebox, ttk
import fonctions_ajouts
import os


def return_page():
    screen.destroy()
    os.system("python ../Pokedex/main.py")

screen = tk.Tk()

def modif():
    try:
        nm = name.get()
        verification = True
        with open('index.txt', 'r', encoding='utf-8') as f:
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
            if(os.path.exists(f"./Pokémon_img/{generation}/{nm}.png")):
                c = capacity.get()
                fonctions_ajouts.modif_pkm(nm,nb,stat,t1,t2,s1,s2,s3,h,w,generation,c)
                messagebox.showinfo("Information", "Pokémon Ajouté.")
            else:
                messagebox.showinfo("Information", "Chemin d'image non valide.\nLa génération ou le nom ne correspond pas.")
        else:
            messagebox.showinfo("Information", "Page déjà existante..")
    except ValueError:
        messagebox.showinfo("Information", "Certaines informations sont érronés ou vide.")
    except tk.TclError:
        messagebox.showinfo("Information","Le type ou la génération n'est pas déterminé.")

title = tk.Label(screen,text="Ajouter un Pokémon")
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
dossier=os.listdir('./Pokémon_img')

for i in dossier[1:]:
    listbox.insert(tk.END, f"{i}")


stat_label = tk.Label(screen,text="HP | ATK | DEF | ATK_S | DEF_S | VIT")
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

type1 = ttk.Combobox(screen)
type2 = ttk.Combobox(screen)
type1.pack()
type2.pack()

type1['values']=('Acier', 'Combat', 'Dragon', 'Eau', 'Electrik', 'Fée', 'Feu', 'Glace', 'Insecte', 'Normal', 'Plante', 'Poison', 'Psy', 'Roche', 'Sol', 'Spectre', 'Ténèbres', 'Vol')
type2['values']=('Acier', 'Combat', 'Dragon', 'Eau', 'Electrik', 'Fée', 'Feu', 'Glace', 'Insecte', 'Normal', 'Plante', 'Poison', 'Psy', 'Roche', 'Sol', 'Spectre', 'Ténèbres', 'Vol',None)


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
