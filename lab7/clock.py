import pygame
import datetime


pygame.init()


screen_width=1000
screen_height=800
screen=pygame.display.set_mode((screen_width, screen_height))


minute_hand=pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\minute.png")
second_hand=pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\second.png")
clock_face=pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\main_body.png")
clock_face_position = (screen_width/2-clock_face.get_width()/2), (screen_height/2-clock_face.get_height()/2)
clock_center = (clock_face_position[0]+clock_face.get_width()/2, clock_face_position[1]+clock_face.get_height()/2)
while True:
    current_time = datetime.datetime.now()

    minute_angle = 90-((current_time.minute/60)*360)
    minute_hand_rotated = pygame.transform.rotate(minute_hand, minute_angle)
    second_angle = 90-((current_time.second/60)*360)
    second_hand_rotated = pygame.transform.rotate(second_hand, second_angle)

    screen.blit(clock_face, clock_face_position)
    screen.blit(minute_hand_rotated, (clock_center[0]-minute_hand_rotated.get_width()/2, clock_center[1]-minute_hand_rotated.get_height()/2))
    screen.blit(second_hand_rotated, (clock_center[0]-second_hand_rotated.get_width()/2, clock_center[1]-second_hand_rotated.get_height()/2))

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip()


