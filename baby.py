import pygame


#Loading picture of baby from game folder and resizing
baby_image = pygame.image.load('/Users/alexbruno/Desktop/Baby Reveal Game/baby.png')
resized_baby = pygame.transform.scale(baby_image, (75,75))

class Baby(pygame.sprite.Sprite):
    """Class to create baby as a Sprite"""
    def __init__(self, x, y):
        """Initialize attributes and settings"""
        super().__init__()
        self.image = resized_baby
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 1.5
        self.right_moving = 2
   
    def update(self):
        """Keeps the baby always moving right at desired speed"""
        self.rect.x += self.right_moving
    
    def move_up(self):
        """Move up and down controls for next two methods"""
        if self.rect.y > 0:
            self.rect.y -= self.velocity

    def move_down(self):
        if self.rect.y < 450:
            self.rect.y += self.velocity