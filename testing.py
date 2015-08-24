import pygame

#Idea for text
#gameWindow will have a writer to write menus and such
#characters will have their own writers to write their speech relative to their location?

gameObjects = []
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

class gameWindow(object):
    def __init__(self, width, height):
        #Setup Drawing Screen
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont("monospace,arial", 15)

    def write(self, text):
        speech = self.font.render(text, 1, (255, 0, 0))
        self.screen.blit(speech, (WINDOW_WIDTH/2, 3 * ( WINDOW_HEIGHT / 4)))
        
        
        
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
        self.rect = self.rect.move(x, y)

def enterCharacter(character):
    pass

def main():
    #Initialize module
    pygame.init()

    game = gameWindow(WINDOW_WIDTH, WINDOW_HEIGHT)

    clock = pygame.time.Clock()

    #Are we in game?
    done = False

    #Define Objects
    gameObjects.append(character(game, pic="cia1.png"))

    #Using to queue cia slide in
    ciaEnter=False

    #Using to display text
    talking = False
    
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
                if event.key == pygame.K_SPACE:
                    ciaEnter = True

        #Character Entry
        #Problem should this be a class function somehow?
        #Thinking maybe have the boolean as a member
        #Then maybe modifying move or something
        #Can't have a loop in the member function because
        #it will hault the rest of the game

               
        if ciaEnter:
            if gameObjects[0].rect.centerx >= WINDOW_WIDTH/2:
                ciaEnter = False
                talking = True

            else:
                gameObjects[0].move(1, 0)

        #Draw loop
        game.screen.fill((0,0,0))
                       
        for obj in gameObjects:
            obj.draw()
            
        if talking:
            game.write("I'm CIA")

        #Flip buffers
        pygame.display.flip()
        
        #Maintain 60 FPS
        clock.tick(60)
        
        
    

if __name__ == "__main__":
    main()
    
