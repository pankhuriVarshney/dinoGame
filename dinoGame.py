import pygame
import random 
import sys

pygame.init()

screen=pygame.display.set_mode((1280, 720))
clock=pygame.time.Clock()
pygame.display.set_caption("Dino in Space")


global score, gravity, rockSpeed, cloudx, platformx, jumping, running, boot
score=0
startTime=0
cloudx=0
platformx=0
rockSpeed=5
jumping=False
running=True
gravity=0
boot=True
i=0


platform= pygame.image.load('assets/graphics/platform.png').convert_alpha()
platform=pygame.transform.scale(platform,(1280,720))
platformrect=platform.get_rect(bottomleft=(0,720))

background=pygame.image.load('assets/graphics/background.png').convert()
background=pygame.transform.scale(background,(1280,720))

cloud=pygame.image.load('assets/graphics/clouds.png').convert_alpha()
cloudrect=cloud.get_rect(topleft=(0,50))
cloud=pygame.transform.scale(cloud,(1280,500))

star=pygame.image.load('assets/graphics/stars.png').convert_alpha()
starrect=star.get_rect(center=(1280, 350))
star=pygame.transform.scale(star,(1280,500))

font=pygame.font.Font('assets/font/Pixeltype.ttf', 50)
startfont=pygame.font.Font('assets/font/Pixeltype.ttf', 100)
endfont=pygame.font.Font('assets/font/Pixeltype.ttf', 150)

def Score():
    global score, gravity, rockSpeed
    score+=0.1
    if score%100==0:
        rockSpeed+=0.05
        gravity-=0.05
    text=font.render(str(int(score)),False, (255,0,0))
    textrect=text.get_rect(topleft=(1100,100))
    screen.blit(text, textrect )
    

