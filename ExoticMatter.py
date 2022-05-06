import random
import pygame
from sys import exit

screen_height = 800
screen_width = 1500
particleWidth = 10


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        directionNum = random.randint(0, 7)
        self.collision = 0
        self.direction = directionNum
        self.directionCount = random.randint(0, 75)
        self.image = pygame.Surface([particleWidth, particleWidth])
        
        colors = ['Blue', 'Red', 'White', 'Orange', 'Green', 'Purple', 'Grey', 'Pink']
        randomInt = random.randint(0, 7)
        self.colorName = colors[randomInt]
        self.image.fill(colors[randomInt])
        self.rect = self.image.get_rect()


        
  


def direction(num, move_amount):
    if num == 0:
        particle.rect.x += move_amount         
    elif num == 1:
        particle.rect.x -= move_amount    
    elif num == 2:
        particle.rect.y += move_amount     
    elif num == 3:
        particle.rect.y -= move_amount
    elif num == 4:
        particle.rect.x += move_amount
        particle.rect.y += move_amount
    elif num == 5:
        particle.rect.x -= move_amount
        particle.rect.y -= move_amount
    elif num == 6:
        particle.rect.x += move_amount
        particle.rect.y -= move_amount
    elif num == 7:
        particle.rect.x -= move_amount
        particle.rect.y += move_amount
    


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Exotic Matter')

field_surface = pygame.surface.Surface((1200, screen_height))
field_surface.fill('Black')

menu_surface = pygame.surface.Surface((300, screen_height))
menu_surface.fill('White')

font = pygame.font.Font(None, 37)
create_text = font.render('Create Particle', True, 'white', 'black')
create_rect = create_text.get_rect(topleft = (1250, 50))

particleGroup = pygame.sprite.Group()

particleCount = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and particleCount <= 250:
            for i in range(20):
                particle = Particle()
                ranX = random.randint(50, 1150)
                ranY = random.randint(50, screen_height - 50)
                particle.rect.x = ranX
                particle.rect.y = ranY
                
                particleGroup.add(particle)
               
                particleCount += 1
                
                

    
    
    for particle in particleGroup:
        
        if particle.directionCount < 200:
            direction(particle.direction, 1)
            particle.directionCount += 1
        else:
            particle.directionCount = random.randint(0, 90)
            particle.direction = random.randint(0, 7)
        
        
        
            
        if particle.rect.left < 0:
            particle.rect.right = 1200
        if particle.rect.right > 1200:
            particle.rect.left = 0
        if particle.rect.top < 0:
            particle.rect.bottom = screen_height
        if particle.rect.bottom > screen_height:
            particle.rect.top = 0
        
        for otherParticle in particleGroup:
            if otherParticle != particle:
                if particle.rect.colliderect(otherParticle.rect) and particle.collision == 0:
                    particle.collision += 1
                    ranNum = random.randint(0, 2)
                    if ranNum == 0:
                        otherParticle.kill()
                        particle.kill()
                        particleCount -= 2
                    else:
                        if particleCount <= 350:
                            newParticle = Particle()
                            particleDirection = [[particle.rect.x + 70, particle.rect.y - 40, 6], 
                            [particle.rect.x + 70, particle.rect.y + 40, 4],
                            [particle.rect.x + 70, particle.rect.y, 0]]
                            ranNum2 = random.randint(0, 2)
                            if ranNum2 == 0:
                                randomX = particleDirection[0][0]
                                randomY = particleDirection[0][1]
                                randomSpeed = particleDirection[0][2]
                            elif ranNum2 == 1:
                                randomX = particleDirection[1][0]
                                randomY = particleDirection[1][1]
                                randomSpeed = particleDirection[1][2]
                            elif ranNum2 == 2:
                                randomX = particleDirection[2][0]
                                randomY = particleDirection[2][1]
                                randomSpeed = particleDirection[2][2]
                            ranArr = [randomX, randomY, randomSpeed]
                            newParticle.rect.x = ranArr[0]
                            newParticle.rect.y = ranArr[1]
                            newParticle.direction = ranArr[2]
                            newParticle.collision += 1
                            
                            particleGroup.add(newParticle)
                            
                            particleCount += 1
                else:
                    particle.collision += 1
                if particle.collision == particleWidth - 1:
                    particle.collision = 0

    
                        

                    
    screen.blit(field_surface, (0,0))
    particleGroup.update()
    particleGroup.draw(screen)
    screen.blit(menu_surface, (1201, 0))
    screen.blit(create_text, create_rect)

 
    

    pygame.display.update()
    clock.tick(120)


