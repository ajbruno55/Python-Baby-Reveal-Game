import pygame

# Load poop image from game folder and resize
image = pygame.image.load('/Users/alexbruno/Desktop/Baby Reveal Game/poop.png')
resized_image = pygame.transform.scale(image, (40,40))

class Poop(pygame.sprite.Sprite):
    """Create class for poop"""
    def __init__(self, x, y):
        """Initialize attributes"""
        super().__init__()
        self.image = resized_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def update(self):
        """move poop to the left at speed"""
        self.rect.x -= self.speed