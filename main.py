# Module import start
import pygame, sys
import random
import point
# Module import end

def random_point(): # Generator for random coordinate x and y
    return (random.randint(1,screen_size[0]), random.randint(1,screen_size[1]))

screen_size = (1080,720)
primiary_pointSize = (10,10)
secondary_pointSize = (5,5)
random_list = ["A","B","C"]

started_point = random_point() # started chosen point 

A = point.Point(primiary_pointSize,random_point(),(255,0,0)) # point A
B = point.Point(primiary_pointSize,random_point(),(0,255,0)) # point B
C = point.Point(primiary_pointSize,random_point(),(0,0,255)) # point C

pygame.init()

pygame.display.set_caption("Chaos Game")
screen = pygame.display.set_mode(screen_size, 0, 32)

# Drawing point A,B and C on the screen
pygame.draw.rect(screen,A.get_color(),(A.get_point(),A.get_size()))
pygame.draw.rect(screen,B.get_color(),(B.get_point(),B.get_size()))
pygame.draw.rect(screen,C.get_color(),(C.get_point(),C.get_size()))

# Drawing first random point on the screen
pygame.draw.rect(screen,(255,255,255),(started_point,secondary_pointSize))

current_point = started_point # intialize the random points and floag with a variable

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    check_point = random.choice(random_list) # Chosing point between A,B and C

    if check_point == "A":
        current_point = A.mid_point(current_point)
        pygame.draw.rect(screen,A.get_color(),(current_point,secondary_pointSize))
    elif check_point == "B":
        current_point = B.mid_point(current_point)
        pygame.draw.rect(screen,B.get_color(),(current_point,secondary_pointSize))
    elif check_point == "C":
        current_point = C.mid_point(current_point)
        pygame.draw.rect(screen,C.get_color(),(current_point,secondary_pointSize))
 
    pygame.time.delay(300) # Delay for better visualization 
    pygame.display.update()