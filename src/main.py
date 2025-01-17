import pygame
from game import Game
pygame.init()
game=Game(20,10)
pygame.mixer.init()
screen=pygame.display.set_mode((450,750))
clock = pygame.time.Clock()
font = pygame.font.Font("../materials/joystix_monospace.otf",15)
ingame=False
run=True
GAMEUPDATE=pygame.USEREVENT
pygame.time.set_timer(GAMEUPDATE,200)
bg=pygame.image.load("../materials/pngwing.com.png")
walls=pygame.image.load("../materials/walls.png")
resize=pygame.transform.scale(bg,(280,190))
pygame.mixer.music.load("../materials/tetrisSoundtrack.ogg")
pygame.mixer.music.play(-1,0,0)
pygame.mixer.music.set_volume(1)
buttonposs=[(130,375,165,25),(130,405,165,25),(130,425,165,25)]
arrowpos=0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif not ingame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    arrowpos=(arrowpos+1)%3
                elif event.key == pygame.K_UP:
                    arrowpos=(arrowpos-1)%3
                elif event.key == pygame.K_RETURN:
                    if arrowpos == 2:
                        run=False
                    elif arrowpos == 0:
                        ingame = True
        elif ingame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    game.moveRight()
                elif event.key == pygame.K_DOWN:
                    game.moveDown()
                elif event.key == pygame.K_d:
                    game.rotateClockwise()
                elif event.key == pygame.K_a:
                    game.rotateAntiClockwise()
            if event.type == GAMEUPDATE:
                game.moveDown()
    # <-------------------------MAIN MENU ------------------------>
    if not ingame:
        screen.fill((65, 105, 225))
        screen.blit(resize,(75,180))
        button=pygame.draw.rect(screen,(252,251,244),pygame.Rect(buttonposs[arrowpos]))
        screen.blit(font.render("Main Menu",1,(252,251,244)),(155,305))
        for i in range(len(buttonposs)):
            color =  (65, 105, 225) if i!=arrowpos else (252,251,244)
            tcolor = (252,251,244) if i!=arrowpos else (65, 105, 225)
            pygame.draw.rect(screen,color,pygame.Rect(buttonposs[i]))
            buttonText =""
            if i==0:
                buttonText="Start New Game"
            elif i == 1:
                buttonText = "Settings"
            elif i == 2:
                buttonText = "Exit"
            textSurface = font.render(buttonText,1,tcolor)
            textRect = textSurface.get_rect(center=(buttonposs[i][0]+buttonposs[i][2]//2,buttonposs[i][1]+buttonposs[i][3]//2))
            screen.blit(textSurface,textRect)
    #<-------------------------END------------------------------->
    #<-------------------------GAME------------------------------>
    elif ingame:
        screen.fill((65, 105, 225))
        gameArea=pygame.draw.rect(screen,(65, 105, 225),pygame.Rect(20,10,300,600))
        game.draw(screen)
        screen.blit(pygame.transform.scale(walls,(20,600)),(0,10))
        screen.blit(pygame.transform.scale(walls,(20,600)),(320,10))
    #<-------------------------END------------------------------>
    pygame.display.update()
    clock.tick(60)
pygame.quit()
