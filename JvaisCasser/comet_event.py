import pygame
from comet import Comet
#créer une classe pour gérer cet evenement


class CometFallEvent:
    #lors du chargement -> créer un compteur
    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 5

        #definir un groupe de sprite pour stockker nos cometes
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False


    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #une boucle pour les valeurs entre 1 et 10
        for i in range(1, 20):
            #apparaitre 1 bdf
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'evenement est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de cometes !")
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement

    def update_bar(self, surface):

        #ajouter du pourcentage à la barre
        self.add_percent()



        #barre noir en background
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #l'axe des x
            surface.get_height() - 20, #l'axe des y
            surface.get_width(), #longueur de la fenetre
            10 #epaisseur de la barre
        ])

        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #l'axe des x
            surface.get_height() - 20,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])
