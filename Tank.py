#This is the game file for the game
class Tank:
    '''
    This class represents a single tank object and will be the parent class 
    '''
    def __init__(self, speed, size, color, x_pos, y_pos, health, direction):
        self.speed = speed
        self.size = size
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.health = health
        self.direction = direction
    
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
    def __init__(self, length, width, x_pos, y_pos):
        self.length = length
        self.width = width
        self.x_pos = x_pos
        self.y_pos = y_pos

    def create_wall(length, width_input, x_pos_input, y_pos_input):
        '''
        Creates a wall in a certain area
        (We are not sure if we want to implement this yet)
        '''
        pass















































