class dino(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.x=xpos
        self.y=ypos
        self.running_sprites=[]
        self.running_sprites.append(pygame.transform.scale(pygame.image.load('assets/graphics/dino1.png'),(170,170)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load('assets/graphics/dino2.png'),(170,170)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load('assets/graphics/dino4.png'),(170,170)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load('assets/graphics/dinoD1.png'),(200,140)))
        self.running_sprites.append(pygame.transform.scale(pygame.image.load('assets/graphics/dinoD2.png'),(200,140)))
        self.current_image=0
        self.image=self.running_sprites[self.current_image]
        self.rect=self.image.get_rect(center=(xpos,ypos))
        self.ducking=False
        self.unduck=0

    def update(self):
        self.animate()
        if(running==False):
            self.end()

    def animate(self):
        if self.ducking:
            self.current_image+=1
            i=3
            j=5
            dinosaur.rect.centery=530
        else:
            i=0
            j=2
        self.current_image+=0.075
        if self.current_image>=j:
            self.current_image=i
        self.image=self.running_sprites[int(self.current_image)]
        if self.unduck>=100:
            self.unduck=0
            self.ducking=False
            dinosaur.rect.centery=500

    def end(self):
        self.image=self.running_sprites[2]

dino_group=pygame.sprite.GroupSingle()
dinosaur=dino(150,500)
dino_group.add(dinosaur)

obstacleindex=0
obstacle=[]
obstaclerect=[]
obstacle.append(pygame.transform.scale(pygame.image.load('assets/graphics/alien1.png').convert_alpha(),(110,110)))
obstaclerect.append(obstacle[0].get_rect(center=(1000,500)))
obstacle.append(pygame.transform.scale(pygame.image.load('assets/graphics/alien2.png').convert_alpha(),(130,130)))
obstaclerect.append(obstacle[1].get_rect(center=(1000,500)))
obstacle.append(pygame.transform.scale(pygame.image.load('assets/graphics/fire.png').convert_alpha(),(100,70)))
obstaclerect.append(obstacle[2].get_rect(center=(1000,400)))
obstacle.append(pygame.transform.scale(pygame.image.load('assets/graphics/fire.png').convert_alpha(),(120,90)))
obstaclerect.append(obstacle[3].get_rect(center=(1000,400)))


def menu():
    while True:
        
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()

        start=pygame.image.load('assets/graphics/start.png').convert_alpha()
        start=pygame.transform.scale(start, (1280,720))
        screen.blit(start, (0,0))

        stext=startfont.render("Press Return to Start Game", False, (255,0,0))
        stextrect=stext.get_rect(center=(640,650))
        screen.blit(stext,stextrect)

        keys_pressed=pygame.key.get_pressed()
        if(keys_pressed[pygame.K_RETURN]):
            menu2()
            menu3()
            return
        
        pygame.display.update()
        clock.tick(120)

def menu2():
    for x in range(120):        
        start=pygame.image.load('assets/graphics/start2.png').convert()
        start=pygame.transform.scale(start, (1280,720))
        screen.blit(start, (0,0))

        stext=startfont.render("Is there a Dino in Space?", False, (255,0,0))
        stextrect=stext.get_rect(center=(640,650))
        screen.blit(stext,stextrect)

        pygame.display.update()
        clock.tick(120)

def menu3():
    for x in range(120):
        start=pygame.image.load('assets/graphics/start3.png').convert()
        start=pygame.transform.scale(start, (1280,720))
        screen.blit(start, (0,0))

        stext=startfont.render("!!!!", False, (0,255,150))
        stextrect=stext.get_rect(center=(640,650))
        screen.blit(stext,stextrect)

        pygame.display.update()
        clock.tick(120)

while True:
    for event in pygame.event.get():
        if(event.type==(pygame.QUIT)):
            boot=True
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_UP or event.key==pygame.K_SPACE):
                jumping=True
                gravity=-15
            if(event.key==pygame.K_RETURN):
                running=True  
                score=0
            if(event.key==pygame.K_DOWN):
                dinosaur.ducking=True           
            
    if boot:
        menu()
        boot=False

    if running:
        screen.blit(background,(0,0))

        screen.blit(star,starrect)
        starrect.left-=2
        if(starrect.right<0):
            starrect.left=1280
            starrect.top=random.choice([50,100,150,200])
        
        cloudx-=1
        screen.blit(cloud, (cloudx,50))
        screen.blit(cloud, (cloudx+1280,50))
        if cloudx<=-1280:
            cloudx=0

        platformx-=5
        screen.blit(platform, (platformx,0))
        screen.blit(platform, (platformx+1280,0))
        if platformx<=-1280:
            platformx=0

        
        screen.blit(obstacle[i], obstaclerect[i])
        obstaclerect[i].left-=rockSpeed
        
        if(obstaclerect[i].right<0):
            if score>=50:
                i=random.choice([0,1,2,3])
            else:
                i=random.choice([0,1])
            obstaclerect[i].left=1280        
        
        if obstaclerect[i].colliderect(dinosaur.rect):
            print ("hit player")
            dinosaur.end()
            running = False
            obstaclerect[i].left = 1000
            dinosaur.rect.centery = 485
            rockSpeed=5
            dinosaur.ducking=False
            dinosaur.unduck=0

        if jumping:
            gravity+=0.3
            dinosaur.rect.centery+=gravity
            if(dinosaur.rect.centery>500):
                dinosaur.rect.centery=500

        if dinosaur.ducking:
            dinosaur.unduck+=1

        dino_group.update()
        dino_group.draw(screen)

        Score()

    else:
        score=str(int(score))
        text1=endfont.render("GameOver!", False, (255,0,0))
        textrect1=text1.get_rect(center=(640,300))
        screen.blit(text1, textrect1)
        text2=endfont.render("SCORE: "+score, False, (255,0,0))
        textrect2=text2.get_rect(center=(640,400))
        screen.blit(text2, textrect2)
        text1=font.render("Press Return to Start Again", False, (0,255,150))
        textrect1=text1.get_rect(center=(640,620))
        screen.blit(text1, textrect1)
        startTime=0
        jumping=False
        ducking=False

    pygame.display.update()
    clock.tick(120)

