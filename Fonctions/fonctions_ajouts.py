import os

def ajout_index(name):
    file=open(f"./Fonctions/index.txt","a",encoding='utf-8')
    file.write(f"""\n{name}""")
    file.close()


def ajout_pkm(name,number,stat,type1,type2,skill1,skill2,skill3,height,weight,generation,capacity):
    link = f"./Pokémon_img/{generation}/{name}.png"
    file=open(f"./Fonctions/index.py","a",encoding='utf-8')
    file.write(f"""pokedex.ajout("{name}",{number},"{generation}",{stat},[{capacity}],"{link}","{type1}","{type2}","{skill1}","{skill2}","{skill3}",{height},{weight})""")
    file.close()

def modif_pkm(name,number,stat,type1,type2,skill1,skill2,skill3,height,weight,generation,capacity):
    link = f"./Pokémon_img/{generation}/{name}.png"
    with open("./Fonctions/index.py", "r",encoding='utf-8') as fp:
        lines = fp.readlines()

    with open("./Fonctions/index.py", "w", encoding='utf-8') as fp:
        for line in lines:
            if f"{name}" not in line.strip("\n"):
                fp.write(line)
    file=open(f"./Fonctions/index.py","a",encoding='utf-8')
    file.write(f"""pokedex.ajout("{name}",{number},"{generation}]",{stat},[{capacity}],"{link}","{type1}","{type2}","{skill1}","{skill2}","{skill3}",{height},{weight})""")
    file.close()

def delete_pokemon(name,generation):

    dossier=os.listdir('./Fonctions')
    print(dossier)
    with open("./Fonctions/index.py", "r",encoding='utf-8') as fp:
        lines = fp.readlines()

    with open("./Fonctions/index.py", "w", encoding='utf-8') as fp:
        for line in lines:
            if f"{name}" not in line.strip("\n") or f'{generation}' not in line.strip("\n"):
                fp.write(line)
    with open("./Fonctions/index.txt", "r",encoding='utf-8') as fp:
        lines = fp.readlines()

    with open("./Fonctions/index.txt", "w", encoding='utf-8') as fp:
        for line in lines:
            if f"{name}" != line.strip("\n"):
                fp.write(line)
    