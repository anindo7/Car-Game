import pygame
import time
import random

pygame.init()

#crash = pygame.mixer.Sound("crash.wav")
#pygame.mixer.music.load("music.wav")

display_width = 600
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
b_green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()

cari = pygame.image.load('car.png')
#default size of icon 32*32
pygame.display.set_icon(cari)
#pixAr = pygame.PixelArray(gameDisplay)
#pixAr[10][10]=blue
#pygame.draw.line(gameDisplay, green, (100,200),(300,500),5)
#pygame.draw.circle(gameDisplay, white, (50,50), 60)
#pygame.draw.polygon(gameDisplay, blue, ((50,50),(120,200),(300,140)))


def button(msg,r_x,r_y,w,h,c,a_c,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if r_x+w>mouse[0]>r_x and r_y+h>mouse[1]>r_y:
        if click[0] == 1 and action!=None:
            action()
        pygame.draw.rect(gameDisplay,a_c,[r_x,r_y,w,h])
    else:
        pygame.draw.rect(gameDisplay,c,[r_x,r_y,w,h])
    
    smallText = pygame.font.SysFont('comicsansms',20)
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center = (r_x+w/2,r_y+h/2)
    gameDisplay.blit(textSurf,textRect)
    

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        largeText = pygame.font.SysFont('comicsansms',100)
        textSurf, textRect = text_objects("Welcome",largeText)
        textRect.center = (display_width/2,display_height/2)
        gameDisplay.blit(textSurf,textRect)
        
        r_x = display_width*0.42
        r_y = display_height-100
        
        button("Go!!",r_x,r_y,100,50,green,b_green,gameloop)
        
        pygame.display.update()
        clock.tick(15)

def car(x,y):
    gameDisplay.blit(cari,(x,y))

def things(x,y,w,h,c):
    pygame.draw.rect(gameDisplay,c,[x,y,w,h])

def text_objects(text,font):
    textS = font.render(text,True,white)
    return textS,textS.get_rect()

def message(text):
    largeText = pygame.font.SysFont('comicsansms',100)
    textSurf, textRect = text_objects(text,largeText)
    textRect.center = (display_width/2,display_height/2)
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()


def crash():
    #pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(crash)
    message("You crashed")

def scoreboard(score):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(score),True,white)
    gameDisplay.blit(text, [0,0])

def gameloop():
    
    #pygame.mixer.music.Play(-1)
    x = (display_width*0.45)
    y = (display_height*0.8)
    x_change = 0
    
    thing_w = 100
    thing_h = 100
    thing_x = random.randrange(0,display_width-thing_w)
    thing_y = -600
    thing_s = 7
    
    car_x = 5
    carsize = 65
    crashed = False
    car_s = 5
    cou=0
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -car_s
                if event.key == pygame.K_RIGHT:
                    x_change = car_s
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            
            #print(event)
        x+=x_change
        #x_change=0
        gameDisplay.fill(black)
        things(thing_x,thing_y,thing_w,thing_h, green)
        thing_y+=thing_s
        
        car(x,y)
        scoreboard(cou)
        
        
        if x> display_width - carsize or x<0:
            crash()
        
        if thing_y>display_height:
            thing_y = -thing_h
            thing_x = random.randrange(0,display_width-thing_w)
            cou+=1
            thing_s+=0.5
            car_s+=0.1
        
        if y<thing_y+thing_h:
            if (x+car_x>thing_x and x+car_x<thing_x+thing_w) or (x+carsize>thing_x and x+carsize<thing_x+thing_w):
                crash()
        
        pygame.display.update()
        clock.tick(80)

game_intro()
#gameloop()

#quit()