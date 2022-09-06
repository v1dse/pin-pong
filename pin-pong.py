import pygame
import os
pygame.init()
 
back = (200, 255, 255) 
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
clock = pygame.time.Clock()


 
ROOTDIR = os.getcwd()

racket_x = 50
racket_y = 330
 
game_over = False

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color
    
    def color(self, new_color):
        self.fill_color = new_color
    
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
 
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
   
class Label (Area):
    def set_text(self, text, fsize = 12, text_color = (0,0,0)):
        self.txt = pygame.font.SysFont('verdana', 70).render(text, True, text_color)
    def draw(self, x_txt, y_txt):
        self.fill()
        mw.blit(self.txt, (self.rect.x + x_txt, self.rect.y + y_txt))

BALL = [os.path.join(ROOTDIR, 'modules/image/ball.png')]
PLATFORM = [os.path.join(ROOTDIR, 'modules/image/platform.png')]
BGM_SOUND = [os.path.join(ROOTDIR, 'modules/sound/ballandplatform.mp3')]
pop_right = False
pop_Left = False

dx = 3
dy = 3

while not game_over:
    BALL.fill()
    PLATFORM.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT:
                pop_right = False
            elif event.key == pygame.K_LEFT: 
                pop_Left = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT:
                pop_right = True
            elif event.key == pygame.K_LEFT: 
                pop_Left = True

    if pop_Left:
        PLATFORM.rect.x -= 3
    if pop_right:
        PLATFORM.rect.x += 3

    BALL.rect.x += dx
    BALL.rect.y += dy

    if BALL.rect.y < 0:
        dy *= -1
    if BALL.rect.x > 450 or BALL.rect.x < 0:
        dx *= -1

    if BALL.rect.colliderect(PLATFORM.rect):
         dy *= -1

    if BALL.rect.y > (PLATFORM.rect.y + 20):
        pop_text = Label(150,150,50,50,back)
        pop_text.set_text("YOU LOSE!", 50,(255,0,0))
        pop_text.draw(10,10)
        game_over = True

    pygame.display.update()
    clock.tick(40)
