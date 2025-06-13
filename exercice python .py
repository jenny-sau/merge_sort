#{clé: valeur for élément in séquence if condition}
#codes = {"a": 1, "b": 2, "c": 3}
#nouveau_dict = {valeur: clé for clé, valeur in codes.items()}
#print(nouveau_dict)
#from curses.ascii import isdigit

#mot = "banane"
#dico = {lettre: mot.count(lettre) for lettre in set(mot)}
##print (dico)

#ots = ["salut", "bonjour", "yo"]
#ico = {mot: len(mot) for mot in mots}

#ots = ["chat", "chien", "cheval", "rat"]
#ico = {animal[0].upper(): animal for  animal in mots if len(animal) >4}

#prenoms = ["Alice", "Bob", "Charlotte", "Dan"]
#dico = {prenom: len(prenom) for prenom in prenoms}
#print(dico)

#dico2 = {prenom[0].upper(): prenom for prenom in prenoms}
#print(dico2)

#ombres = list(range(1, 21))
#ico3 = {i: i**2 for i in nombres if i%2==0 and(i**2)%4==0}
#rint(dico3)
#oyelles = "aeiouy"
#ots = ["arbre", "eau", "python", "ordinateur", "stylo"]
#ico4 = {mot: sum(mot.count(v) for v in voyelles) for mot in mots}
#rint(dico4)

#hrase = "le python est cool"

#ico4 = {i: phrase.count(i) for i in phrase if i.isalpha()}
#rint(dico4)

# Exercice 1 : Dictionnaire des longueurs de mots pairs
#crée un dictionnaire où :
#clé = mot
#valeur = longueur du mot
#Seulement pour les mots dont la longueur est paire.
#mots = ["pomme", "banane", "cerise", "kiwi", "fraise", "ananas"]
#dicolongpaires = { mot: len(mot) for mot in mots if len(mot)%2==0}
#print(dicolongpaires)

#Exercice 3:
# Crée un dictionnaire où :
#clé = lettre initiale (majuscule)
#valeur = nombre de mots commençant par cette lettre#
#mots = ["avion", "arbre", "bateau", "banane", "chat", "chien", "cactus"]

#dico_comptage_lettre = {
#    lettre: sum(m[0].upper() == lettre for m in mots)
#    for lettre in set(m[0].upper() for m in mots)
#}
#print(dico_comptage_lettre)

#COMPREHENSION DE LISTE:
#Exercice 1 — Carrés simples
#Crée une liste des carrés des nombres de 1 à 15.
#list_carré = [x**2 for x in range(1, 16)  ]
#print(list_carré)

#Exercice 2 — Filtrage
#Crée une liste des nombres de 1 à 50 qui sont divisibles par 3.
#list_1_to_50_divisible_par_3 = [x for x in range(1, 51) if x %3==0  ]
#print(list_1_to_50_divisible_par_3)

#Exercice 3 — Transformation + condition
#Crée une liste des doubles des nombres impairs entre 0 et 20.
#liste_double_impaire= [x*2 for x in range(0,21) if x%2!=0]
#print(liste_double_impaire)

#Exercice 4 — Chaîne de caractères
#À partir de la chaîne "programmation", crée une liste des lettres sans les voyelles.
#chaine = "programmation"
#voyelles= ('a','e','i','o','u','y')
#chaine_sans_voyelle = [char for char in chaine if char not in voyelles]
#print(chaine_sans_voyelle)

#matrice = [[j for j in range(3)] for i in range(3)]
#print(matrice)

#{clé: valeur for élément in séquence if condition}
#codes = {"a": 1, "b": 2, "c": 3}
#nouveau_dict = {valeur: clé for clé, valeur in codes.items()}
#print(nouveau_dict)


#phrases = ["Je mange une pomme.", "Ceci est un secret.", "Rien à cacher ici."]
#for index, phrase in enumerate(phrases):
#    print(f'{index:>2}. {"[CENSURÉ]" if "secret" in phrase else phrase}')

