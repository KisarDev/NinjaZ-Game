import pygame
from classes.ninja import Ninja

#Setup
pygame.init()
clock = pygame.time.Clock()

largura_janela = 1920
altura_janela = 1020
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Jogo de Ninja")

x = 500
y = 500


# Crie uma instância do ninja
ninja = Ninja(x, y)

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False
        

    # Limpe a tela
    janela.fill((0, 0, 0))


    # Atualize a posição do ninja
    ninja.update()

    # Desenhe o ninja na tela
    janela.blit(ninja.image, ninja.rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
