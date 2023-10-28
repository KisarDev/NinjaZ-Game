import pygame
import os

class Ninja(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """ Carrega todos os atributos necessários"""
        super().__init__()
        self.animation_frames = []
        self.frame_index = 0
        self.load_animation()
        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.elapsed = 0

    def load_animation(self):
        """ Carrega todas as imagens das animações"""
        animation_folder = "assets/ninja/idle"
        for filename in os.listdir(animation_folder):
            img = pygame.image.load(os.path.join(animation_folder, filename))
            self.animation_frames.append(img)

    def update(self):
        """ Atualiza os frames da animação de forma independente do FPS do game"""
        if self.elapsed == 0 or pygame.time.get_ticks() - self.elapsed > 50: # Regula a velocidade da animação
            self.animate()
            self.elapsed = pygame.time.get_ticks()
        self.image = self.animation_frames[self.frame_index]

    def animate(self):
        self.frame_index += 1
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
