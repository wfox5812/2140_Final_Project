import sys
print(sys.executable)

import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

#This is the game file for the game
class Tank:
    '''
    This class represents a single tank object and will be the parent class
    '''
    def __init__(self, x_pos, y_pos, walls_list):
        img = pygame.image.load('player_one.png')
        self.image = pygame.transform.scale(img, (30, 35))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.direction = 270
        self.walls = walls_list


    def update_tank(self):
        dx = 0
        dy = 0
        self.left = 'yes'
        self.right = 'yes'
        self.up = 'yes'
        self.down = 'yes'

        #check for collisions with walls
        for i in range(len(self.walls)):
            if self.walls[i].rect.colliderect(self.rect):
                if self.direction == 0:
                    self.right = 'no'
                    self.rect.x -= 2
                if self.direction == 90:
                    self.up = 'no'
                    self.rect.y += 2
                if self.direction == 180:
                    self.left = 'no'
                    self.rect.x += 2
                if self.direction == 270:
                    self.down = 'no'
                    self.rect.y -= 2
                pass
        
        #check for collisions with other tanks
        for i in range(len(enemy_tanks_list)):
            if enemy_tanks_list[i].rect.colliderect(self.rect):
                if self.direction == 0:
                    self.right = 'no'
                    self.rect.x -= 2
                if self.direction == 90:
                    self.up = 'no'
                    self.rect.y += 2
                if self.direction == 180:
                    self.left = 'no'
                    self.rect.x += 2
                if self.direction == 270:
                    self.down = 'no'
                    self.rect.y -= 2
                pass

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.centerx > 15 and self.left != 'no':
            dx -= 2
        if key[pygame.K_RIGHT] and self.rect.centerx < 780 and self.right != 'no':
            dx += 2
        if key[pygame.K_UP] and self.rect.centery > 17 and self.up != 'no':
            dy -= 2
        if key[pygame.K_DOWN] and self.rect.centery < 783 and self.down != 'no':
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


class EnemyTank:
    '''
    This is a class representing the enemy tank
    '''

    def __init__(self, start_x, start_y, end_x, end_y, direction = 270):
        img = pygame.image.load('enemy_tank.png')
        self.image = pygame.transform.scale(img, (30, 35))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.recent_limit_x = self.start_x
        self.recent_limit_y = self.start_y
        if direction == 270:
            self.direction = 270
        elif direction == 180:
            self.direction = 180
            self.image = pygame.transform.rotate(self.image, -90)
        elif direction == 90:
            self.direction = 90
            self.image = pygame.transform.rotate(self.image, 180)
        elif direction == 0:
            self.direction = 0
            self.image = pygame.transform.rotate(self.image, 90)


    #def check_collision(self):

    def update_tank(self):
        dx = 1
        dy = 1

        screen.blit(self.image, self.rect)

        if self.recent_limit_x == self.start_x:
            self.rect.x += dx
            if self.rect.x == self.end_x:
                self.recent_limit_x = self.end_x
        
        if self.recent_limit_y == self.start_y:
            self.rect.y += dx
            if self.rect.y == self.end_y:
                self.recent_limit_y = self.end_y

        if self.recent_limit_x == self.end_x:
            self.rect.x -= dx
            if self.rect.x == self.start_x:
                self.recent_limit_x = self.start_x

        if self.recent_limit_y == self.end_y:
            self.rect.y -= dx
            if self.rect.y == self.start_y:
                self.recent_limit_y = self.start_y
        
        

    def set_fire_rate(self):
        '''
        Sets the fire rate of the tank
        (We want to make the tank fire at random in a specific interval)
        '''
        pass


