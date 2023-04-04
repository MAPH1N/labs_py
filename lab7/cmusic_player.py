import pygame
import os
pygame.init()
pygame.mixer.init
screen=pygame.display.set_mode((500,400))
done=False


musiccc=r'C:\Users\sarda\Desktop\labs_py\lab7\musiccc'
music_files=os.listdir(musiccc)
music_files=[os.path.join(musiccc,file) for file in music_files if file.endswith(".mp3")]

current=0
pygame.mixer.music.load(music_files[current])
song_number=len(music_files)
pause=True


while not done:
    for event in pygame.event.get():
        pressed=pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
        if pressed[pygame.K_UP]:
            current=(current-1)%song_number
            pygame.mixer.music.load(music_files[current])
            pygame.mixer.music.play()
        if pressed[pygame.K_DOWN]:
            current=(current+1)%song_number
            pygame.mixer.music.load(music_files[current])
            pygame.mixer.music.play()
        if pressed[pygame.K_LEFT] and pause:
            pygame.mixer.music.play()
            pause=False
        elif pressed[pygame.K_LEFT] and not pause:
            pygame.mixer.music.stop()
            pause=True

        
        
    
    
