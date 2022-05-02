from cmath import cos, sin
import math
from re import S, X
from tkinter import W
from turtle import distance, width
from xml.sax.handler import DTDHandler
import pygame

pygame.init()



WIDTH, HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
pygame.display.set_caption("Planetas")

class Planet():
    GRAVITY = 6.67 * 10**-11
    def __init__(self, x,y,dx,dy,radius,massa,color,timestep = 0):
        self.x = x
        self.y = y
        self.dy = dy
        self.dx = dx
        self.radius = radius
        self.massa = massa
        self.color = color
        self.timestep = timestep
        

    def draw(self,orbit = False): 
        pygame.draw.circle(WIN,self.color,(WIDTH/2 + self.x,HEIGHT/2 + self.y),self.radius)
        
            
        
    
       
    def move(self,other):
        GRAVITY = 6.2 * 10 ** -11
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        forceG = GRAVITY * other.massa * self.massa / distance ** 2
        theta = math.atan2(distance_y,distance_x)
        force_x = forceG * cos(theta)
        force_y = forceG * sin(theta)
        self.dx += force_x.real / self.massa * self.timestep
        self.dy += force_y.real /self.massa * self.timestep
        self.x += self.dx * self.timestep
        self.y += self.dy * self.timestep
        
            
            
       
        
       







def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet(0,0,0,1,30,1*10**11,WHITE)
    earth = Planet(200,0,0,1.5/10,10,5*10**6,(0,255,255),5)

    orbit = False
    while run:
        clock.tick(60)
        WIN.fill((0,0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        sun.draw()
        earth.draw()
        earth.move(sun)
    

        pygame.display.update()

    pygame.quit()
main()