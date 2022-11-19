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