import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    #вывод игровой информации
    def __init__(self,screen,stats):
        #инициализирум подсчёт очков
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stats=stats
        self.text_color=(39,177,77)
        self.font=pygame.font.SysFont('Comic Sans MS',29)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        #преобразовавывает текст счёта в графическом изрображение
        self.score_img=self.font.render(str(self.stats.score),True,self.text_color,(0,0,0))
        self.score_rect=self.score_img.get_rect()
        self.score_rect.right=self.screen_rect.right-40
        self.score_rect.top=20

    def image_guns(self):
        #кол-во жизней
        self.guns=Group()
        for gun_number in range(self.stats.guns_left):
            gun=Gun(self.screen)
            gun.rect.x=15+gun_number*gun.rect.width
            gun.rect.y=20
            self.guns.add(gun)

    def image_high_score(self):
        #преобразует рекорд в графическое изображение
        self.high_score_image=self.font.render(str(self.stats.hight_score),True,self.text_color,(0,0,0))
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top+20

    def show_score(self):
        #вывод счёта на экран
        self.screen.blit(self.score_img,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)


