#this is a game where the player is a helicopter and has to dodge the missiles coming to them.
import pygame
import random

#initialise the pygame modules.
pygame.init() 

#set screen size for the game, using width and height.
screen_width= 1080
screen_height= 600
screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Helicopter vs Missiles.")

#loading the player and the 3 enemy character images.
#got the helicopter for the player character from Shutterstock
#https://www.shutterstock.com/image-vector/helicopter-silhouette-vector-graphic-black-1560276911
player= pygame.image.load("c:/Users/Lwandiso/Dropbox/Lwandiso Ntlanga-86418/Introduction to Programming/Task 15/helicopter.png") 

#I got the images for the missiles from Flaticon and changed the colour for enemy character
#https://www.flaticon.com/free-icon/missile_2809725?term=missile&related_id=2809725
enemy1= pygame.image.load("c:/Users/Lwandiso/Dropbox/Lwandiso Ntlanga-86418/Introduction to Programming/Task 15/missiles1.png") 
enemy2= pygame.image.load("c:/Users/Lwandiso/Dropbox/Lwandiso Ntlanga-86418/Introduction to Programming/Task 15/missiles2.png")
enemy3= pygame.image.load("c:/Users/Lwandiso/Dropbox/Lwandiso Ntlanga-86418/Introduction to Programming/Task 15/missiles3.png") 

#get width and height of character images for boundry detection.
player_width= player.get_width() 
player_height= player.get_height() 

enemy1_width= enemy1.get_width() 
enemy1_height= enemy1.get_height()

enemy2_width= enemy2.get_width() 
enemy2_height= enemy2.get_height()

enemy3_width= enemy3.get_width() 
enemy3_height= enemy3.get_height() 

#display the player and enemies width and height image info.
print(f"Player width: {player_width}, height: {player_height}")
print(f"Enemy 1 width: {enemy1_width}, height: {enemy1_height}")
print(f"Enemy 2 width: {enemy2_width}, height: {enemy2_height}")
print(f"Enemy 3 width: {enemy3_width}, height: {enemy3_height}")

#the position of the player
player_x_position= 100
player_y_position= 50

#the position of the enemies
enemy1_x_position= screen_width
enemy1_y_position= random.randint(0, screen_height-enemy1_width) 

enemy2_x_position= screen_width
enemy2_y_position= random.randint(0, screen_height-enemy2_width) 

enemy3_x_position= screen_width
enemy3_y_position= random.randint(0, screen_height-enemy3_width) 

#checks if the up, down, left or right key is pressed.
#since they are not pressed now, they will be initialised as False until pressed.
key_up= False
key_down= False
key_left= False
key_right= False

#game loop
while True:
    screen.fill(False)
    #this draws the player image to the screen at the postion specfied. I.e. (100, 50)
    screen.blit(player,(player_x_position,player_y_position))
    screen.blit(enemy1, (enemy1_x_position, enemy1_y_position))
    screen.blit(enemy2, (enemy2_x_position, enemy2_y_position))
    screen.blit(enemy3, (enemy3_x_position, enemy3_y_position))

    #updates the screen
    pygame.display.flip()
    
    #loops through the events in the game.
    for event in pygame.event.get():
        
       #this event checks if the user quits the program, then if so it exits the program.
        if(event.type== pygame.QUIT):
           pygame.quit()
           exit(False)
        
        #checks if the user pressed the up, down, left or right key.
        if(event.type== pygame.KEYDOWN):
            if(event.key== pygame.K_UP):
                key_up= True

            if(event.key== pygame.K_DOWN):
                key_down= True

            if(event.key== pygame.K_LEFT):
                key_left= True

            if(event.key== pygame.K_RIGHT):
                key_right= True

        #checks if the pressed down keys are released.
        if(event.type== pygame.KEYUP):
            if(event.key== pygame.K_UP):
                key_up= False

            if(event.key== pygame.K_DOWN):
                key_down= False

            if(event.key== pygame.K_LEFT):
                key_left= False

            if(event.key== pygame.K_RIGHT):
                key_right= False

    #this makes sure that the user does not move the player above the window.
    if(key_up== True):
        if(player_y_position> 0):
            player_y_position -=1
    
    #this makes sure that the user does not move the player below the window.
    if(key_down== True):
        if(player_y_position< screen_height-player_height):
            player_y_position +=1

    #this makes sure the user does not move the player out of left side of window.
    if(key_left== True):
        if(player_x_position> 0):
            player_x_position -=1

    #this makes sure the user does not move the player out of right side of window.
    if(key_right== True):
        if(player_x_position< screen_width-player_width):
            player_x_position +=1

    #check for collision of the enemy with the player.
    #to do this we need bounding boxes around the images of the player and enemy.

    #bounding box for the player
    player_box= pygame.Rect(player.get_rect())

    #the following updates the playerBox position to the player's position,
    #in effect making the box stay around the player image.    
    player_box.top= player_y_position
    #player_box.down= player_y_position #'pygame.Rect' object has no attribute 'down'
    player_box.left= player_x_position
    player_box.right= player_x_position

    #bounding box for the enemy 1
    enemy1_box= pygame.Rect(enemy1.get_rect())

    #the following updates the enemy1 box position to the player's position,
    #in effect making the box stay around the player image.
    enemy1_box.top= enemy1_y_position
    #enemy1_box.down= enemy1_y_position #'pygame.Rect' object has no attribute 'down'
    enemy1_box.left= enemy1_x_position
    enemy1_box.right= enemy1_x_position

    #bounding box for the enemy 2
    enemy2_box= pygame.Rect(enemy2.get_rect())

    #the following updates the enemy2 box position to the player's position,
    #in effect making the box stay around the player image.
    enemy2_box.top= enemy2_y_position
    #enemy2_box.down= enemy2_y_position #'pygame.Rect' object has no attribute 'down'
    enemy2_box.left= enemy2_x_position
    enemy2_box.right= enemy2_x_position

    #bounding box for the enemy 3
    enemy3_box= pygame.Rect(enemy3.get_rect())

    #the following updates the enemy2 box position to the player's position,
    #in effect making the box stay around the player image.
    enemy3_box.top= enemy3_y_position
    #enemy3_box.down= enemy3_y_position #'pygame.Rect' object has no attribute 'down'
    enemy3_box.left= enemy3_x_position
    enemy3_box.right= enemy3_x_position

    #tests collision of the boxes.
    if(player_box.colliderect(enemy1_box)):
        
        #display losing status to the user if boxes collide.
        print("You lose!")
        pygame.quit()
        exit(False)
    
    if(player_box.colliderect(enemy2_box)):
        
        #display losing status to the user if boxes collide.
        print("You lose!")
        pygame.quit()
        exit(False)

    if(player_box.colliderect(enemy3_box)):
        
        #display losing status to the user if boxes collide.
        print("You lose!")
        pygame.quit()
        exit(False)

    #if the enemy is off screen the user wins the game.
    if(enemy1_x_position< 0 -enemy1_width):
        
        #display winning status to the user if boxes do not collide.
        print("You win!")
        pygame.quit()
        exit(False)

    if(enemy2_x_position< 0 -enemy2_width):
        
        #display winning status to the user if boxes do not collide.
        print("You win!")
        pygame.quit()
        exit(False)
    
    if(enemy3_x_position< 0 -enemy3_width):
        
        #display winning status to the user if boxes do not collide.
        print("You win!")
        pygame.quit()
        exit(False)

    #enemy approaching the player.
    enemy1_x_position-= 0.40
    enemy2_x_position-= 0.30
    enemy3_x_position-= 0.50
