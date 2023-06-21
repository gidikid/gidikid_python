import pygame

pygame.init()

colors ={
    "bg-color" : pygame.Color("#caf0f8"),
}    

window_width = 800
window_length = 600
window = pygame.display.set_mode((window_width, window_length))
pygame.display.set_caption("Drawing Shapes")

running =True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill(colors["bg-color"])
    
    pygame.draw.rect(window,  (255,0,0), pygame.Rect (50, 50 ,200, 100))
    
    pygame.draw.ciircle(window,  (0,255,0),(400, 300), 50)
    
    pygame.draw.line(window,  (0,0,255),(600, 100), (700, 200),5)
    
    pygame.display.update()
    
pygame.quit
    