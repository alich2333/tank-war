import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)

    screen.fill("black")
    rect_list = [pygame.Rect(10*i, 10*i, 20, 20) for i in range(10)]
    rect = pygame.Rect(15,15,20,20)
    # print(rect.collidelistall(rect_list))
    for r in rect_list:
        pygame.draw.rect(screen, "red", r)
    pygame.draw.rect(screen, "blue", rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
