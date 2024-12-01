import pygame
import NPC

def Simulation():
    BLACK = (255, 255, 255)
    screenSize = [550,200]
    screen = pygame.display.set_mode(screenSize)
    BACKGROUND = pygame.image.load('BackGround.png')

    pygame.init()
    clock = pygame.time.Clock()
    spriteGroup = pygame.sprite.Group()
    human = NPC.Human("generic-sheet.png",2)
    zombie = NPC.Human("zombie-sheet.png",1)
    human.rect.x = 100
    zombie.rect.x = 120
    spriteGroup.add(human,zombie)
    font = pygame.font.Font(None, 24)
    text = font.render('Press Q to Quit', True, BLACK)

    while True:
        screen.blit(BACKGROUND, [0, 0])
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_q:
                    pygame.quit()
        human.wanderAround((0,0),screenSize)
        zombie.wanderAround((0,0),screenSize)
        
        spriteGroup.update()
        spriteGroup.draw(screen)
        screen.blit(text, [10, 10])
        clock.tick(60)
        pygame.display.update()
    pygame.quit()
Simulation()


