import pygame

def load_image(path):
    img = pygame.image.load(path).convert()
    img.pygame.surface.set_colorkey((0, 0, 0))
    return img