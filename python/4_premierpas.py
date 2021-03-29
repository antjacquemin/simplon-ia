# Pour l'exercice 4
from math import sqrt
# Pour le dernier exercice
from random import randint

# 1 Présent de l'indicatif 
# Conjuger au présent de l'indicatif un verbe du permier groupe

# Version naïve
def conjugaisonNaive(verbe):
    pronoms = ["je ", "tu ", "il ", "nous ", "vous ", "ils "]
    terminaisons = ["e", "es", "e", "ons", "ez", "ent"]
    baseVerbale = verbe[:-2]
    for i in range(6):
        print(pronoms[i] + baseVerbale + terminaisons[i])

conjugaisonNaive("manger")
conjugaisonNaive("aimer")

# Version complète
def conjugaison():
    # On récupère le verbe saisi par l'utilsateur
    verbe = input("Veuillez entrer un verbe du premier groupe : ")
    # On vérifie la terminaison
    terminaison = verbe[-2:]
    # Tant que ce n'est pas un verbe du premier groupe
    while terminaison != "er":
        # On réitère
        verbe = input("Veuillez entrer un verbe du premier groupe (-er) : ")
        terminaison = verbe[-2:]
    # Liste des pronoms personnels sujets
    pronoms = ["je ", "tu ", "il/elle ", "nous ", "vous ", "ils/elles "]
    # Liste des terminaisons pour les verbes du premier groupe
    terminaisons = ["e", "es", "e", "ons", "ez", "ent"]
    baseVerbale = verbe[:-2]
    # Liste des initiales des verbes pour lesquels il y a élision
    elisions = ["a", "e", "h", "i", "o", "u", "y"]
    # Si l'initiale fait partie de la liste
    if baseVerbale[0] in elisions:
        # On applique l'élision à la première personne du singulier
        pronoms[0] = "j'" 
    # On conjugue normalement
    present = [pronoms[i] + baseVerbale + terminaisons[i] for i in range(6)]
    # On va considérer les exceptions
    # Les verbes en -ger
    if baseVerbale[-1] == "g":
        # voient un e apparaître pour nous
        present[3] = present[3][:-3] + "e" + present[3][-3:]
    # Les verbes en -cer
    elif baseVerbale[-1] == "c":
        # voient une cédille apparaître pour nous
        present[3] = present[3][:-3] + "ç" + present[3][-3:]
    # Les verbes en -ayer, -oyer, -uyer (optionnel pour ceux en -ayer)
    elif baseVerbale[-2:] in ["ay", "oy", "uy"]:
        # voient pour je, tu, il/elle, ils/elles
        for i in (0, 1, 2, 5):
            # leur y changé en i
            present[i] = pronoms[i] + baseVerbale[:-1] + "i" + terminaisons[i]
    # Les verbes en -eler et -eter #voient pour je, tu, il/elle, ils/elles
    elif baseVerbale[-2:] in ["el", "et"]:
        # sauf pour acheter, geler, haleter, déceler, modeler, ciseler, congeler, marteler et crocheter
        if baseVerbale in ["achet", "gel", "halet", "décel", "model", "cisel", "congel", "martel", "crochet"]:
            for i in (0, 1, 2, 5):
                # où le e prende un accent grave
                present[i] = pronoms[i] + baseVerbale[:-2] + "è" + baseVerbale[-1] + terminaisons[i]
        else:
            for i in (0, 1, 2, 5):
                # voient leur dernière consonne doublée
                present[i] = pronoms[i] + baseVerbale + baseVerbale[-1] + terminaisons[i]
    # Les verbes en -ecer, -emer, -ener, -eper, -erer, -eser, -ever, -écer, -éder, -éler, -émer, -éner, -érer, -éser, -éter, -éyer
    elif baseVerbale[-2:] in ["ec", "em", "en", "ep", "er", "es", "ev", "éc", "éd", "él", "ém", "én", "ér", "és", "ét", "éy"]:
        for i in (0, 1, 2, 5):
            # prennent un accent grave
            present[i] = pronoms[i] + baseVerbale[:-2] + "è" + baseVerbale[-1] + terminaisons[i]
    # Les verbes en -evrer, -ébrer, -écher, -écrer, -égler, -égner, -égrer, -éguer, -équer, -étrer, -évrer
    elif baseVerbale[-3:] in ["evr", "ébr", "éch", "écr", "égl", "égn", "égr", "égu", "équ", "étr", "évr"]:
        for i in (0, 1, 2, 5):
            # prennent un accent grave
            present[i] = pronoms[i] + baseVerbale[:-3] + "è" + baseVerbale[-2:] + terminaisons[i]
    for mot in present:
        print(mot)

# Exemples de verbes à tester : aimer, manger, placer, payer, nettoyer, essuyer, jeter, appeler, acheter, amener, espérer
conjugaison()

