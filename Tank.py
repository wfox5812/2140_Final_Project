#This is the game file for the game
class Tank:
    def __init__(self, speed):
        self.speed = speed































































































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