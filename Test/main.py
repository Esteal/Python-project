def uniquement_minuscules(mot):
    """
    mot -- chaîne de caractères

    renvoie True si mot n'est constitué que de minuscules de l'alphabet,
    False sinon.
    >>> uniquement_minuscules('azeRty')
    False
    >>> uniquement_minuscules('azerty')
    True
    """
    minuscules = 'abcdefghijklmnopqrstuvwxyz'
    for caractere in mot:
        if caractere not in minuscules: return False
    return True


def tab_uniquement_minuscules(tab):
    """
    tab -- liste de chaînes
    renvoie True si chaque élément de tab est uniquement constitué
    de minuscules de l'alphabet. renvoie False sinon.
    >>> tab_uniquement_minuscules(['aHa', 'uhu'])
    False
    >>> tab_uniquement_minuscules(['aha', 'uhu'])
    True
    """
    for element in tab:
        if uniquement_minuscules(element):
            return False
    return True

import doctest
doctest.testmod()

