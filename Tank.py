import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()



#This is the game file for the game
class Tank:
    '''
    This class represents a single tank object and will be the parent class 
    '''
    def __init__(self, x_pos, y_pos):
        img = pygame.image.load('player_one.png')
        self.image = pygame.transform.scale(img, (30, 35))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


    def update_tank(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 2
        if key[pygame.K_RIGHT]:
            dx += 2
        if key[pygame.K_UP]:
            dy -= 2
        if key[pygame.K_DOWN]:
            dy += 2
    
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dx = 0
            dy = 0

        screen.blit(self.image, self.rect)
    
    def rotate_tank(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.image = pygame.transform.rotate(self.image, 90)
        if key[pygame.K_d]:
            self.image = pygame.transform.rotate(self.image, -90)


    def remove_heart(self):
        '''
        This function will remove one heart from the tank's health
        '''
        self.health -= 1
        pass

    def set_health(self, health_input):
        '''
        This function
        '''
        self.health = health_input
        pass
    
    def move(self, x_pos_input, y_pos_input):
        '''
        Takes in inputs from the arrow keys and moves the tank in either the x or y direction
        '''
        pass

    def shoot_projectile(self):
        '''
        Creates a projectile object and causes it to moves away from the tank object in the direction of self.direction with
        speed determined by self.fire_rate
        '''
        pass

    def set_direction(self, key_press):
        '''
        Sets self.direction of tank object to the direction of most recent arrow key press
        '''
        pass

class PlayerTank(Tank):
    '''
    Represents the player's tank
    '''
    def get_movement_key_press(self, direction_key_input):
        '''
        Gets a button press input from the arrow keys
        Input:
            direction_key_input
        '''
        pass

    def get_shoot_button_press(self, shoot_key_input):
        '''
        Gets button press input from designated button for firing
        Input:
            shoot_key_input
        '''

class EnemyTank(Tank):
    '''
    This is a class representing the enemy tank
    '''
    pass

    def set_fire_rate(self):
        '''
        Sets the fire rate of the tank
        (We want to make the tank fire at random in a specific interval)
        '''
        pass

    def set_direction(self):
        '''
        Sets the direction of the tank (probably will be patrol an area)
        '''

class Projectile:
    '''
    This is a class representing the a projectile
    '''
    pass

    def __init__(self, speed, direction, x_pos, y_pos, size):
        self.speed = speed
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size
   
    def set_direction(self, x_pos_input, y_pos_input):
        '''
        Sets the direction of the projectile
        '''
        pass

class Wall:
    '''
    This is a class representing a wall on the board
    '''
    pass
    def __init__(self, x_length, y_length):
        self.surface = pygame.image.load('Wall.jpg')
        self.surface = pygame.transform.scale(self.surface,(x_length, y_length))
        self.wall_rect = self.surface.get_rect()

#creating walls
wall1 = Wall(10,100)
wall2 = Wall(10,110)
wall3 = Wall(90,10)
wall4 = Wall(55,10)
wall5 = Wall(20,350)
wall6 = Wall(245,20)
wall7 = Wall(50,20)
wall8 = Wall(270,10)
wall9 = Wall(270,10)
wall10 = Wall(90,60)
wall11 = Wall(80,10)
wall12 = Wall(60,90)
wall13 = Wall(20,100)
wall14 = Wall(150,15)
wall15 = Wall(150,15)


screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

bg_img = pygame.image.load('Background.png')
bg_img = pygame.transform.scale(bg_img,(800,800))

#create players tank
player_one = Tank(100, 100)

#add caption to the game window
pygame.display.set_caption("Tank Game")

#run condition
run = True
#game loop
while run:
    #set background
    screen.blit(bg_img, (0,0))

    #update tank
    player_one.update_tank()

    #rotate tank
    player_one.rotate_tank()
    screen.blit(wall1.surface,(345,345))
    screen.blit(wall2.surface,(445,345))
    screen.blit(wall3.surface,(355,345))
    screen.blit(wall4.surface,(345,445))
    screen.blit(wall5.surface,(380,450))
    screen.blit(wall6.surface,(455,390))
    screen.blit(wall7.surface,(750,390))
    screen.blit(wall8.surface,(80,345))
    screen.blit(wall9.surface,(0,445))
    screen.blit(wall10.surface,(200,100))
    screen.blit(wall11.surface,(720,70))
    screen.blit(wall12.surface,(445,235))
    screen.blit(wall13.surface,(550,50))
    screen.blit(wall14.surface,(60,600))
    screen.blit(wall15.surface,(60,600))

    #quit condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()










































































