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
    while verbe.isalpha() and terminaison != "er":
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

# 2 Distance entre deux mots
# Calculer la distance de Hamming entre deux mots

def hamming():
    mot1 = input("Veuillez entrer un premier mot : ")
    while not mot1.isalpha() :
        mot1 = input("Veuillez entrer un premier mot : ")
    mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    while not mot2.isalpha() :
        mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    if len(mot1) != len(mot2):
        return "Les mots ne sont pas de la même longueur"
    else:
        distance = 0
        for i in range(len(mot1)):
            if mot1[i] != mot2[i]:
                distance += 1
        return distance
    
print(hamming())

# Autre possibilité
def hamming2():
    mot1 = input("Veuillez entrer un premier mot : ")
    while not mot1.isalpha() :
        mot1 = input("Veuillez entrer un premier mot : ")
    mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    while not mot2.isalpha() :
        mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    if len(mot1) != len(mot2):
        return "Les mots ne sont pas de la même longueur"
    else:
        distance = 0
        for c1, c2 in zip(mot1, mot2):
            if c1 != c2:
                distance += 1
        return distance
        
print(hamming2())

# hamming2 condensé
def hamming3():
    mot1 = input("Veuillez entrer un premier mot : ")
    while not mot1.isalpha() :
        mot1 = input("Veuillez entrer un premier mot : ")
    mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    while not mot2.isalpha() :
        mot2 = input("Veuillez entrer un deuxième mot de même longueur : ")
    if len(mot1) != len(mot2):
        return "Les mots ne sont pas de la même longueur"
    else:
        return sum(c1 != c2 for c1, c2 in zip(mot1, mot2))
        
print(hamming3())

# 3 Mot à l'envers
# Afficher un mot à l'envers

def alenvers():
    mot = input("Veuillez saisir un mot : ")
    print("Le mot", mot, "donne à l'envers : ", end="")
    for i in range(len(mot)):
        print(mot[-1-i], end="")
    print()

alenvers()

# Version simplifiée
def alenversSimple():
    mot = input("Veuillez entrer un mot : ")  
    print(mot[::-1])

alenversSimple()

# 4 Calculer les racines d’un polynôme du second degré    
def racines():
    coeff = input("Veuillez entrer les 3 coefficients du polynôme séparés par un espace : ")
    listeCoeff = coeff.split()
    a = float(listeCoeff[0])
    b = float(listeCoeff[1])
    c = float(listeCoeff[2])
    delta = b**2 - 4 * a * c
    if delta > 0:
        print("Votre polynôme a 2 racines réelles:", (-b + sqrt(delta)) / 2*a, "et", (-b - sqrt(delta)) / 2*a)
    elif delta < 0:
        print("Votre polynôme n'a pas de racine réelle")
    else:    
        print("Votre polynôme a 1 racine réelle:", -b/2*a)

racines()

# 5 Addition des n premiers entiers 
def sommepremiers():
    mot = input("Veuillez entrer un nombre entier: ")
    while not mot.isdigit():
        mot = input("Veuillez entrer un nombre entier (que des chiffres) : ")
    n = int(mot)  
    somme = 0
    for i in range(n + 1):
        somme += i
    print("La valeur de la somme des entiers de 1 à", n, "vaut", somme)

sommepremiers()

# 6 Infiniment petit
def divisions():
    print("XX" + "0123456789" * 5)
    valeur = 1
    for _ in range(50):
        valeur /= 2
        print("{0:51.50f}".format(valeur))

divisions()