#------------------------------------------------------------------
# ------- Exercice 1 : Nombres carrés -----------------------
#Crée une liste contenant les carrés des nombres de 0 à 9.
#carre_liste = [x**2 for x in range (0,10)]
#print(carre_liste)

# --------Exercice 2: filtrage pair:
#Crée une liste contenant uniquement les nombres pairs entre 0 et 20 (inclus).
#nombres_pairs = [x for x in range (0,21) if x %2==0]
#print(nombres_pairs)

#-----Exercice 3 : Mots en majuscules
#À partir d'une liste de mots, crée une nouvelle liste contenant ces mots en majuscules.
#mots = ["chat", "chien", "oiseau"]
#mots_majuscule = [mot.upper() for mot in mots]
#print(mots_majuscule)

#------ Compréhensions de dictionnaire
#Exercice 4 : Mots et longueurs
#Crée un dictionnaire qui associe chaque mot à sa longueur.
#mots = ["python", "chat", "ordinateur"]
#mots_longueur = {cle: len(cle) for cle in mots  }
#print(mots_longueur)


#----- Exercice 5 : Carrés des nombres pairs
#Crée un dictionnaire où les clés sont les nombres pairs de 0 à 10 et les valeurs sont leurs carrés.
#carré_des_paires = {clé: clé**2 for clé in range(0,11) if clé % 2 == 0}
#print(carré_des_paires)

#----Exercice 6: Inverser un dictionnaire
# À partir d’un dictionnaire, crée un nouveau dictionnaire où les clés et valeurs sont inversées.
#d = {"a": 1, "b": 2, "c": 3}
#inversé = {v:c for c, v  in d.items()}
#print(inversé)

#----- La fonction enumerate
#Exercice 7 : Numérotation des éléments
#Affiche chaque élément d'une liste avec son indice, en utilisant enumerate.
#fruits = ["pomme", "banane", "cerise"]
#for index, fruit in enumerate(fruits):
#    print(f'{index}. {fruit}')

#---- Exercice 8 : Paires d’index impairs
#Récupère dans une nouvelle liste les éléments d’index impair d'une liste donnée.
#noms = ["Alice", "Bob", "Claire", "David", "Emma"]
#nom_index_impaires = [nom for index, nom in enumerate(noms) if index % 2 !=0]
#print(nom_index_impaires)

#----- LIST COMPREHENSION — Niveau 2
#Exercice 1 : Mots de plus de 4 lettres
#Exercice 1 : Mots de plus de 4 lettres
#mots = ["arbre", "chat", "ordinateur", "clé", "papillon"]
#mots_sup_4 = [mot for mot in mots if len(mot) >4 ]
#print(mots_sup_4)

#----- Exercice 2: double voyelle
#À partir d’une phrase, construis une liste des lettres doublées si ce sont des voyelles.
#phrase = "chaton"
#phrase_voyelle_double = [char*2  if char in 'aeiouy' else char for char in phrase ]
#print(phrase_voyelle_double)

#📚 DICT COMPREHENSION — Niveau 2
#Exercice 3 : Filtrer un dictionnaire
#À partir d’un dictionnaire contenant des noms et âges, crée un nouveau dictionnaire avec uniquement les personnes de plus de 18 ans.
#ages = {"Alice": 17, "Bob": 22, "Claire": 19, "David": 15}
#personne_majeur = {nom: age for nom, age in ages.items() if age >18}
#print(personne_majeur)

#Exercice 4 : Dictionnaire inversé avec doublage
#À partir d’un dictionnaire clé → valeur (ex: produit → prix), crée un dictionnaire inversé, mais avec les valeurs doublées.
#produits = {"stylo": 2, "cahier": 5, "gomme": 1}
#inversé_et_doublé = {valeur*2: clé for clé, valeur in produits.items()}
#print(inversé_et_doublé)

