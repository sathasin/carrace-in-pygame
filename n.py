import pygame
import random
file=open("high.txt","r+")
pygame.init()
w,l=500,700
s=pygame.display.set_mode((w,l))
run=True
road=pygame.image.load("road.PNG")
road=pygame.transform.scale(road,(w,l))
car=pygame.image.load("car.PNG")
car=pygame.transform.scale(car,(100,200))
font=pygame. font.SysFont("timesnewroman",30)
i=0
y=700
a=200
cars=["bus.PNG","lorry1.PNG"]
loc=[50,w-150,200]
score=0
speed=1
f=0
s2=font.render("",1,(255,255,255))
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_y:
                speed=1
                y=700
                score=0
                f=0
                s2=font.render("",1,(255,255,255))
            if e.key==pygame.K_UP:
                speed+=1
            if e.key==pygame.K_DOWN:
                speed-=1
                if speed<=0 and f==0:
                    speed=1
                    
    if y>=700:
        y=-200
        randcar=random.choice(cars)
        randloc=random.choice(loc)
        enemy=pygame.image.load(randcar)
        enemy=pygame.transform.scale(enemy,(100,200))
    enml=[x for x in range(a-100,a+110)]
    enml2=[x for x in range(300,700)]
    if randloc in enml and y in enml2:
        speed=0
        f=1
        s2=font.render(" press y to reset  ",1,(255,255,255))
    if speed!=0:
        score+=speed
        sa=str(score)
        s1=font.render("score : "+sa,1,(255,255,255))
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                run=False
        press=pygame.key.get_pressed()
        if press[pygame.K_LEFT]:
            a-=5
        if press[pygame.K_RIGHT]:
            a+=5
        if a<=0:
            a=0
        if a>=w-100:
            a=400
        s.blit(road,(0,i))
        s.blit(road,(0,i-700))
        s.blit(car,(a,500))
        s.blit(enemy,(randloc,y))
        if i>=l:
            i=0
        i=i+speed
        y+=speed*2
    s.blit(s1,(0,0))
    s.blit(s2,(0,40))
    pygame.display.update()
pygame.quit()
