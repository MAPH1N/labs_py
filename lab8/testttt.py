import pygame
pygame.init
second_hand=pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\second.png")
x,y=1000,500
x1,y1=546,140
screen= pygame.display.set_mode((x,y))
screen.fill((255,255,255))
done=False
'''

for x in range(360):
        second_hand_rotated=pygame.transform.rotate(second_hand, x)
        screen.blit(second_hand_rotated, (60,60))
        print(second_hand_rotated.get_width(),second_hand_rotated.get_height())

'''


while not done:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done= True
    second_hand_rotated=pygame.transform.rotate(second_hand, 50)
    screen.blit(second_hand_rotated, (60,60))
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(60,60,second_hand_rotated.get_width(),second_hand_rotated.get_height()))
    screen.blit(second_hand_rotated,(60,60))

    pygame.display.flip()

    

'''
second_hand_rotated1 = pygame.transform.rotate(second_hand, 0)
second_hand_rotated2 = pygame.transform.rotate(second_hand, 4)
second_hand_rotated3 = pygame.transform.rotate(second_hand, 8)
second_hand_rotated4 = pygame.transform.rotate(second_hand, 16)
second_hand_rotated5 = pygame.transform.rotate(second_hand, 32)
second_hand_rotated1 = pygame.transform.rotate(second_hand, 0)
screen.blit(second_hand_rotated1, (60,60))
    
    screen.blit(second_hand_rotated2, (60,60))
    #screen.blit(second_hand,(0,0))
    #screen.blit(second_hand,(546,140))
    
    screen.blit(second_hand_rotated3, (60,60))
    
    screen.blit(second_hand_rotated4, (60,60))

    screen.blit(second_hand_rotated5, (60,60))
'''