class Projectile:
    '''
    This is a class representing the a projectile
    '''
    pass

    def __init__(self, owner_tank, walls_list, health = 3):
        self.health = health
        img = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(img, (5, 20))
        self.owner_tank = owner_tank
        self.rect = self.image.get_rect()
        self.rect.x = self.owner_tank.rect.centerx
        self.rect.y = self.owner_tank.rect.centery
        self.direction = self.owner_tank.direction
        self.orientation = 90
        self.walls = walls_list
        if self.owner_tank != player_one:
            self.state = 'fired'
            self.direction = self.owner_tank.direction
            self.rect.x = self.owner_tank.rect.centerx
            self.rect.y = self.owner_tank.rect.centery
            self.constant_shoot = True
        else:
            self.state = 'ready'
            self.constant_shoot = False
        #self.tanks = [tank for tank in self.tanks if not tank.remove_flag]


    def update_bullet(self):
        dy = 5
        dx = 5
        key = pygame.key.get_pressed()

        #if space bar pressed
        if self.owner_tank == player_one:
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
            if self.constant_shoot == True:
                self.state = 'fired'
            elif self.constant_shoot == False:
                self.state = 'ready'
            self.rect.x = self.owner_tank.rect.x
            self.rect.y = self.owner_tank.rect.y

        #if bullet hits a wall
        for i in range(len(self.walls)):
            if self.walls[i].rect.colliderect(self.rect):
                if self.constant_shoot == True:
                    self.state = 'fired'
                elif self.constant_shoot == False:
                    self.state = 'ready'
                self.rect.x = self.owner_tank.rect.x
                self.rect.y = self.owner_tank.rect.y
                pass
        
        #if bullet hits an enemy tank
        for i in range(len(enemy_tanks_list) - 1, -1, -1):
            if enemy_tanks_list[i].rect.colliderect(player_one_bullet.rect):
                self.state = 'ready'
                self.rect.x = self.owner_tank.rect.x
                self.rect.y = self.owner_tank.rect.y
                print('before removing from list')
                del enemy_tanks_list[i]
                del enemy_tank_bullets[i]
                print('after removing from list')
                break

        #if enemy bullet hits player tank
        for i in range(len(enemy_tank_bullets) - 1, -1, -1):
            if enemy_tank_bullets[i].rect.colliderect(player_one.rect):
                self.health = self.health - 1
                print('Health: ' + str(self.health))
                if self.constant_shoot == True:
                    self.state = 'fired'
                elif self.constant_shoot == False:
                    self.state = 'ready'
                self.rect.x = self.owner_tank.rect.x
                self.rect.y = self.owner_tank.rect.y
                break

        screen.blit(self.image, self.rect)


class Wall:
    '''
    This is a class representing a wall on the board
    '''
    pass
    def __init__(self, x_length, y_length, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        img = pygame.image.load('Wall.jpg')
        self.surface = pygame.transform.scale(img,(x_length, y_length))
        self.rect = Rect(x_pos, y_pos, x_length, y_length)

#creating walls
wall1 = Wall(10,100,345,345)
wall2 = Wall(10,110,445,345)
wall3 = Wall(90,10,355,345)
wall4 = Wall(55,10,345,445)
wall5 = Wall(20,350,380,450)
wall6 = Wall(245,20,455,390)
wall7 = Wall(50,20,750,390)
wall8 = Wall(270,10,80,345)
wall9 = Wall(270,10,0,445)
wall10 = Wall(90,60,200,100)
wall11 = Wall(80,10,720,70)
wall12 = Wall(60,90,445,235)
wall13 = Wall(20,100,550,50)
wall14 = Wall(150,15,60,600)
wall15 = Wall(150,15,60,600)

walls_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
                wall11, wall12, wall13, wall14, wall15]

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

bg_img = pygame.image.load('Background.png')
bg_img = pygame.transform.scale(bg_img,(800,800))

#create enemy tanks
#middle right
enemy_tank_one = EnemyTank(470, 342, 620, 342, 0)
#top left
enemy_tank_two = EnemyTank(30, 30, 30, 230, 0)
#middle left
enemy_tank_three = EnemyTank(100, 365, 300, 365, 180)
#bottom left
enemy_tank_four = EnemyTank(50, 700, 350, 700, 90)
#2nd to bottom left
enemy_tank_five = EnemyTank(50, 500, 200, 500, 0)
#bottom right
enemy_tank_six = EnemyTank(500, 700, 700, 700, 90)
enemy_tanks_list = [enemy_tank_one, enemy_tank_two, enemy_tank_three, enemy_tank_four, enemy_tank_five, enemy_tank_six]

