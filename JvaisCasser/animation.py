import pygame
import random

#classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    #définir les choses à faire à la création de l'tentité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 #commencer l'animation à l'image 0
        self.images = animation.get(sprite_name)
        self.animation = False

    #definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #definir une methode pour animer le sprite
    def animate(self, loop=False):

        #verifier si l'animation est active
        if self.animation:

            #passer à l'image suivante
            self.current_image += random.randint(0, 1)

            #verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remettre l'animation au départ
                self.current_image = 0

                #vérifié si l'animation n'est pas en mode boucle
                if loop is False:

                    #désactivation de l'animation
                    self.animation = False

            #modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

#définir un fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    #récupérer le chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenu de la liste d'image
    return images


#definir un dictionnaire qui va contenir les images chargées de chaque sprite
#mummy -> [...mummy1.png,...mummy2.png,...]
animation = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}