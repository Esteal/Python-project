import  pygame
from projectile import Projectile
import animation


#classe du joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_heal_bar(self, surface):
        #déssiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 10, self.max_health, 10])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 10, self.health, 10])


    def launch_projectile(self):
        #creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        #demarrer l'animation du lancer
        self.start_animation()
        #jouer le projectile
        self.game.sound_manager.play("tir")

    def move_right(self):

        #si le joueur n'est pas en collision
        if not self.game.check_colision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity