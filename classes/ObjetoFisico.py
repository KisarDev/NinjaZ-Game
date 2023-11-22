import pygame

class ObjetoFisico(pygame.sprite.Sprite):
    def __init__(self, x, y, tamanho, massa, espaco, imagem_path):
        super().__init__()
        self.image = pygame.image.load(imagem_path)
        self.image = pygame.transform.scale(self.image, tamanho)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.body.position = (x, y)
        
        espaco.add(self.body, self.shape)

    def update(self):
        self.rect.topleft = self.body.position

