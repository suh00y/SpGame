import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):
        #создаём пулю в пушки
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,5,12)
        self.color=39,177,77
        self.speed=4.5
        self.rect.centerx=gun.rect.centerx
        self.rect.top=gun.rect.top
        self.y=float(self.rect.y)

    def update(self):
        #перемещение пули по оси y
        self.y-=self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        #вывод пули на экран
        pygame.draw.rect(self.screen,self.color,self.rect)