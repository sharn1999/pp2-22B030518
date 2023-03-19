import pygame

pygame.init()

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

music_files = ["Killer_queen.mp3", "ShowMustGoOn.mp3", "WeWellRockYou.mp3"]
music_index = 0
pygame.mixer.music.load(music_files[music_index])


play_key = pygame.K_SPACE
stop_key = pygame.K_ESCAPE
next_key = pygame.K_RIGHT
prev_key = pygame.K_LEFT

pygame.mixer.music.play()
font = pygame.font.Font(None,36)
text = font.render(music_files[music_index], True,(180, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == play_key:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == stop_key:
                pygame.mixer.music.stop()
            elif event.key == next_key:
                music_index += 1
                if music_index >= len(music_files):
                    music_index = 0
                pygame.mixer.music.load(music_files[music_index])
                pygame.mixer.music.play()
                text = font.render(music_files[music_index], True,(180, 0, 0))
                screen.fill((0, 0, 0))
                screen.blit(text, (10, 50))

            elif event.key == prev_key:
                music_index -= 1
                if music_index < 0:
                    music_index = len(music_files)-1
                pygame.mixer.music.load(music_files[music_index])
                pygame.mixer.music.play()
                text = font.render(music_files[music_index], True,(180, 0, 0))
                screen.fill((0, 0, 0))
                screen.blit(text, (10, 50))
    pygame.display.update()
pygame.quit()