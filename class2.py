
import pygame
pygame.init
window_width = 800
window_length = 600
window = pygame.display.set_mode((window_width, window_length))
pygame.display.set_caption("Moving Rectangle")

rect_x =100
rect_y =100

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] :
        rect_y -= .5
    if keys[pygame.K_DOWN]  :
        rect_y += .5
    if keys[pygame.K_LEFT] :
        rect_x -= .5
    if keys[pygame.K_RIGHT]:
        rect_y += .5
         
    window.fill((255, 255, 255))
    pygame.draw.rect(window,  (255,0,0), pygame.Rect (50, 50 ,200, 100))
    
    pygame.display.update()
    
pygame.quit
    
    
    
    


        
    
        
        
           
    




