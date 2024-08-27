import pygame

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH , HEIGHT))
# for line
start = (50 , 50)
end = (250 , 50)

# for circle
pos = ( 300 , 100)
radius = 100

screen.fill((255,255,255))
pygame.display.update()

running = True

while running == True:
    # to draw a line
    pygame.draw.line(screen , (0,0,0) , start , end )
    
    # to draw a circle
    pygame.draw.circle(screen , (70,20,30) , pos , radius)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()



    
