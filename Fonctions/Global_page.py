import index
from Classes.BDDAttaque import *
import tkinter as tk
from PIL import ImageTk, Image
import os
from fonctions_ajouts import delete_pokemon


# =======================
# Couleurs par type Pokémon
# =======================
TYPE_COLORS = {
    "Plante": "#78C850",
    "Feu": "#F08030",
    "Eau": "#6890F0",
    "Electrik": "#F8D030",
    "Glace": "#98D8D8",
    "Combat": "#C03028",
    "Poison": "#A040A0",
    "Sol": "#E0C068",
    "Vol": "#A890F0",
    "Psy": "#F85888",
    "Insecte": "#A8B820",
    "Roche": "#B8A038",
    "Spectre": "#705898",
    "Dragon": "#7038F8",
    "Ténèbres": "#705848",
    "Acier": "#B8B8D0",
    "Fée": "#EE99AC",
    "Normal": "#A8A878"
}


# =======================
# Canvas avec fond dégradé
# =======================
class GradientCanvas(tk.Canvas):
    def __init__(self, parent, color1, color2, **kwargs):
        super().__init__(parent, **kwargs)
        self.color1 = color1
        self.color2 = color2
        self.bind("<Configure>", self.draw_gradient)

    def draw_gradient(self, event=None):
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()

        r1, g1, b1 = self.winfo_rgb(self.color1)
        r2, g2, b2 = self.winfo_rgb(self.color2)

        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            r = int(r1 + r_ratio * i)
            g = int(g1 + g_ratio * i)
            b = int(b1 + b_ratio * i)
            color = f"#{r//256:02x}{g//256:02x}{b//256:02x}"
            self.create_line(0, i, width, i, fill=color, tags=("gradient",))

        self.lower("gradient")


# =======================
# Page principale Pokémon
# =======================
def main(name):

    def delete():
        delete_pokemon(Pokemon.name, Pokemon.generation)
        screen.destroy()
        os.system("python ./Fonctions/main.py")

    def modif():
        screen.destroy()
        os.system("python ./Fonctions/modification.py")

    def return_page():
        screen.destroy()
        os.system("python ./Fonctions/main.py")

    Pokemon = index.pokedex.found_pages(name)

    # Couleurs du fond selon types
    color1 = TYPE_COLORS.get(Pokemon.type1, "#777777")
    if Pokemon.type2 not in [None, "None"]:
        color2 = TYPE_COLORS.get(Pokemon.type2, color1)
    else:
        color2 = color1

    # Fenêtre
    screen = tk.Tk()
    screen.title(Pokemon.name)
    screen.geometry("1000x650")

    canvas = GradientCanvas(
        screen,
        color1=color1,
        color2=color2,
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)

    # =======================
    # Widgets
    # =======================

    title = tk.Label(
        canvas,
        text=Pokemon.name,
        font=("Arial", 40, "bold"),
        fg="black",
        bg=canvas["bg"]
    )
    canvas.create_window(278, 60, window=title)

    image = ImageTk.PhotoImage(Image.open(Pokemon.img))
    label_image = tk.Label(canvas, image=image, bg=canvas["bg"])
    label_image.image = image
    canvas.create_window(750, 180, window=label_image)

    type1_img = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type1}.png"))
    label_type1 = tk.Label(canvas, image=type1_img, bg=canvas["bg"])
    label_type1.image = type1_img
    canvas.create_window(150, 140, window=label_type1)

    if Pokemon.type2 not in [None, "None"]:
        type2_img = ImageTk.PhotoImage(Image.open(f"./Type/Miniature {Pokemon.type2}.png"))
        label_type2 = tk.Label(canvas, image=type2_img, bg=canvas["bg"])
        label_type2.image = type2_img
        canvas.create_window(420, 140, window=label_type2)

    # Talents
    skills = [Pokemon.skill1, Pokemon.skill2, Pokemon.skill3]
    skills = [s for s in skills if s not in [None, "None"]]

    label_skill = tk.Label(
        canvas,
        text="Talents :\n" + " | ".join(skills),
        font=("Arial", 14),
        fg="black",
        bg=canvas["bg"],
        justify="left"
    )
    canvas.create_window(250, 220, window=label_skill)

    # Taille / Poids
    label_hw = tk.Label(
        canvas,
        text=f"Taille : {Pokemon.height} m\nPoids : {Pokemon.weight} kg",
        font=("Arial", 14),
        fg="black",
        bg=canvas["bg"],
        justify="left"
    )
    canvas.create_window(250, 300, window=label_hw)

    # # Capacités
    # listbox_capacity = tk.Listbox(canvas, width=50)
    # Pokemon.list_capacity(listbox_capacity)
    # canvas.create_window(300, 420, window=listbox_capacity)

    # Stats
    listbox_stat = tk.Listbox(canvas, width=50)
    Pokemon.list_stat(listbox_stat)
    canvas.create_window(700, 420, window=listbox_stat)

    # Boutons
    button_return = tk.Button(canvas, text="Retour", command=return_page)
    canvas.create_window(250, 580, window=button_return)

    button_delete = tk.Button(canvas, text="Supprimer", command=delete)
    canvas.create_window(750, 580, window=button_delete)

    button_modification = tk.Button(canvas, text="Modifier", command=modif)
    canvas.create_window(500, 580, window=button_modification)

    screen.mainloop()
