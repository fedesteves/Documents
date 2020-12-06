import pygame
import numpy as np
import time


pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height,width))

bg = 25,25,25
screen.fill(bg)

nxC, nyC = 100,100
dimCW = width / nxC
dimCH = height / nyC

# celdas vivas =1, muertas =0
gameState = np.zeros((nxC,nyC))

# Creo el automata Gosper Glider Gun
posicionX,posicionY = 10,10
gameState[posicionX,posicionY+4]=1
gameState[posicionX,posicionY+4]=1
gameState[posicionX+1,posicionY+4]=1
gameState[posicionX+1,posicionY+5]=1

gameState[posicionX+10,posicionY+4]=1
gameState[posicionX+10,posicionY+5]=1
gameState[posicionX+10,posicionY+6]=1
gameState[posicionX+11,posicionY+3]=1
gameState[posicionX+11,posicionY+7]=1
gameState[posicionX+12,posicionY+2]=1
gameState[posicionX+12,posicionY+8]=1
gameState[posicionX+13,posicionY+2]=1
gameState[posicionX+13,posicionY+8]=1
gameState[posicionX+14,posicionY+5]=1
gameState[posicionX+15,posicionY+3]=1
gameState[posicionX+15,posicionY+7]=1
gameState[posicionX+16,posicionY+4]=1
gameState[posicionX+16,posicionY+5]=1
gameState[posicionX+16,posicionY+6]=1
gameState[posicionX+17,posicionY+5]=1

gameState[posicionX+20,posicionY+2]=1
gameState[posicionX+20,posicionY+3]=1
gameState[posicionX+20,posicionY+4]=1
gameState[posicionX+21,posicionY+2]=1
gameState[posicionX+21,posicionY+3]=1
gameState[posicionX+21,posicionY+4]=1
gameState[posicionX+22,posicionY+1]=1
gameState[posicionX+22,posicionY+5]=1
gameState[posicionX+24,posicionY]=1
gameState[posicionX+24,posicionY+1]=1
gameState[posicionX+24,posicionY+5]=1
gameState[posicionX+24,posicionY+6]=1

gameState[posicionX+34,posicionY+2]=1
gameState[posicionX+34,posicionY+3]=1
gameState[posicionX+35,posicionY+2]=1
gameState[posicionX+35,posicionY+3]=1


pauseExcept = False

while True:

    newGameState = np.copy(gameState)

    screen.fill(bg)
    
    
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExcept = not pauseExcept

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) >0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)) , int(np.floor(posY / dimCH))
            newGameState[celX,celY]= not mouseClick[2]


    
   
    for x in range(0,nxC):
        for y in range(0,nyC):
            if not pauseExcept:

                n_neigh =   gameState[(x-1) % nxC, (y-1) % nyC] + \
                            gameState[(x)   % nxC, (y-1) % nyC] + \
                            gameState[(x+1) % nxC, (y-1) % nyC] + \
                            gameState[(x-1) % nxC, (y)   % nyC] + \
                            gameState[(x+1) % nxC, (y)   % nyC] + \
                            gameState[(x-1) % nxC, (y+1) % nyC] + \
                            gameState[(x)   % nxC, (y+1) % nyC] + \
                            gameState[(x+1) % nxC, (y+1) % nyC]
                            
                # regla 1, celda muerta y con 3 vecinos vivos, entonces revive
                if gameState[x,y] == 0 and n_neigh == 3:
                    newGameState[x,y]=1
                # regla 2, celda viva con menos de 2 o mas de 3 vecinos vivos, entonces muere
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x,y]=0

            poly = [((x)*dimCW, y *dimCH),
                    ((x+1)*dimCW, y *dimCH),
                    ((x+1)*dimCW, (y+1) *dimCH),
                    ((x)*dimCW, (y+1) *dimCH)]

            if newGameState[x,y] ==0:
                pygame.draw.polygon(screen, (128,128,128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255,255,255), poly, 0)
            

    gameState = np.copy(newGameState)
    time.sleep(0.01)
    pygame.display.flip()
    