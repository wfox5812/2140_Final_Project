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
        self.direction = 270


    def update_tank(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.centerx > 15:
            dx -= 2
        if key[pygame.K_RIGHT] and self.rect.centerx < 780:
            dx += 2
        if key[pygame.K_UP] and self.rect.centery > 17:
            dy -= 2
        if key[pygame.K_DOWN] and self.rect.centery < 783:
            dy += 2
    
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.centerx < 790 and self.rect.centerx > 10:
            dx = 0
        if self.rect.centery > 790 or self.rect.centery < 10:
            dy = 0

        screen.blit(self.image, self.rect)
    
    def rotate_tank(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.direction != 180:
            if self.direction == 0:
                self.image = pygame.transform.rotate(self.image, 180)
            if self.direction == 90:
                self.image = pygame.transform.rotate(self.image, 90)
            if self.direction == 270:
                self.image = pygame.transform.rotate(self.image, -90)
            self.direction = 180
        if key[pygame.K_RIGHT] and self.direction != 0:
            if self.direction == 90:
                self.image = pygame.transform.rotate(self.image, -90)
            if self.direction == 180:
                self.image = pygame.transform.rotate(self.image, -180)
            if self.direction == 270:
                self.image = pygame.transform.rotate(self.image, -270)
            self.direction = 0
        if key[pygame.K_UP] and self.direction != 90:
            if self.direction == 0:
                self.image = pygame.transform.rotate(self.image, 90)
            if self.direction == 180:
                self.image = pygame.transform.rotate(self.image, -90)
            if self.direction == 270:
                self.image = pygame.transform.rotate(self.image, -180)
            self.direction = 90
        if key[pygame.K_DOWN] and self.direction != 270:
            if self.direction == 0:
                self.image = pygame.transform.rotate(self.image, 270)
            if self.direction == 90:
                self.image = pygame.transform.rotate(self.image, 180)
            if self.direction == 180:
                self.image = pygame.transform.rotate(self.image, 90)
            self.direction = 270

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

    def __init__(self, owner_tank, wall1):
        img = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(img, (5, 20)) 
        self.state = 'ready'
        self.owner_tank = owner_tank
        self.rect = self.image.get_rect()
        self.rect.x = self.owner_tank.rect.centerx
        self.rect.y = self.owner_tank.rect.centery
        self.direction = self.owner_tank.direction
        self.orientation = 90
        self.wall1 = wall1

    def update_bullet(self, wall_hit):
        dy = 10
        dx = 10
        key = pygame.key.get_pressed()

        #if space bar pressed
        if key[pygame.K_SPACE]:
            self.state = 'fired'
            self.direction = self.owner_tank.direction
        
        #if bullet is waiting to be fired
        if (self.state == 'ready'):
            self.rect.x = self.owner_tank.rect.centerx
            self.rect.y = self.owner_tank.rect.centery
            if self.owner_tank.direction == 0:
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, -90)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, -180)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -270)
                self.orientation = 0
            if self.owner_tank.direction == 90:
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, -90)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -180)
                self.orientation = 90
            if self.owner_tank.direction == 180:
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 180)
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -90)
                self.orientation = 180
            if self.owner_tank.direction == 270:
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, 180)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 270)
                self.orientation = 270

        #if bullet is fired
        if (self.state == 'fired'):
            #set bullet orientation
            if self.direction == 0:
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, -90)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, -180)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -270)
                self.orientation = 0
            if self.direction == 90:
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, -90)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -180)
                self.orientation = 90
            if self.direction == 180:
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 180)
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 270:
                    self.image = pygame.transform.rotate(self.image, -90)
                self.orientation = 180
            if self.direction == 270:
                if self.orientation == 90:
                    self.image = pygame.transform.rotate(self.image, 180)
                if self.orientation == 180:
                    self.image = pygame.transform.rotate(self.image, 90)
                if self.orientation == 0:
                    self.image = pygame.transform.rotate(self.image, 270)
                self.orientation = 270
            #determines direction bullet will shoot
            if self.direction == 0: 
                self.rect.x += dx
            if self.direction == 90:
                self.rect.y -= dy
            if self.direction == 180:
                self.rect.x -= dx
            if self.direction == 270:
                self.rect.y += dy
        
        #if bullet hits the edge of the screen
        if (self.rect.x < 0) or (self.rect.x > 800) or (self.rect.y < 0) or (self.rect.y > 800):
            self.state = 'ready'
            self.rect.x = self.owner_tank.rect.x
            self.rect.y = self.owner_tank.rect.y

        #if bullet hits a wall
        if wall_hit == True:
            self.state = 'ready'
            self.rect.x = self.owner_tank.rect.x
            self.rect.y = self.owner_tank.rect.y
            '''
        for i in range(len(self.walls)):
            current_rect = self.walls[i].wall_rect
            collide = pygame.Rect.colliderect(current_rect, self.rect)
            if collide == True:
                self.state = 'ready'
                self.rect.x = self.owner_tank.rect.x
                self.rect.y = self.owner_tank.rect.y
                pass
                    '''
        #update screen
        screen.blit(self.image, self.rect)

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
        img = pygame.image.load('Wall.jpg')
        self.surface = pygame.transform.scale(img,(x_length, y_length))
        self.rect = self.surface.get_rect()

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

walls_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
                wall11, wall12, wall13, wall14, wall15]

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

bg_img = pygame.image.load('Background.png')
bg_img = pygame.transform.scale(bg_img,(800,800))

#create players tank
player_one = Tank(385, 383)

#create player tank bullet
player_one_bullet = Projectile(player_one, wall1)

#add caption to the game window
pygame.display.set_caption("Tank Game")

#run condition
run = True

#GAME LOOP
while run:
    #set background
    screen.blit(bg_img, (0,0))

    #check for collisions
    bullet_collision = pygame.Rect.colliderect(wall1.rect, player_one_bullet.rect)
    print(bullet_collision)

    #update tank
    player_one.update_tank()

    #rotate tank
    player_one.rotate_tank()

    #update player 1 bullet
    player_one_bullet.update_bullet(bullet_collision)

    #draw walls
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










































































