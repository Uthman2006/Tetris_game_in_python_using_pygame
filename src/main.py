import pygame
from game import Game
pygame.init()
pygame.mixer.init()
bgmusic_volume=1
bgmusic=pygame.mixer.Sound("../materials/tetrisSoundtrack.ogg")
bgmusic.set_volume(bgmusic_volume)
bgmusic.play(loops=-1)
game=Game(20,10)
screen=pygame.display.set_mode((450,750))
clock = pygame.time.Clock()
font = pygame.font.Font("../materials/joystix_monospace.otf",15)
insettings=False
ingame=False
run=True
pygame.display.set_caption("Tetris")
GAMEUPDATE=pygame.USEREVENT # this variable is used to save the event that is user created. In this case it is the updating the game. without this variable game moves fast.
pygame.time.set_timer(GAMEUPDATE,200)
bg=pygame.image.load("../materials/pngwing.com.png")
walls=pygame.image.load("../materials/walls.png")
resize=pygame.transform.scale(bg,(280,190))
buttonposs=[(130,375,165,25),(130,405,165,25),(130,425,165,25)]
settingsarrowpos=0
gameOverArrow=0
arrowpos=0
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif not ingame and not insettings:
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
                        insettings=False
                    elif arrowpos == 1:
                        ingame=False
                        insettings=True
        elif ingame and not insettings:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not game.game_over:
                    game.moveLeft()
                elif event.key == pygame.K_RIGHT and not game.game_over:
                    game.moveRight()
                elif event.key == pygame.K_DOWN and not game.game_over:
                    game.moveDown()
                    game.update_score(0,1)
                elif event.key == pygame.K_d and not game.game_over:
                    game.rotateClockwise()
                elif event.key == pygame.K_a and not game.game_over:
                    game.rotateAntiClockwise()
                elif event.key == pygame.K_RIGHT and game.game_over:
                    gameOverArrow=(gameOverArrow+1)%2
                elif event.key == pygame.K_LEFT and game.game_over:
                    gameOverArrow=(gameOverArrow-1)%2
                elif event.key == pygame.K_RETURN:
                    if gameOverArrow == 1:
                        ingame = False
                        game.reset()
                    elif gameOverArrow == 0:
                        game.reset()
                    bgmusic.play(loops=-1)
            if event.type == GAMEUPDATE and not game.game_over:
                game.moveDown()
        elif insettings and not ingame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    settingsarrowpos=(settingsarrowpos+1)%3
                elif event.key == pygame.K_UP:
                    settingsarrowpos=(settingsarrowpos-1)%3
                elif settingsarrowpos == 2 and event.key == pygame.K_RETURN:
                    ingame=False
                    insettings=False
                elif settingsarrowpos == 0:
                    if event.key == pygame.K_m:
                        bgmusic_volume = 0 if bgmusic_volume else 1
                    elif event.key == pygame.K_LEFT:
                        bgmusic_volume = 0 if (bgmusic_volume-0.1<=0) else (bgmusic_volume-0.1)
                    elif event.key == pygame.K_RIGHT:
                        bgmusic_volume = 1 if (bgmusic_volume+0.1>=1) else (bgmusic_volume+0.1)
                    bgmusic.set_volume(bgmusic_volume)
                elif settingsarrowpos == 1:
                    if event.key == pygame.K_m:
                        game.sound_effect_volume=0 if game.sound_effect_volume else 1
                    elif event.key == pygame.K_LEFT:
                        game.sound_effect_volume = 0 if (game.sound_effect_volume-0.1<=0) else (game.sound_effect_volume-0.1)
                    elif event.key == pygame.K_RIGHT:
                        game.sound_effect_volume = 1 if (game.sound_effect_volume+0.1>=1) else (game.sound_effect_volume+0.1)
    # <-------------------------MAIN MENU ------------------------>
    if not ingame and not insettings:
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
    elif ingame and not insettings:
        screen.fill((65, 105, 225))
        gameArea=pygame.draw.rect(screen,(65, 105, 225),pygame.Rect(20,10,300,600))
        pygame.draw.rect(screen,(26,31,40),pygame.Rect(150,613,140,120))
        game.draw(screen)
        screen.blit(pygame.transform.scale(walls,(20,600)),(0,10))
        screen.blit(pygame.transform.scale(walls,(20,600)),(320,10))
        screen.blit(font.render("Score",1,(252,251,244)),(360,10))
        screen.blit(font.render(f"{game.score:03d}",1,(252,251,244)),(370,30))
        screen.blit(font.render("Next Block",1,(252,251,244)),(160,610))
        if game.game_over:
            bgmusic.stop()
            pygame.draw.rect(screen,(252,251,244),pygame.Rect(25,250,400,200))
            pygame.draw.rect(screen,(65, 105, 225),pygame.Rect(35,260,380,180))
            screen.blit(pygame.transform.scale(font.render("Game Over",1,"red"),(200,50)),(120,280))
            pygame.draw.rect(screen,(65, 105, 225) if gameOverArrow != 0 else (252,251,244),pygame.Rect(40,350,100,20))
            screen.blit(font.render("Restart",1,(252,251,244) if gameOverArrow!=0 else (65, 105, 225)),(50,350))
            pygame.draw.rect(screen,(65, 105, 225) if gameOverArrow != 1 else (252,251,244),pygame.Rect(150,350,250,20))
            screen.blit(font.render("Back to Main Menu",1,(252,251,244) if gameOverArrow!=1 else (65, 105, 225)),(170,350))
    #<-------------------------END------------------------------>
    #<-------------------------SETTINGS------------------------------>
    elif insettings and not ingame:
        screen.fill((65, 105, 225))
        pygame.draw.rect(screen,(65, 105, 225) if settingsarrowpos!=0 else (252,251,244),pygame.Rect(30,250,400,20))
        pygame.draw.rect(screen,(252,251,244) if settingsarrowpos!=0 else (65, 105, 225),pygame.Rect(280,255,100*bgmusic_volume,10))
        screen.blit(font.render("Music Volume",1,(252,251,244) if settingsarrowpos!=0 else (65, 105, 225)),(70,250))
        pygame.draw.rect(screen,(65, 105, 225) if settingsarrowpos!=1 else (252,251,244),pygame.Rect(30,300,400,20))
        pygame.draw.rect(screen, (252,251,244) if settingsarrowpos!=1 else (65, 105, 225),pygame.Rect(280,305,100*game.sound_effect_volume,10))
        screen.blit(font.render("Sound Effect Volume",1,(252,251,244) if settingsarrowpos!=1 else (65, 105, 225)),(30,300))
        pygame.draw.rect(screen,(65, 105, 225) if settingsarrowpos!=2 else (252,251,244),pygame.Rect(30,350,400,20))
        screen.blit(font.render("Back To  Main Menu",1,(252,251,244) if settingsarrowpos!=2 else (65, 105, 225)),(90,350))
    pygame.display.update()
    clock.tick(60)
pygame.quit()