# 7 Décompte des nombres à deux chiffres ayant le chiffre 7
def decompteNombresAvec7():
    nombrede7 = 0
    for i in range(10, 100):
        if (i//10 == 7 or i%10 == 7):
            nombrede7 += 1
    print("Parmi les nombres à 2 chiffres , il y en a", nombrede7, "qui ont un 7")

decompteNombresAvec7()

#Bonus : Decompte du nombre de 7 dans les nombres à 2 chiffres
def decompteChiffresAvec7():
    nombrede7 = 0
    for i in range(10, 100):
        if (i//10 == 7):
            nombrede7 += 1
        if (i%10 == 7):
            nombrede7 += 1
    print("Il y a", nombrede7, "7 dans les nombres à 2 chiffres")

decompteChiffresAvec7()

# 8 Décompte des consonnes dans un mot

# Version incomplète
def decompteIncomplet():
    mot = input("Veuillez entrer un mot: ")
    while not mot.isalpha():
        mot = input("Veuillez entrer un mot (que des lettres) : ")
    mot = mot.upper()    
    nbVoyelles = 0
    longueurMot = len(mot)
    for c in mot:
        if (c == "A" or c == "E" or c == "I" or c == "O" or c == "U" or c == "Y"):
            nbVoyelles += 1
    print("Le mot", mot, "a", longueurMot - nbVoyelles, "consonne(s)")

decompteIncomplet()

'''
NB : On n'a pa considéré les voyelles avec accent qui seraient considérées comme des consonnes
Soit on inclut les tests c == 'À' ...
Soit on enlève les accents du mot avec par exemple
import unidecode
motSansAccent = unidecode.unidecode(mot)
''' 

# Version complète
def decompte():
    mot = input("Veuillez entrer un mot: ")
    while not mot.isalpha():
        mot = input("Veuillez entrer un mot (que des lettres) : ")
    mot = mot.upper() 
    voyelles = ["A", "E", "I", "O", "U", "Y", "À", "É", "È", "Ù", "Â", "Ê", "Î", "Ô", "Û", "Ä", "Ë", "Ï", "Ö", "Ü", "Æ", "Œ"]
    nbVoyelles = 0
    for c in mot:
        if c in voyelles:
            nbVoyelles += 1
    print("Le mot", mot, "a", len(mot) - nbVoyelles, "consonne(s)")

decompte()

# 9 Encodage et décryptage d'un nom

def encodeDecode():
    decalage = 3
    nom = input("Veuillez entrer votre nom agent : ")
    while not nom.isalpha():
        nom = input("Veuillez entrer un mot (que des lettres) : ")
    nom = nom.upper()  
    nomCode = ""
    for c in nom:
        nomCode += chr((ord(c) - ord('A') + decalage) % 26 + ord('A'))
    print("Votre nom de code est", nomCode)

    nomCode = input("Veuillez entrer votre nom de code : ").upper()
    while not nomCode.isalpha():
        nomCode = input("Veuillez entrer un mot (que des lettres) : ")
    nomCode = nomCode.upper()  
    nom = ""
    for c in nomCode:
        nom += chr((ord(c) - ord('A') - decalage) % 26 + ord('A'))
    print("Votre nom d'agent est", nom)

encodeDecode()

# 10 Balises d'une page HTML

def balises(page):
    for i in range(len(page)):
        if page[i] == "<":
            posFinBalise = page.find(">", i)
            print(page[i+1:posFinBalise])    

exemple = "<html> <head> <title> Mon Titre </title> </head> <body> Texte sur la page </body> </html>"
balises(exemple)

# 11 Calendrier du mois

def calendrier():
    """Affiche le calendrier du mois"""
    nbJours = input("Veuillez enter le nombre de jours dans le mois : ")
    while not (nbJours.isdigit() and int(nbJours) > 27 and int(nbJours) < 32):
        nbJours = input("Veuillez enter un nombre entre 28 et 31 : ")
    nbJours = int(nbJours) 
    numJour = input("Veuillez entrer le numéro du jour démarrant le mois (1 pour lundi,..., 7 pour dimanche) : ") 
    while not (numJour.isdigit() and int(numJour) > 0 and int(numJour) < 8):
        numJour = input("Veuillez entrer un chiffre entre 1 et 7 : ")
    numJour = int(numJour)
    print("LUN MAR MER JEU VEN SAM DIM")
    for i in range(numJour - 1):
        print(" " * 4, end="")
    colCourante = numJour - 1
    for i in range(nbJours):
        print("{0:^4}".format(i+1), end="")
        colCourante = (colCourante + 1) % 7
        if colCourante == 0:
            print()
    print()

calendrier()

# 12 Statistiques avec pile ou face 
# Simulation de tirages répétés de pile ou face et statistiques

def statistiques():
    nbTirages = input("Veuillez enter le nombre de tirages : ")  
    while not nbTirages.isdigit():
        nbTirages = input("Veuillez enter le nombre de tirages (en chiffres) : ")  
    nbTirages = int(nbTirages) 
    nbPiles = 0
    nbFaces = 0   
    for i in range(nbTirages):
        if randint(0,1) == 0:
            nbPiles += 1
        else:
            nbFaces += 1
    pPiles = round(nbPiles / nbTirages * 100)  
    pFaces = round(nbFaces / nbTirages * 100)     
    print("Sur", nbTirages, "tirages, il y a eu", pPiles, "% de pile et", pFaces, "% de face")

statistiques()