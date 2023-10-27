import qcm
import random

liste_reponse=[]
rdm_question=[]
reponses_fausses=0


def PRNG(nombre):
    """
        Pre: recupère un entier positif n
        - crée une liste allant de 0 à n-1 en order croissant
        Post: retourne liste avac les élément en mode aléatoire
    """

    rdm=random.Random()
    lst=list(range(nombre))
    rdm.shuffle(lst)
    return lst


def est_chiffre(rep, nombre_rep):
    """ Pre: recupere la valeur de la variable reponse et un nombre ebtier positif 1
        * verifie si la valeur de la variable reponse est un chiffre et si c'est un chiffre, il doit se trouve ventre 0 et n, 0 inclu
        * ensuit elle oblige l'utilisateur à donnez une nouvelle reponse tant que 2 les conditions citez si dessus ne sont pas respectées.
        Post: retourne la un entier positif entre 0 et n, 0 inclu
    """ 

    while not rep.isdigit() or int(rep)<0 or int(rep)>(nombre_rep-1):
        rep=input("Repondez par un chiffre entre 0 et " + str(nombre_rep-1) + ": ")
        print(" ")
    return rep


def questionnaire(ques, liste_rep):
    """
       Pre: recupère 2 listes
       *melange les éléments de la première liste grace à la fonction PRNG()
       *affiche les questions et recupère les reponse qu'il check avec la fonction est chiffre
       *enregistre les reponses dans la deuxieme liste
       Post: retourne la deuxieme liste
    """
       
    global rdm_question
    num=1
    rdm_question=PRNG(len(ques))   #crée une liste nombre aléatoire entre 0 et nombre d'élément sur la liste questions

    for q in rdm_question:
        print("\tQuestion " + str(num) + ": \"" + ques[q][0] + "\"") #se sert des éléments de la liste rdm_question comme index des élément de la liste questions pour afficher les question aléatoirement

        print("\t\tChoisir parmi " + ":")
        
        num2=0
        rdm_proposition=PRNG(len(ques[q][1]))    #fait la même chose qu'à la ligne 45 mais avec la liste de des proposition
        for r in rdm_proposition:
            print("\t\t\t" + str(num2) + " : " + ques[q][1][r][0] + "\"") #la même chose qu'à la ligne 48 mais avec les propositions
            num2+=1

        longeur=len(ques[q][1])
        reponse=input("Votre réponse: ")
        liste_rep.append(rdm_proposition[int(est_chiffre(reponse, longeur))]) #ajoute les réponses vérifiées dans la liste
        num+=1
    
    return liste_rep


def mauvaise_reponses(repo):
    """
       Pre: recupere une liste(de reponses données) dont tout les élément sont des entiers positif
       * compare les réponses de la liste avec la liste question
       *compte le nombre de mauvaise réponses sur la liste
       Post: returne le nombre de mauvaise réponse
    """

    index_reponses=0
    mauvais=0
    for question in rdm_question:
        if questions[int(question)][1][int(repo[int(index_reponses)])][1] == False:
            mauvais+=1
        index_reponses+=1

    
    return mauvais


def commentaire(l):
    """
       Pre: recupère une liste de réponse
       Post: affiche 
    """
    index_reponses = 0
    print()
    print("\t\t\t\t\tFEEDBACK:")
    for (question,i) in zip(rdm_question,l):
        quest=questions[int(question)][1]
        if quest[i][1]== False:
            if quest[i][2]!= "":
                print("- ", quest[i][0], " = ", quest[i][2])
        
    index_reponses+=1

    
def calcule_resultats(bonne_rep, reponses_fau):
    """
        Pre: Recupère 2 entier >=0
        fait 3 calcules differents qu'elle stocke dans 3 variables differentes
        elle stocke les 3 variables dans une liste
        Post: retourne la liste
    """

    cote_1 = bonne_rep
    cote_2 = bonne_rep - reponses_fau
    if cote_2<0:
        cote_2=0

    cote_3 = round((bonne_rep - (reponses_fau * 0.3)), 2)
    les_cotes = [cote_1, cote_2, cote_3]

    return les_cotes


def mode_comparatif(cotes):
    """
        Pre: recupère une liste de réel >=0
        Post: affiche les élément de la liste un par un
    """

    les_mode = ["Cotation normale", "-1 à chaque mauvaise réponse", "-0.3 à chaque mauvaise réponse"]
    print("LES RESULTAT EN MODE COMPARATIF")

    for i,(c,m) in enumerate(zip(cotes, les_mode)):
        print(i+1, ". ", m, ": ", c,"/", len(qcm.build_questionnaire(filename)))


def mode_evaluatif(cotas):
    """
        Pre: recupere une liste des réel >= 0
        demande à l'utilisateur quel élément de la liste afficher
        Post: affiche l'élement de la liste
    """

    print("MODE EALUATIF")
    les_modes = ["Cotation normale", "-1 à chaque mauvaise réponse", "Cotation anti-aléatoire"]

    for i,m in enumerate(les_modes):
        print("\t\t", i , " : ", m)
    choix =input("Votre réponse : ")
    choix = int(est_chiffre(choix,3))
    
    print(les_modes[choix], ": ", cotas[choix], "/", len(qcm.build_questionnaire(filename)))


if __name__ == '__main__':
    filename = "QCM.txt"
    questions = qcm.build_questionnaire(filename)
    
    print("VOICI LE QUESTIONNAIRE: tappez un chiffre")

    liste_reponse = questionnaire(questions, liste_reponse)
    reponses_fausses = int(mauvaise_reponses(liste_reponse))
    bonne_reponses = len(questions) - reponses_fausses

    les_cotes = calcule_resultats(bonne_reponses, reponses_fausses)

    print("CHOIX DE MODE D'AFFICHAGE")
    print("Entrer un chiffre pourchoisir le mode d'affichage")
    print("\t\t" + " 0 - Mode Comparatif")
    print("\t\t" + " 1 - Mode Evaluatif")
    choix = input("Votre réponse: ")
    choix = int(est_chiffre(choix, 2))

    if choix == 0:
        mode_comparatif(les_cotes)
    else:
        mode_evaluatif(les_cotes)
    
    commentaire(liste_reponse)