import pygame

#la classe du projectile du joueur
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #faire tourner le projectile
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        #vérifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_colision(self, self.player.game.all_monsters):
            #supp le projectile
            self.remove()
            #infliger des dégâts
            monster.damage(self.player.attack)

        #vérifier si le projectile n'est plus sur l'écran
        if self.rect.x > 1800:
            #supprimer le projectile
            self.remove()
            print("supp")
