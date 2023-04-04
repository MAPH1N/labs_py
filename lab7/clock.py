import pygame
import datetime

# Initialize Pygame
pygame.init()

# Set window size
window_width = 400
window_height = 400
window = pygame.display.set_mode((window_width, window_height))

# Load images of Mickey's hands
minute_hand = pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\minute.png")
second_hand = pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\second.png")

# Set the position of the clock face and calculate the center point
clock_face=pygame.image.load(r"C:\Users\sarda\Desktop\labs_py\lab7\main_body.png")
clock_face_position = (window_width/2 - clock_face.get_width()/2), (window_height/2 - clock_face.get_height()/2)
clock_center = (clock_face_position[0] + clock_face.get_width()/2, clock_face_position[1] + clock_face.get_height()/2)
while True:
    # Get the current time
    current_time = datetime.datetime.now()

    # Calculate the angle of the minute hand
    minute_angle = 90-((current_time.minute/60)*360)
    minute_hand_rotated = pygame.transform.rotate(minute_hand, minute_angle)

    # Calculate the angle of the second hand
    second_angle = 90-((current_time.second/60)*360)
    second_hand_rotated = pygame.transform.rotate(second_hand, second_angle)

    # Draw the clock face
    window.blit(clock_face, clock_face_position)

    # Draw the minute hand
    window.blit(minute_hand_rotated, (clock_center[0] - minute_hand_rotated.get_width()/2, clock_center[1] - minute_hand_rotated.get_height()/2))

    # Draw the second hand
    window.blit(second_hand_rotated, (clock_center[0] - second_hand_rotated.get_width()/2, clock_center[1] - second_hand_rotated.get_height()/2))

    # Update the display
    pygame.display.update()

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


