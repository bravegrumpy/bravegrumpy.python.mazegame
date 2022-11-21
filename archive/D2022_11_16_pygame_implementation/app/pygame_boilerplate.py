def run_pygame_window():
    import pygame
    pygame.init()
    canvas = pygame.display.set_mode((300,500))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                pygame.display.flip()
    pygame.quit()