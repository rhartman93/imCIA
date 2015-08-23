import pygame

gameObjects = []
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

class gameWindow(object):
    def __init__(self, width, height):
        #Setup Drawing Screen
        self.screen = pygame.display.set_mode((width, height))    
        
        
        
        
class gameObject(object):
    def __init__(self, screen, rect=None, pic=None):
        #If there is no pic there must be a rect
        
        self.screen = screen
        self.pic = pic
        if not self.pic:
            self.rect = rect
        else:
            self.pic = pygame.image.load(pic)
            self.rect = self.pic.get_rect()
        

class character(gameObject):
    def __init__(self, screen, rect=None, pic=None):
        gameObject.__init__(self, screen, rect=rect, pic=pic)
                            
    def draw(self):
        if not self.pic:
            pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            self.screen.screen.blit(self.pic, self.rect)

    def move(self, x, y):
        self.rect.move(x, y)
    

def main():
    #Initialize module
    pygame.init()

    game = gameWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

    #Are we in game?
    done = False

    #Define Objects
    gameObjects.append(character(game, pic="cia1.png"))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True #End the game

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gameObjects[0].move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    gameObjects[0].move(1, 0)
                if event.key == pygame.K_UP:
                    gameObjects[0].move(0, -1)
                if event.key == pygame.K_DOWN:
                    gameObjects[0].move(0, 1)

        #Draw loop
        game.screen.fill((0,0,0))
                       
        for obj in gameObjects:
            obj.draw()

        #Flip buffers
        pygame.display.flip()    
        
        
    

if __name__ == "__main__":
    main()
    
