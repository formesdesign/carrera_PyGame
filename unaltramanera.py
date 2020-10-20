import pygame
import sys

class Game():
    corredors = []
    __startLine = 20
    __finishLine = 600
    
    def __init__(self):
        #creen la pantalla de pygame en una tupla
        self.__screen = pygame.display.set_mode((640,480))
        #a la pantalla li fiquem un nom
        pygame.display.set_caption("Carrera loca")
        #imatge de fons
        self.bg = pygame.image.load("images/fons.png")
        
     #creu un atributo del corredor
        self.corredor = pygame.image.load("images/pilota.png")



    def competir(self):
        
        #cree una variable
        x = 0
        hihaGuanyador = False

        while not hihaGuanyador:
        #per pyGame creen la comprovació del eventos, sino no furula
        #get comprovaora tots els events des de l´última vegada que es va comprovar
            for event in pygame.event.get():
               #este event es el de surtida
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys, es la llibreria del sistema de python per fer la suritda
                    sys.exit()
      
            #rederitzar pantalla, li diem les cordenades
            self.__screen.blit(self.bg, (0,0))
            self.__screen.blit(self.corredor, (x,240))
            #libreria de paygame, per refrescar pantalla
            pygame.display.flip()
            
            x += 2
            if x >= 620:
               hihaGuanyador = True
               
        pygame.quit()
        sys.exit()

            

                

            
        
if __name__ == "__main__":
    #per pyGame i que inici bé, tenim que ficar el comando init de pygame
    pygame.init()
    game = Game()
    game.competir()
        
