from main import *
class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/ninja/idle_000.png")
        self.rect = self.image.get_rect()
        self.rect.center = (largura_janela // 2, altura_janela // 2)
