import pygame
import sys
import random

class Corredor():
    __customes = ("C1", "C2", "C3", "C4")
    
    def __init__(self, x=0, y=0):       
        ixCustome = random.randint (0,3)
        
         #creu un atributo del corredor
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x,y]
        self.name = ""
        
    def avanzar(self):
        #per moure el corredor
        self.position[0] += random.randint(1,6)
        


class Game():
    corredors = []
    __posY = (55,155,262,360)
    __names = ("fantasma", "pato", "cap", "peix")
    __startLine = 5
    __finishLine = 600
    
    def __init__(self):
        #creen la pantalla de pygame en una tupla
        self.__screen = pygame.display.set_mode((640,480))
        #a la pantalla li fiquem un nom
        pygame.display.set_caption("Carrera loca")
        #imatge de fons
        self.bg = pygame.image.load("images/fons.png")
        
        
        for i in range (4):
            elCorredor = Corredor(self.__startLine, self.__posY[i])
            elCorredor.name = self.__names[i]
            self.corredors.append(elCorredor)
            
    def close(self):     
        pygame.quit()
        #sys, es la llibreria del sistema de python per fer la suritda
        sys.exit()           
            

    def competir(self):
        
        #cree una variable
        hihaGuanyador = False

        while not hihaGuanyador:
        #per pyGame creen la comprovació del eventos, sino no furula
        #get comprovaora tots els events des de l´última vegada que es va comprovar
            for event in pygame.event.get():
               #este event es el de surtida
                if event.type == pygame.QUIT:
                    hihaGuanyador = True
                    
            for activeCorredor in self.corredors:
                activeCorredor.avanzar()
                if activeCorredor.position[0] >= self.__finishLine:
                    print("{} ha guanyat!".format(activeCorredor.name))
                    hihaGuanyador = True

            
            #rederitzar pantalla, li diem les cordenades
            self.__screen.blit(self.bg, (0,0))
 
            
            #fique als corredor  
            for corredor in self.corredors:
                self.__screen.blit(corredor.custome, corredor.position)


            #libreria de paygame, per refrescar pantalla
            pygame.display.flip()
            
            
        #este bluque es per tancar, i comporbar els evetns i que no es penje la pantalla    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
            
               
 
        
if __name__ == "__main__":
    #per pyGame i que inici bé, tenim que ficar el comando init de pygame
    pygame.init()
    game = Game()
    game.competir()
        

