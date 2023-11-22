import pygame
import os

GRAVITY = 0.5
JUMP_VELOCITY = -10
FRICTION = 0.9
ACCELERATION = 0.5

class Ninja(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animation_frames = []
        self.frame_index = 0
        self.image = pygame.image.load("assets/ninja/idle/Idle__000.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.x_velocity = 0
        self.y_velocity = 0
        self.correndo = False
        self.direcao = 1
        self.atacando = False
        self.elapsed = 0

    def load_animation(self):
        animation_folder = ""
        if self.atacando:
            animation_folder = "assets/ninja/attack"
        elif self.correndo:
            animation_folder = "assets/ninja/run"
        else:
            animation_folder = "assets/ninja/idle"

        self.animation_frames = []  # Limpa as animações existentes
        for filename in os.listdir(animation_folder):
            img = pygame.image.load(os.path.join(animation_folder, filename))
            self.animation_frames.append(img)

    def update(self, platform_group):
        if self.elapsed == 0 or pygame.time.get_ticks() - self.elapsed > 10:
            self.load_animation()
            self.elapsed = pygame.time.get_ticks()

        self.animate()  # Corrigindo aqui para chamar o método animate

        self.image = pygame.transform.flip(self.animation_frames[self.frame_index], self.direcao == -1, False)
        self.rect.topleft = (self.rect.x + self.x_velocity, self.rect.y + self.y_velocity)

        keys = pygame.key.get_pressed()

        self.y_velocity += GRAVITY
        self.x_velocity *= FRICTION

        if keys[pygame.K_LEFT]:
            self.x_velocity += -ACCELERATION
            self.correndo = True
            self.direcao = -1
        elif keys[pygame.K_RIGHT]:
            self.x_velocity += ACCELERATION
            self.correndo = True
            self.direcao = 1
        else:
            self.correndo = False

        if keys[pygame.K_x]:
            self.atacando = True
        else:
            self.atacando = False

    def animate(self):
        self.frame_index += 1
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
