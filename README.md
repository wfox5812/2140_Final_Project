# 2140_Final_Project
1. Who is on your team? If you are working with a partner, how will the labor be divided? 
    William Fox and Charlie Amante are collaborating on this project. The labor will be as evenly divided as possible by assigning
different issues to each partner. For example, if three classes have to be defined as three different issues in the project,
and one class is slightly more complex than the other two, the two simpler classes will be assigned to one partner and the 
more complex class will be assigned to the other partner. Work will be divided in an attempt to have both partners work on
every main aspect of the game so that they both have a solid understanding of every aspect of the program.

2. An overview of the project similar in scope and length to the example projects listed below.
Tank game:
    We will write a program that will create a game window displaying an environment with walls and enemy tanks, and a tank to be controlled by the user. The goal of the game is for the user to eleminate enemy tanks without dying. The user's tank will 'die' if it loses all of its hearts. Both the user's tank and  enemy tanks will be able to shoot projectiles that, if come in contact with another tank, will either destroy or remove a heart from the tank. The user's tank will have three hearts, a set speed, and set fire rate. Enemy tanks will vary in number of hearts, speed, and fire rate and these attributes will correspond to a specified color. The walls in the 2D game environment will prevent any tank or projectile from moving through them. The user will control the motion of the tank by pressing keys that correspond to an x or y direction. The user will be able to shoot projectiles by pressing a different key and will be shot in the direction the tank is facing. If the enemy tanks are eliminated,
    the game will end and a victory message and score will be displayed that will be determined using 1.The time taken to complete the game, 2.The number of hearts left on the user's tank. If the user's tank loses all of its hearts, a different message will be displayed telling the user they have lost.   

3. A short description of the structure of your project. How many classes will you write? What the methods be for each class? (You can change this if it turns out a better structure would work better once you start writing code and you decide to refactor. Just try to come up with a reasonable one for the proposal.)

--------- We may not need all of these, or we may need to add more depending on issues that arise throughout the process ---------
We have outlined the classes that we should need for this game below.
    CLASSES:
        -Tank()                         #Tank class for each tank object
           Variables:
            -speed
            -direction
            -x_position
            -y_position
            -health
            -color
            -size
           Method Functions:
            -get_speed()
            -get_direction()
            -get_health()
            -set_health()
            -shoot_projectile()
            -remove_heart()
            -move()
            -set_direction()
        -Player(Tank)                   #User tank class
           Methods:
            -get_key_press()
        -Enemy(Tank)                    #Represents an enemy tank
        -Projectile()                   #Represents a projectile
           Variables:
            -speed
            -direction
            -x_position
            -y_position
            -size
        -Wall()                         #Represents a wall
           Variables:
            -length
            -width
            -x_position
            -y_position

4. What libraries and tools will you need to learn to use?
    We will be importing PyGame. PyGame has many different features such as creating a border for your game, tracking direction and speed, tracking the key you press, sprites, and so on. Since we are making a tank game with walls, enemy tanks, and projectiles, we will need to learn how all of these will intereact with each other. We may need to import the random library and/or time library to track the time 

5. Identify the highest-priority features, the medium-priority features, and the lowest-priority features for your project.
    Highest-priority features:
        1. Game board
        2. Tank objects
        3. Movement
    
    Medium-priority features:
        1. Projectiles
        2. Collisions

    Lowest-priority features:
        1. Score
        2. Losing a life






Summary of Code:
This program is a 1-player tank game in which the user controls a tank with the arrow keys and shoots projectiles with the space bar. The player starts in the middle of the map and has to navigate around the map to the final section through a series of walls and obstacles. Throughout the map, enemy tanks are scattered that move in predetermined paths and shoot in the path of the player's tank. The player must control their tank to navigate around the map and destroy the enemy tanks by shooting them. The pygame module was used to create the game and was used to make almost all of the features including the game environment, the walls, the tanks, and the bullets. The main features are the player tank, the walls, the enemy tanks, and the bullets. The player tank is controlled by the arrow keys and can move up, down, left, right, and diagonally (although the tank only ever faces one of the four main directions of up, down, left, and right). The walls limit the tank's movement, and nothing can pass through them. The enemy tanks move in predetermined paths and are not "smart" (although this is a feature that could be implemented in the future). The bullets can be fired one at a time and return to the tank that shot them when they collide with an obstacle. The tanks and bullets cannot pass through the walls or the edge of the screen, and this collision control is an important aspect of the game. The expected applications of this game are to be played casually by individuals. The goal is for the player to enjoy themselves during the game and have fun.

Overview of the code:
We have four classes in our program total. None of them are parent classes to the other because of how we designed the tank class which would have been a parents class to the enemy tank when we initially thought about designing our program. There were too many differences between the classes. Then tank class is to control the functions of the tank, like to move around, change the orientation of the tank, and shoot bullets when the space bar is pressed. The tank class has the functions update tank and rotate tank. The update tank method, updates the x and y velocity depending on the key that is pressed. The starting position is part of the initialization of the player tank. We have the tank not being able to move through walls and the projectile also can't move through walls. The other method is the is the rotate tank function. This function rotates the tank based on the current orientation and what button is being pressed. The next class is the enemy tank which just has the update tank function. We couldn't figure out how to fire bullets from this tank and make them get destroyed if they are hit. The update function will move the tank back and forth in one direction. The projectile class has and update bullet function that changes the position and orientation of the bullet based on the key pressed and on the initial orientation of the tank. The wall class is the last class. Each time we made a wall we added it to a list of walls and when checking for collisions, we iterated through the loop and checked eached wall to make sure the bullet reset every time it hit something.


Instructions for use:
First, once you run the code, move the tank around with the arrow keys and make sure it it moving properly. Once you've done that, use the space bar to shoot the bullets out of the tank. Once you've learned the controls, drive around and shoot the enemy tanks. We have not implemented the enemy tanks getting destroyed yet because we couldn't figure it out in time. We also have not implemented the enemy tnaks rotating yet, although that would be easy to implement since we already have the code for rotating the player tank. We spent most of our time figuring out how to make the player tank and collisions with walls including the collisions with the projectiles with the walls.


Suggested future directions:
One feature that would be great to add to this game would be making the enemy tanks "smart". This means that instead of the enemy tanks moving in predetermined paths that loop, their movement and shooting would be based on the location of the player's tank. This would be very interesting to develop and would require constantly getting the input of the coordinates of the player's tank and using that to determine the movement of the enemy tanks. They would have to recognize when they got close to walls and would have to realize that they cannot shoot through walls. Another feature that would be a good addition to the game would be making the game a two-player game. Another tank could be added that could be controlled by another player and the tanks could either work together to destroy the enemy tanks or they could battle each other. This would not be as difficult as making enemy tanks smarter because this would just involve making another object of the Tank class and getting inputs for movement and shooting from a different 5 buttons so that both players could play on a single keyboard. A third feature that could be added could be making it possible for tanks to shoot more than one bullet at once. This would involve having multiple bullet objects associated with a single tank, and there would have to be a fire rate implemented that would determine how often a bullet could be shot from the tank. This would be a great addition because it would make the game more intense and likely more fun for the user.





