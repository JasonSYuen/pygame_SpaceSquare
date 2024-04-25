import pygame
import random


# pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 720))
pygame.display.set_caption("Space Squares")
clock = pygame.time.Clock()
running = True
dt = 0

block_movement = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

class Square(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self,x_move,y_move):
        self.rect.x += x_move
        self.rect.y += y_move
        if self.rect.x > 600:
            self.kill()
        if self.rect.y > 720:
            self.kill() 

        collide = self.rect.colliderect(playerRect)
        if collide:
            self.kill()
            global hp 
            hp = hp-1
        for bullet in BulletGroup:
            collideBullet = self.rect.colliderect(bullet)

            if collideBullet:
                self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        
        laser = pygame.image.load("laser2.png")
        laser2 = pygame.transform.scale(laser,(40,120))
        self.image = laser2
        self.rect = self.image.get_rect()
        print(self.rect)
        #self.rect.width -= 10
        
        self.rect.center = (x,y)
        print(self.rect)
    def update(self):
        self.rect.y -= 20

        if self.rect.y < 0:
            self.kill()
        
      
timer = 0
bulletTimer =0

SpriteGroup = pygame.sprite.Group()
BulletGroup = pygame.sprite.Group()

heart = pygame.transform.scale(pygame.image.load("heart.png"),(75,75))

playerImg = pygame.transform.scale(pygame.image.load("SpaceShipSet1/spaceship1.png"),(50,50))
hp = 3

playerRect = playerImg.get_rect()

def gameloop():
    global hp
    global timer
    global dt
    global playerRect
    while hp > 0:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hp = 0

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        #player = pygame.draw.circle(screen, "red", player_pos, 10)
        #                                   
                        #screen , #color,            #x-pps #y-pos #width #height
        screen.blit(playerImg,(player_pos)) 
        
        
        playerRect = playerImg.get_rect()
        playerRect.height -= 8
        playerRect.topleft = (player_pos)

        

        #block_movement += 100 *dt

        
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_pos.y > 0:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s] and player_pos.y < 570:
            player_pos.y += 300 * dt
        if keys[pygame.K_a] and player_pos.x > 0:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d] and player_pos.x < 550:
            player_pos.x += 300 * dt

        

        global bulletTimer
        if keys[pygame.K_SPACE] and bulletTimer == 0:
            bulletTimer = 100
            bullet = Bullet(player_pos.x+23, player_pos.y)
            
            BulletGroup.add(bullet)
        if bulletTimer > 0:
            bulletTimer -= 1 

        color = "red"
        width = (100-bulletTimer) * 5
        if (bulletTimer == 0):
            color = "blue"
        pygame.draw.rect(screen, color, pygame.Rect(0,600 , width, 20))


        BulletGroup.draw(screen)
        BulletGroup.update()

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Score: " + str(timer),True,(0,255,0))  #(0,255,0) is RGB val of green
        textRect = text.get_rect()

        textRect.topleft = (0,0)

        screen.blit(text,textRect)

        #textRect.topleft = (0,100)
        #text2 = font.render(str(dt),True,(0,255,0))  #(0,255,0) is RGB val of green
        #screen.blit(text2,textRect)

        textRect.topleft = (0,560)
        if bulletTimer == 0:
            text3 = font.render("READY",True, (0,255,0))
        else:
            text3 = font.render("CHARGING",True, (0,255,0))
        
        screen.blit(text3,textRect)

        timer += 1
        if timer % 50 == 0:
            obj = Square("red", random.randint(25,575), 0)
            SpriteGroup.add(obj)

        if timer > 300 and timer % 40 == 0:
            obj = Square("blue", random.randint(25,575), 0)
            SpriteGroup.add(obj)

        if timer > 600 and timer % 30 == 0:
            obj = Square("yellow", random.randint(25,575), 0)
            SpriteGroup.add(obj)

        if timer > 1000 and timer % 20 == 0:
            obj = Square("green", random.randint(25,575), 0)
            SpriteGroup.add(obj)
        
        if timer > 1500 and timer % 10 == 0:
            obj = Square("black", random.randint(25,575), 0)
            SpriteGroup.add(obj)
        

        



            




        SpriteGroup.draw(screen)
        SpriteGroup.update(0,10)
        
        
        #pygame.draw.rect(screen, "blue", pygame.Rect(block_movement, 300,     20, 60))

        
        #image, coords of top left of image 

        pygame.draw.rect(screen, "gray",pygame.Rect(0, 620,  600, 100) )
        if hp >= 0:
            for x in range(hp):
                screen.blit(heart,(125+150*x,635)) 

    
        
        #pygame.time.set_timer = (event,millis) 
        
        # flip() the display to put your work on screen
        pygame.display.flip()


        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000


runningAll = True
startScreen = True
while startScreen:
    pygame.event.get()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            runningAll = False
            startScreen = False
            pygame.quit()

    screen.fill("black")

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render("Press Space To Start",True,(0,255,0))  #(0,255,0) is RGB val of green
    textRect = text.get_rect()
    textRect.center = (300,360)

    screen.blit(text,textRect)

    text = font.render("wasd to move",True,(0,255,0))  #(0,255,0) is RGB val of green
    textRect = text.get_rect()
    textRect.center = (300,460)
    screen.blit(text,textRect)
    text = font.render("space to shoot",True,(0,255,0))  #(0,255,0) is RGB val of green
    textRect = text.get_rect()
    textRect.center = (300,560)
    screen.blit(text,textRect)

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        startScreen = False

    pygame.display.flip()

while runningAll:
    gameloop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningAll = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                runningAll = False

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Game Over",True,(0,255,0))  #(0,255,0) is RGB val of green
        textRect = text.get_rect()
        textRect.center = (300,360)

        screen.blit(text,textRect)

        text = font.render("Play Again?",True,(0,255,0))  #(0,255,0) is RGB val of green
        textRect = text.get_rect()
        textRect.center = (400,460)

        screen.blit(text,textRect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if textRect.collidepoint(event.pos):
                    print("a")
                    print(running)
                    running = False


        pygame.display.flip()

    running = True
    hp = 3
    timer = 0
    SpriteGroup.empty()

    

pygame.quit()