#create players tank
player_one = Tank(385, 383, walls_list)

#create player tank bullet
player_one_bullet = Projectile(player_one, walls_list)
enemy_one_bullet = Projectile(enemy_tank_one, walls_list)
enemy_two_bullet = Projectile(enemy_tank_two, walls_list)
enemy_three_bullet = Projectile(enemy_tank_three, walls_list)
enemy_four_bullet = Projectile(enemy_tank_four, walls_list)
enemy_five_bullet = Projectile(enemy_tank_five, walls_list)
enemy_six_bullet = Projectile(enemy_tank_six, walls_list)
enemy_tank_bullets = [enemy_one_bullet, enemy_two_bullet, enemy_three_bullet, enemy_four_bullet, enemy_five_bullet, enemy_six_bullet]


#heart image
h_img = pygame.image.load('pixel_heart.png')
hp_img = pygame.transform.scale(h_img, (20, 20))


def game_over_screen():
    pygame.init()
    pygame.display.set_caption("Game Over")
    
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 80)
    text = font.render("Game Over", True, (255, 255, 255))
    text_width, text_height = text.get_size()
    center_x = (screen_width - text_width) // 2
    center_y = (screen_height - text_height) // 2
    screen.blit(text, (center_x, center_y))

    pygame.display.update()

#add caption to the game window
pygame.display.set_caption("Tank Game")

#run condition
game_over = False



#GAME LOOP
while not game_over:
    #set background
    screen.blit(bg_img, (0,0))

    #update all bullets
    player_one_bullet.update_bullet()
    for bullet in enemy_tank_bullets:
        bullet.update_bullet()

        if bullet.health == 3:
            screen.blit(hp_img, (370, 360))
            screen.blit(hp_img, (390, 360))
            screen.blit(hp_img, (410, 360))
        elif bullet.health == 2:
            screen.blit(hp_img, (370, 360))
            screen.blit(hp_img, (390, 360))
        elif bullet.health == 1:
            screen.blit(hp_img, (370, 360))
        else:
            game_over_screen()
            pygame.time.delay(5000)
            game_over = True


    #update tank
    player_one.update_tank()

    #rotate tank
    player_one.rotate_tank()
    
    #update all enemy tanks
    for tank in enemy_tanks_list:
        tank.update_tank()

    #draw walls
    screen.blit(wall1.surface,(wall1.x_pos,wall1.y_pos))
    screen.blit(wall2.surface,(wall2.x_pos,wall2.y_pos))
    screen.blit(wall3.surface,(wall3.x_pos,wall3.y_pos))
    screen.blit(wall4.surface,(wall4.x_pos,wall4.y_pos))
    screen.blit(wall5.surface,(wall5.x_pos,wall5.y_pos))
    screen.blit(wall6.surface,(wall6.x_pos,wall6.y_pos))
    screen.blit(wall7.surface,(wall7.x_pos,wall7.y_pos))
    screen.blit(wall8.surface,(wall8.x_pos,wall8.y_pos))
    screen.blit(wall9.surface,(wall9.x_pos,wall9.y_pos))
    screen.blit(wall10.surface,(wall10.x_pos,wall10.y_pos))
    screen.blit(wall11.surface,(wall11.x_pos,wall11.y_pos))
    screen.blit(wall12.surface,(wall12.x_pos,wall12.y_pos))
    screen.blit(wall13.surface,(wall13.x_pos,wall13.y_pos))
    screen.blit(wall14.surface,(wall14.x_pos,wall14.y_pos))
    screen.blit(wall15.surface,(wall15.x_pos,wall15.y_pos))

    #quit condition
    if len(enemy_tanks_list) == 0:
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()





































































