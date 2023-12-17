def mot_a_lenvers(mot):
    """
    Le mot est réécris mais à l'envers
    
    
    >>> verlant('bonjour')
    ruojnob
    >>> verlant ('ruojnob')
    bonjour
    """
    
    inverse = ''
    for x in mot:
        inverse = x + inverse
    print (inverse)
 
    
def derniere_lettre(mot):
    """
    On prend les quatre dernières lettres du mot pour les mettre à l'avant puis on met les 3 premières devant.
    Il faut que le mot fasse minimum 3 lettres.
    Si il n'y a pas quatre lettres alors la quatrième lettre qui devait être choisie sera la dernière
    Si le script fais plus de 7 lettres alors les lettres entre la troisième en partant du début et la quatrième en partant
    de la fin seront effacées.
    (je ne sais pas pourquoi mais la console m'affiche pleins d'erreurs avec import doctest alors qu'avec la console
    tout marche très bien)
    >>> derniere_lettre('bonjour')
    ruojbon
    >>> derniere_lettre('bon')
    nobnbon
    >>> derniere_lettre('mangéer')
    reégman
    >>> derniere_lettre('manger')
    regnman
    >>> derniere_lettre('mange')
    egnaman
    >>> derniere_lettre('bonjourour')
    ruorbon
    """
    mot = (mot[len(mot) -1] + mot[len(mot)-2] + mot[len(mot)-3] + mot[len(mot)-4] + mot[0] + mot[1] + mot[2])
    print (mot)
    
    
def e_au_carre(mot):
    """
    On prend le nombre de e du mot pour le mettre à la puissance de 2.
    Le nombre de e qu'on obtient se place à la fin du mot.
    
    >>> accent_sur_e('estbane')
    estbaneeeee
    >>> accent_sur_e('estbanee')
    estbaneeeeeeeeee
    >>> accent_sur_e('estebane')
    estebaneeeeeeeee
    """
    variable = 'e'
    for lettre in mot:
        if lettre in ['e']:
            variable = variable * 2
    print(mot + variable)    
    
    
 
import doctest
doctest.testmod()