# avançar el corredor

import pygame
import sys
#per tindre tots el parametres de pygma fiquem aquesta formula
from pygame.locals import *
import random


class Corredor():
    __customes = ("C1", "C2", "C3", "C4")
    
    def __init__(self, x=0, y=0):       
        ixCustome = random.randint (0,3)
        
         #creu un atributo del corredor
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""

class Game():
    def __init__(self):
        #creen la pantalla de pygame en una tupla
        self.__screen = pygame.display.set_mode((640,480))
        #a la pantalla li fiquem un nom
        pygame.display.set_caption("Carrera loca")
        #imatge de fons
        self.bg = pygame.image.load("images/fons.png")
        
        self.corredor = Corredor(320,240)
        


    def start(self):
        
        #cree una variable
        hihaGuanyador = False

        while not hihaGuanyador:
        #per pyGame creen la comprovació del eventos, sino no furula
        #get comprovaora tots els events des de l´última vegada que es va comprovar
            for event in pygame.event.get():
               #este event es el de surtida
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP: #moure amunt el corredor
                        self.corredor.position[1] -= 5
                    elif event.key == K_DOWN:#moure cap a baix el corredor
                        self.corredor.position[1] += 5
                    elif event.key == K_LEFT:
                        self.corredor.position[0] -= 5
                    elif event.Key == K_RIGHT:
                        self.corredor.position[0] += 5
                    else:
                        pass
                            
            self.__screen.blit(self.bg, (0,0))
            self.__screen.blit(self.corredor.custome, self.corredor.position)
            
            pygame.display.flip()
            
            
            
if __name__ == "__main__":
    #per pyGame i que inici bé, tenim que ficar el comando init de pygame
    game = Game()
    pygame.font.init()
    game.start()
        


                    