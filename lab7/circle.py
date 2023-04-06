import pygame
pygame.init()
a,b=400,500
screen= pygame.display.set_mode((a,b))
done=False
screen.fill((255,255,255))
r=25
x=25
y=-150
clock = pygame.time.Clock()
pygame.draw.circle(screen, (255, 0, 0),(x,y),r)
while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
    screen.fill((255,255,255))
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>=r:
        y-=20 
        if y<20:y=r
    if pressed[pygame.K_DOWN]and y<=b-r: 
        y+=20
        if y>b-20:y=b-r
    if pressed[pygame.K_LEFT]and x>=r: 
        x-=20
        if x<20:x=r
    if pressed[pygame.K_RIGHT]and x<=a-r: 
        x+=20
        if x>a-20:x=a-r
    pygame.draw.circle(screen, (255, 0, 0),(x,y),r)


        
    pygame.display.flip()