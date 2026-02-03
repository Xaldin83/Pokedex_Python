def ajout_index(name,number,generation):
    file=open(f"index.py","a",encoding='utf-8')
    file.write(f"""\npokedex.ajout("{name}",{number},"{generation}")""")
    file.close()
    file=open(f"index.txt","a",encoding='utf-8')
    file.write(f"""\n{name}""")
    file.close()


def ajout_pkm(name,number,stat,type1,type2,skill1,skill2,skill3,height,weight,generation,capacity):
    link = f"./Pokémon_img/{generation}/{name}.png"
    file=open(f"./Pages/{name}.py","a",encoding='utf-8')
    file.write(f"""from Classes import Classe_Pokemon\nfrom BDD.BDDAttaque import *\nimport tkinter as tk\nfrom PIL import ImageTk, Image\nimport os\n\ndef return_page():\n    screen.destroy()\n    os.system("python ../Pokedex/main.py")\n\nlist_capacity = [{capacity}]\nPokemon = Classe_Pokemon.Pokemon("{name}",{number},{stat},list_capacity,"{link}","{type1}","{type2}","{skill1}","{skill2}","{skill3}",{height},{weight})\n\nscreen = tk.Tk()\n\nname = tk.Label(screen, text=Pokemon.name,font=("Arial",41))\nname.grid(row=0,column=0)\n\nimage=ImageTk.PhotoImage(Image.open(Pokemon.img))\nLabel_image = tk.Label(screen,image=image)\nLabel_image.grid(row = 0,column=3,rowspan=4)\n\ntype1 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature""")
    file.write(""" {Pokemon.type1}.png"))\nLabel_type1 = tk.Label(screen,image=type1)\nLabel_type1.grid(row=1,column=0)\n""")
    if(type2!=None):
        file.write("""type2 = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type2}.png"))\nLabel_type2 = tk.Label(screen,image=type2)\nLabel_type2.grid(row=1,column=1)""")
    file.write("""\n\n\nLabel_skill=tk.Label(screen, text=f"Talents:\\n{Pokemon.skill1}""")
    
    if(skill2!=None):
        file.write(""" | {Pokemon.skill2}""")
    if(skill3!=None):
        file.write(""" | {Pokemon.skill3}""")
    file.write("""")\nLabel_skill.grid(row=2,column=0)\n\nLabel_height_weight = tk.Label(screen, text=f"Taille : {Pokemon.height}m\\nPoids : {Pokemon.weight}kg")\nLabel_height_weight.grid(row=3,column=0)\n\n\nlistbox_capacity = tk.Listbox(screen,width=50)\nlistbox_capacity.grid(row=4, column=0, columnspan=2)\nPokemon.list_capacity(listbox_capacity)\n\nlistbox_stat = tk.Listbox(screen,width=50)\nlistbox_stat.grid(row=4, column=2, columnspan=2)\nPokemon.list_stat(listbox_stat)\n\n\nbutton_return = tk.Button(screen,text="Retour",command=return_page)\nbutton_return.grid(row=5, column=0, columnspan=4)\n\n\n""")
    file.write(f"""screen.title("{name}")\nscreen.geometry("1024x768")\nscreen.mainloop()\n\n""")
    file.close()