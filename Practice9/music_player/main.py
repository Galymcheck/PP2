import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 635, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 32)
def draw_progress_bar(screen, progress):
        x, y = 50, 250
        width, height = 500, 20

        pygame.draw.rect(screen, (100, 100, 100), (x, y, width, height))

        pygame.draw.rect(screen, (0, 200, 0), (x, y, width * progress, height))

playlist = [
    {"file": "C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice9/music_player/music/urbeat1.wav","title": "You are beautifil", "artist": "James Blunt"},
    {"file": "C:/Users/Galam/OneDrive/Документы/VScodes/repositories/PP2/Practice9/music_player/music/urbeat2.wav","title": "You are beautifil (Remix)", "artist": "Fredking"}
]

player = MusicPlayer(playlist)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False
    progress = player.get_progress()
    draw_progress_bar(screen, progress)   
    # Display current track
    track = player.get_current_track()

    text = font.render(
        f"{track['title']} - {track['artist']}",
        True,
        (255, 255, 255)
    )
    screen.blit(text, (10, 200))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()