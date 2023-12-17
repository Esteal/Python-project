import pygame
import random

from monster import Mummy, Alien


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 2)
        self.rect.x = random.randint(20, 1400)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play("meteorite")
        #verifier si le nbre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("La pluie est finie")
            #remettre la barre à 0
            self.comet_event.reset_percent()
            #apparaitre les 2 premiers monstre
            self.comet_event.game.start()
    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 525:
            print("sol")
            #retirer la bdf
            self.remove()




        #verifier si la bdf touche le joueur
        if self.comet_event.game.check_colision(
                self, self.comet_event.game.all_player
        ):
            print ("Joueur touché :")
            #retirer la bdf
            self.remove()

            #subir des dégats
            self.comet_event.game.player.damage(20)