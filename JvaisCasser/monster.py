import pygame
import random
import animation

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.1
        self.rect = self.image.get_rect()
        self.rect.x = 1800 + random.randint(1, 300)
        self.rect.y = 540 - offset  # - déplace vers le haut et + vers le bas
        self.start_animation()
        self.loot_amount = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        #infliger des dégâts
        self.health -= amount

        #vérifier les hp, si égal à 0, il meurt
        if self.health <= 0:
            #Respawn comme un nouveau monstre
            self.rect.x = 1800 + random.randint(1, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            #ajouter le nombre de points
            self.game.add_score(self.loot_amount)

            #vérifier si la barre d'evenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la méthode pour déclencher la pluie de cometes
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_heal_bar(self, surface):
        #definir une couleur pour notre jauge de vie (vert clair)
        bar_color = (111, 210, 46)

        #définir une couleur pour l'arrière plan
        back_bar_color = (60, 63, 60)

        #d"finir la position de notre jauge de vie ainsi que sa largeur et épaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]

        #definir l'arrière plan de la barre
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        #déssiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)



    def forward(self):
        #uniquement si il n'y a pas de collision
        if not self.game.check_colision(self, self.game.all_player):
            self.rect.x -= self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des degats
            self.game.player.damage(self.attack)


#definir une classe pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

#definir une classe pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game,"alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_speed(1)
        self.attack = 0.8
        self.set_loot_amount(80)

