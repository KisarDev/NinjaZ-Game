import pygame
import os

velocidade = 20

class Ninja(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 32, 32)
        self.x = x
        self.y = y
        self.velX = 0
        self.velY = 0
        self.animation_frames = []
        self.frame_index = 0
        self.correndo = False
        self.direcao = 1  # 1 para direita, -1 para esquerda
        self.atacando = False  # Adiciona uma variável para controlar o ataque
        self.load_animation()
        self.image = self.animation_frames[self.frame_index]
        self.rect.topleft = (x, y)
        self.elapsed = 0

    def load_animation(self):
        self.animation_frames = []  # Limpa as animações existentes
        if self.atacando:
            animation_folder = "assets/ninja/attack"
        elif self.correndo:
            animation_folder = "assets/ninja/run"
        else:
            animation_folder = "assets/ninja/idle"

        for filename in os.listdir(animation_folder):
            img = pygame.image.load(os.path.join(animation_folder, filename))
            self.animation_frames.append(img)

    def draw(self, win):
        pass  # Se precisar de uma função para desenhar, adicione aqui

    def update(self):
        if self.elapsed == 0 or pygame.time.get_ticks() - self.elapsed > 20:
            self.animate()
            self.elapsed = pygame.time.get_ticks()
        self.image = pygame.transform.flip(self.animation_frames[self.frame_index], self.direcao == -1, False)
        self.rect.topleft = (self.x, self.y)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.velX = -velocidade
            self.correndo = True
            self.direcao = -1  # Define a direção para a esquerda
        elif keys[pygame.K_RIGHT]:
            self.velX = velocidade
            self.correndo = True
            self.direcao = 1  # Define a direção para a direita
        else:
            self.velX = 0
            self.correndo = False

        if keys[pygame.K_UP]:
            self.velY = -velocidade
        elif keys[pygame.K_DOWN]:
            self.velY = velocidade
        else:
            self.velY = 0

        if keys[pygame.K_x]:
            self.atacando = True
        else:
            self.atacando = False

        self.x += self.velX
        self.y += self.velY

        self.load_animation()

    def animate(self):
        self.frame_index += 1
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
