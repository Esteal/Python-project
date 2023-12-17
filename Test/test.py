les_mots_avec_accents = ['é', 'à', 'è']
les_mots_avec_voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
les_mots_avec_majuscules = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z']
les_mots_avec_chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
les_mots_avec_espaces = [' ']

def verifie_minuscules(chaine):
    for character in chaine:
        if character in les_mots_avec_accents or character in les_mots_avec_majuscules or character in les_mots_avec_chiffres or character in les_mots_avec_espaces:
            return False

    return True
    pass


def espacer(mot, intermediaire, n):
    nombre_de_boucle = 0
    nombre_de_character = len(mot)

    if verifie_minuscules(mot):
        variable_final = ""

        for character in mot:
            variable_final = variable_final + character

            if not nombre_de_boucle == nombre_de_character - 1:
                nombre_de_boucle = nombre_de_boucle + 1

                for _ in range(n):
                    variable_final = variable_final + intermediaire

        return variable_final
    else:
        return False

    pass

def double_voyelle(mot):
    nombre_de_boucle = 0
    nombre_de_character = len(mot)
    list_de_character_de_mot = list(mot)

    if verifie_minuscules(mot):
        variable_final = ""

        for character in mot:
            variable_final = variable_final + character

            if not nombre_de_boucle == nombre_de_character - 1:
                nombre_de_boucle = nombre_de_boucle + 1

                if character in les_mots_avec_voyelles:
                    if not (character == "e" and list_de_character_de_mot[nombre_de_boucle] == "n"):
                        variable_final = variable_final + character

        return variable_final
    else:
        return False

    pass


def substitue_o_ou(mot):
    nombre_de_boucle = 0
    nombre_de_character = len(mot)
    list_de_character_de_mot = list(mot)

    if verifie_minuscules(mot):
        variable_final = ""
        passer = False

        for character in mot:
            nombre_de_boucle = nombre_de_boucle + 1

            if character == "o":
                if not nombre_de_boucle == nombre_de_character:
                    if list_de_character_de_mot[nombre_de_boucle] == "u":
                        passer = True
                        variable_final = variable_final + character
                    else:
                        variable_final = variable_final + "ou"
                else:
                    variable_final = variable_final + "ou"
            else:
                if not passer:
                    variable_final = variable_final + character
                else:
                    passer = False

        return variable_final
    else:
        return False
    pass

print(verifie_minuscules('minuscule'))
print(verifie_minuscules('minus  cule'))
print(verifie_minuscules('Minuscule'))
print(verifie_minuscules('univers42'))
print(verifie_minuscules('àààééé'))

print(espacer('nsi', 'x', 2))
print(espacer('coucou', ' ', 1))
print(espacer('a', 'y', 2))
print(espacer('zou', 'ba', 3))

print(double_voyelle('enduire'))
print(double_voyelle('ordinateur'))
print(double_voyelle('nsi'))
print(double_voyelle('lenteur'))

print(substitue_o_ou('loup'))
print(substitue_o_ou('zozo'))
print(substitue_o_ou('bou'))
print(substitue_o_ou('oo'))
print(substitue_o_ou('ouou'))
print(substitue_o_ou('ououo'))
print(substitue_o_ou('uoou'))