#enumerate
#Exercice 5 : Ajouter un numéro de ligne --> J?ai eu pas mal de peine avec celui là  j'ai du chercher des indices sur internet
#À partir d’une liste de phrases, crée une nouvelle liste avec les phrases numérotées (comme dans un script).
#repliques = ["Bonjour.", "Comment ça va ?", "Très bien, merci."]
#replique_indexé = [f"{index+1} - {replique}" for index, replique in enumerate(repliques)]
#print(replique_indexé)

#Exercice 6: Repérer les erreurs --> Sur cette exercice j'ai aussi mis pas mal de temmps et j'ai cherché dans mes notes... c'était pas très naturelle pour moi celuil là
#À partir d’une liste de notes (sur 20), affiche toutes les notes < 10 avec leur position dans la liste (index), en utilisant enumerate.
#notes = [12, 7, 14, 9, 8, 16]
#for index, note in enumerate(notes):
#    if note<10:
#        print(f"Note insuffisante à l'index {index} : {note}")

#---------------- Exercices Spéciaux enumerate()
#🧠 Exercice 1 : Affichage pair/impair avec index
#Affiche chaque élément d'une liste avec son index, en indiquant si l’index est pair ou impair.
#animaux = ["chat", "chien", "poisson", "oiseau", "hamster"]
#for index, animal in enumerate(animaux):
#    print(f" Index  {index} {'pair' if index%2==0 else 'impair'}: {animal} ")


#1. Exercices de compréhension de liste
#🔸 Exercice 1
#Créer une liste contenant les carrés des nombres de 0 à 10 inclus.
#carré_1_à_10 = [x**2 for x in range(0,11)]
#print(carré_1_à_10)

#Exercice 2
#Créer une liste contenant uniquement les nombres pairs entre 1 et 50.
#pairs_1_à_50 = [x for x in range(0,51) if x%2==0 ]
#print(pairs_1_à_50)

#Exercice 3:
#mots = ["arbre", "soleil", "chat", "ordinateur", "eau"]
#longueures_mot = [len(mot) for mot in mots]
#print(longueures_mot)

#Exercice 4
#cube_nombres_impair = [x**2 for x in range(0,20) if x%2!=0]
#print(cube_nombres_impair)

#🔹 2. Exercices de compréhension de dictionnaire
#ex 1:
#dico_carré = {x:x**2 for x in range(1,6) }
#print(dico_carré)

#Exercice 2:
#Créer un dictionnaire avec chaque mot comme clé, et le nombre de lettres comme valeur.
#animaux = ["chat", "chien", "singe"]
#dico_animaux = {animal: len(animal) for animal in animaux }
#print(dico_animaux)

#Exercice 3:
#mot = "Python"
#dico_python = {char: char.upper() for char in mot}
#print(dico_python)

#🔹 3. Exercices avec enumerate()
#Ex 1
#fruits = ["pomme", "banane", "cerise"]
#for index, fruit in enumerate(fruits):
#    print(f'{index} - {fruit}')

#Ex 2:
#dico_index_fruit = {index: fruit for index, fruit in enumerate(fruits)}
#print(dico_index_fruit)

#Exercice 3: ---> J'ai eu + de mal avec celui là, c'était plus difficile pour moi
#phrase = "le python est amusant"
#liste_index_mot = [(index, mot) for mot, index in enumerate(phrase.split())]
#print(liste_index_mot)

#------ Fonction map:
# Niveau facile -
#1. Convertir des chaînes en entiers
#Entrée : une liste comme ["10", "20", "30"]
#Objectif : la transformer en [10, 20, 30]
#📌 Utilise map(int, ...)
#Nombres = ["10", "20", "30"]
#resultat = map(int,Nombres)
#print(list(resultat))

#ex2: Élever chaque nombre au carré
#entree = [1, 2, 3, 4]
#sortie = map(lambda x: x**2, entree)
#print(list(sortie))

#Filtrer les nombres pairs
#num = [1, 2, 3, 4, 5, 6]
#paires = filter(lambda x: x %2== 0 , num)
#print(list(paires))

#somme = lambda x,y: x+y
#print(somme(5,7))

