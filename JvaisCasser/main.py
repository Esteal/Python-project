import pygame
import math
from game import Game
pygame.init()

#definir une clock
clock= pygame.time.Clock()
FPS = 120


#générer la fenêtre
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1800, 720))

#charger l'arrière plan du jeu
background = pygame.image.load("assets/bg.jpg")

#importer la bannière
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x  =  math.ceil(screen.get_width() / 3)

#importer le bouton pour start la game
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.7)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#charger notre jeu
game = Game()

running = True

#Boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    #vérifier si le jeu a commencé ou non
    if game.is_playing:
        #declencher les instructions de la partie
        game.update(screen)
    #vérifier si le jeu n'a pas commencé
    else:
        #ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    #mettre à jour l'ecran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #si l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenché pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancé
                    game.start()
                    # jouer le son
                    game.sound_manager.play("click")

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.start()
                #jouer le son
                game.sound_manager.play("click")
    #fixer le nombre de fps sur ma clock
    clock.tick(120)
