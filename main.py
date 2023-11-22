import pygame
from classes.ninja import Ninja
from classes.plataform import Platform

GRAVITY = 0.5
JUMP_VELOCITY = -10
FRICTION = 0.9
ACCELERATION = 0.5

# Setup
pygame.init()
clock = pygame.time.Clock()

largura_janela = 1920
altura_janela = 1020
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo de Ninja")

x = 500
y = 500

# Create ninja and platform sprites
ninja = Ninja(200, 798)
ninja_group = pygame.sprite.Group()
ninja_group.add(ninja)

platform = Platform(0, 800, 1920, 100)  # Ajustei a altura da plataforma
platform_group = pygame.sprite.Group()
platform_group.add(platform)

ninja_movement = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and ninja.rect.colliderect(platform.rect):  # Verifica a colisão antes de permitir o pulo
                ninja.y_velocity = JUMP_VELOCITY
            elif event.key == pygame.K_LEFT:
                ninja_movement = -1
            elif event.key == pygame.K_RIGHT:
                ninja_movement = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                ninja_movement = 0
                
    ninja.x_velocity += ninja_movement * ACCELERATION
    ninja_group.update(platform_group)  # Agora, passa o grupo da plataforma para o método update
    janela.fill((255, 255, 255))
    ninja_group.draw(janela)
    platform_group.draw(janela)

    # Dentro do loop principal
    collided_sprites = pygame.sprite.spritecollide(ninja, platform_group, False)
    if collided_sprites:
        ninja.y_velocity = 0
        ninja.rect.y = collided_sprites[0].rect.top  # Ajusta a posição para o topo da plataforma


    if ninja.rect.colliderect(platform.rect):  # Verifica colisão ao desenhar para ajustar a posição
        ninja.y_velocity = 0
        ninja.rect.y = platform.rect.y - ninja.rect.height

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