#liste_triee = sorted([("a", 3), ("b", 1), ("c", 2)], key=lambda x: x[1])
#print(liste_triee)

#new_chaine = map(lambda char: char.lower(), ["PYTHON", "java", "C++"])
#print(list(new_chaine))

#nombre_positif = lambda x: x>0
#print(nombre_positif(3))

#- Exercices niveau intermédiaire
#Doubler tous le nombres
#ex1= map(lambda x: x*2,[3, 6, 9])
#print(list(ex1))

#Calculer la longueur des mots
#ex2 = map(lambda x: len(x), ["chat", "éléphant", "rat"])
#print(list(ex2))

#3. 🔁 Inverser chaque mot
#ex3= map(lambda x: x[::-1], ["bonjour", "python", "lambda"])
#print(list(ex3))

#4. ⏱️ Convertir des minutes en heures:minutes
#ex4= map(lambda x:divmod(x, 60), [90, 120, 135])
#print(list(ex4))

#Ajouter un suffixe à chaque mot
#ex5 = map(lambda x: x+".txt", ["file", "book", "car"])
#print(list(ex5))

# Élève chaque élément au carré et ajoute 1
#ex6= map(lambda x: (x**2)+1, [1, 2, 3])
#print(list(ex6))

#----Niveau avancé
#ex7= map(lambda x: ("pair" if x%2==0 else "impair"), [1, 2, 3, 4])
#print(list(ex7))

# Miroir : mot et sa longueur
#ex8= map(lambda x: [x, len(x)], ["chat", "chien"])
#print(list(ex8))
#---> Est-ce que dans cet exercice une compréhension de liste aurait été possible?

#9. 🎉 Bonus : combiné map + filter
#num = [1, 2, 3, 4, 5, 6]
#ex9 = map(lambda x: x*2, filter(lambda x:x%2==0, num))
#print(list(ex9))
#--> Cet exercice c'était moins naturelle faut que je renforce comment combiner map et filter

#celsius = map((lambda x:  x * 9/5 + 32), [0, 10, 20, 30])
#print(list(celsius))

#Rendre toutes les chaînes minuscules + sans espace autour
#mots = ["  Bonjour", "MONDE ", " PyThOn  "]
#print(list(map(lambda x: x.lower().strip(), mots)))

#Filtrer les nombres supérieurs à 100
#nombres = [10, 150, 200, 99, 101]
#ex3 = list(filter (lambda x: x>10, nombres))
#print(ex3)
#--> Cet ex m'a pris + de temps c'est pas encore très naturel

#----Niveau Intermédiaire
#4. 🧮 Calculer le carré + 2 de chaque nombre impair uniquement
#entiers = [1, 2, 3, 4, 5]
#ex4= map(lambda x: x**2+2, filter(lambda x: x%2!=0, entiers))
#print(list(ex4))

#5. 🧵 Ajouter un préfixe "item_" à chaque élément d’une liste
#choses = ["chaise", "table", "lampe"]
#ex5 = list(map(lambda x: "item_"+x, choses))
#print(ex5)

#ex6 6. 🧠 Filtrer les mots de plus de 4 lettres, puis retourner chaque mot
#mots = ["chat", "éléphant", "rat", "grenouille"]
#ex6 = map(lambda x: x[::-1], filter(lambda x: len(x)>4, mots))
#print(list(ex6))

#--- Niveau Avancé
#7. 🕘 Extraire uniquement les durées valides (< 90 min) et les convertir en h:min
#durees = [45, 120, 30, 95, 89]
#ex7= map(lambda x: divmod(x,60), filter(lambda x: x<90, durees))
#print(list(ex7))

#8. 🔍 Filtrer les tuples ayant un score > 50 et retourner juste les noms en majuscules
#notes = [("Alice", 45), ("Bob", 80), ("Charlie", 55)]
#ex9=  list(map(lambda x: x[0].upper(), filter(lambda x: x[1]>50, notes)))
#print(ex9)

