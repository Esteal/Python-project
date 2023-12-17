from player import  Player
from monster import Monster, Mummy
from monster import Monster, Alien
from comet_event import  CometFallEvent
import  pygame


from sound import SoundManager

#creer une classe qui represente le jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        #generer le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #generer l'evenement
        self.comet_event = CometFallEvent(self)
        #gérer le son
        self.sound_manager = SoundManager()
        #grp de monstre
        self.all_monsters = pygame.sprite.Group()
        #mettre le score à 0
        self.font = pygame.font.Font("assets/fontcustom.ttf", 25)
        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre full vie et l'écran d'accueil
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play("game_over")

    def update(self, screen):
        #afficher le score sur l'ecran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la vie du joueur
        self.player.update_heal_bar(screen)

        #actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation du joueur
        self.player.update_animation()

        # récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_heal_bar(screen)
            monster.update_animation()

        #recuperer les cometes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Aplliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Aplliquer l'ensemble des images de mon groupe de monster
        self.all_monsters.draw(screen)

        #appliquer l'ensemble  des images de mon groupe de cometes
        self.comet_event.all_comets.draw(screen)

        # vérifier si le joueur va à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -35:
            self.player.move_left()

    def check_colision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))