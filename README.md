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