#Ex9  Créer une liste de dictionnaires à partir de deux listes (clé : valeur)
#cles = ["nom", "age", "ville"]
#valeurs = ["Alice", 30, "Paris"]
#ex9 = map(lambda x, y: {x:y}, cles, valeurs)
#print(list(ex9))

#🔸 Exercice 1 : Compter les voyelles
#mot = "bonjour"
#voyelles = "aeiouAEIOU"
#nb = sum(1 for c in mot if c in voyelles)
#print(nb)

#compter les majuscule
#phrase = "BonJour LE monde"
#nb_maj = sum(1 for c in phrase if c.isupper())
#print(nb_maj)

#Compter les chiffres dans une chaine
#But : Afficher combien de chiffres (0–9) se trouvent dans un texte.
#phrase_ex3=  "Il y a 2 chats et 15 souris"
#nb_d = sum(1 for c in phrase_ex3 if c.isdigit())
#print(nb_d)

#Exercice4 - Nombre de mots de plus de 5 lettres
#ut : Demander une phrase, et afficher combien de mots ont plus de 5 lettres.
#phrase = "Bonjour le monde incroyable"
#nb_m = sum(1 for mot in phrase.split() if len(mot)>5)
#print(nb_m)


#Ex1
#Objectif : Demande à l’utilisateur d’entrer un nombre, puis affiche la somme de ses chiffres.
#nombre= (input("Entrer un nombre"))
#chiffre = [int(c) for c in str(nombre)]
#print(" + ".join(str(c) for c in chiffre)," = ", (sum(chiffre)))

# Exercice 2 : Inverser un nombre
#Objectif : Écris un programme qui prend un nombre (par exemple 456) et affiche 654
#nombre= 456
#chiffre = [int(c) for c in str(nombre)]
#chiffre_inv = chiffre[::-1]
#print(''.join(str(c) for c in chiffre_inv))
#--> J'ai eu pas mal de mal, j'ai encore de la peine enfaite à savoir ce qui exige un str

#📊 Exercice 3 : Compter les chiffres pairs et impairs
#Objectif : Pour un nombre donné, compte combien de chiffres sont pairs et combien sont impairs.
#entree= 12345666
#chiffre = [int(c) for c in str(entree)]
#print(f'{sum(1 for c in chiffre if c % 2 !=0)} chiffre impairs, {sum(1 for c in chiffre if c % 2 ==0)} chiffre pairs')

#Ex 4: Liste eds carrés des chiffres
#Objectif : Crée une liste contenant le carré de chaque chiffre d’un nombre.
#entree= 314
#sortie= [x**2 for x in [int(x) for x in str(entree)]]
#print(sortie)

#---------------------
#🔢 Exercice 1 – Compter les voyelles
#phrase_ex1 = str(input("Entrer un phrase"))
#print(sum(1 for c in phrase_ex1 if c.lower() in "aeiou"))

#Exercice 2 Compter les mots longs
phrase_ex2= "Il fait incroyablement beau aujourd’hui"
print(sum(1 for mot in phrase_ex2.split() if len(mot)> 4))

# Exercice 3 – Combien d’éléments > 10 dans une liste
list_ex3=[3, 17, 22, 5, 9, 11]
print(sum(1 for i in list_ex3 if i>10))

#ex4: Combien de chaînes vides
ex4=["bonjour", "", "ok", "", "salut"]
print(sum(1 for i in ex4 if i==""))

#exercice_5 - Moyenne des nombres positifs uniquement
import statistics

ex5 = [-10,-100, -10]
nb_positif= [i for i in ex5 if i>0]
positif= sum(1 for i in ex5 if i>=0)
negatif= sum(1 for i in ex5 if i<=0)
moyenne = "Aucun positif" if not nb_positif else statistics.mean(nb_positif)

print(f'''
Chiffre positif : {positif if positif>0 else "Aucun positif!" }
Chiffre negatif:{negatif}
Moyenne des positif: {moyenne}
''')
