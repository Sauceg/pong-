# MARVIN UWALAKA 

# access pygame, random and math modules 
import pygame,random,math


# define main function 
def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Pong')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes
# GAme class handles smostof pomg events 
class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # self is the Game to initialize
      # surface is the display window surface object

      self.surface = surface 
      # backround color of where the game would be plaued on 
      self.bg_color = pygame.Color('black')
      
      # fps set to 60 so we can see the objects in the game moving 
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      paddle_length = 50
      # === game specific objects
      
      # distance paddles moves 
      self.paddle_increment = 10
      # paddle2 starting position
      y = self.surface.get_height()//2 - paddle_length//2 
      x = self.surface.get_width() - 100
      
      # making paddle objects paddles 1 and 2 
      self.paddle = Paddle(100,y,10,40,'white',self.surface)
      self.paddle2 = Paddle(x,y,10,40,'white',self.surface)
      
      # making ball and setting its starting position to the middle 
      ball_center = [self.surface.get_width()//2, self.surface.get_height()//2] 
      self.ball = Ball('white',5,ball_center,[4,2.5],self.surface,self.paddle,self.paddle2)

      # setting scor of both players to 0 at the start of the game 
      self.left_score = 0 
      self.right_score = 0 
      
      
      
                    
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box 
         # check for certain events 
         self.handle_events()
         # draw objects
         self.draw()          
         # if contnue_game is true call upadate and decide continue methodss 
         if self.continue_game:
            self.update()
            self.decide_continue()  # check if the game is over and return continue_game as false 
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      events = pygame.event.get()  # get  and receive event method from pygame
      # check your user input using event method 
      for event in events: 
         if event.type == pygame.QUIT:  # check if the close window event happens and set self.close_clicked to false 
            self.close_clicked = True
         elif event.type == pygame.KEYDOWN: # check if the user presses a key down and the game uses handle_key_down funtcion to react accodingly 
            self.handle_key_down(event)
         elif event.type == pygame.KEYUP:   # check if the user releases a key and the game uses handle_key_up function to react accodingly
            self.handle_key_up(event)
   
   
   def handle_key_down(self,event):
      # reponds to KEYDOWN event
      # - self is the Game object
      if event.key == pygame.K_p:  # if p key is pressed move right paddle up 
         self.paddle2.set_vertical_velocity(-self.paddle_increment)
      elif event.key == pygame.K_l:   # if l key is pressed move right paddle down
         self.paddle2.set_vertical_velocity(self.paddle_increment)
      if event.key == pygame.K_q:      # if q key is pressed move left paddle up 
         self.paddle.set_vertical_velocity(-self.paddle_increment)
      elif event.key == pygame.K_a:    # if a key is pressed move down paddle up 
         self.paddle.set_vertical_velocity(self.paddle_increment)
   
   def handle_key_up(self,event):
      # responds to KEYUP event
      # - self is the Game object
      if event.key == pygame.K_p:  # if p key is released stop moving right paddle 
         self.paddle2.set_vertical_velocity(0)
      elif event.key == pygame.K_l:   # if l key is released stop moving right paddle 
         self.paddle2.set_vertical_velocity(0)
      if event.key == pygame.K_q:    # if q key is released stop moving left paddle 
         self.paddle.set_vertical_velocity(0)
      elif event.key == pygame.K_a:   # if q key is released stop moving left paddle 
         self.paddle.set_vertical_velocity(0)         

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.paddle.draw()  # draw left paddle 
      self.paddle2.draw() # draw right paddle 
      self.ball.draw()    # draw ball
      self.draw_score()   # draw left and right scores 
      
      pygame.display.update() # make the updated surface appear on the display
   
   def draw_score(self):
      # draws left and right scores
  
      self.draw_left_score()
      self.draw_right_score()
      
   def draw_left_score(self):
      # draws left score 
      font = pygame.font.SysFont('',70)  # text size 
      test_image = font.render(str(self.left_score),True, pygame.Color('white'), self.bg_color) # text and the text color 
      location = (0,0)    # where txt is to be drawn 
      self.surface.blit(test_image,location)   # blits the text to surface and intended location 
   
   def draw_right_score(self):
      font= pygame.font.SysFont('',70)                                    # text size 
      test_image = font.render(str(self.right_score),True, pygame.Color('white'), self.bg_color) # text and the text color 
      location = (self.surface.get_width() - test_image.get_width() ,0)   # where txt is to be drawn 
      self.surface.blit(test_image,location)                              # blits the text to surface and intended location  
         
   
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      self.paddle.move()         # movement of  left paddle being updated 
      self.paddle2.move()        # movement of right paddle being updated 
      edge = self.ball.move()    # movement of ball being updated and return what edge the ball touched
      if edge == 'left':         # if the ball touches the left edge the right player get a point
         self.right_score = self.right_score +1 
      elif edge == 'right':      # if the ball touches the left edge the right player get a point  
         self.left_score = self.left_score + 1 
      
   
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to chec_game
      # if any of the two players get to 11 self.continue is set to false and the game stops updatting and responding to events 
      if self.left_score == 11 or self.right_score == 11:
         self.continue_game = False 
   
class Paddle:
   # An object in this class represents a Paddle that moves
   
   def __init__(self,x,y,width,height,color,surface):
      # - self is the Paddle object
      # - x, y are the top left corner coordinates of the rectangle of type int
      # - width is the width of the rectangle of type int
      # - height is the heightof the rectangle of type int
      # - surface is the pygame.Surface object on which the rectangle is drawn
      
      self.rect = pygame.Rect(x,y,width,height)
      self.color = pygame.Color(color)
      self.surface = surface
      self.vertical_velocity = 0 # paddle is not moving at the start
      
   def draw(self):
      # -self is the Paddle object to draw
      pygame.draw.rect(self.surface,self.color,self.rect)
   def set_vertical_velocity(self,vertical_distance):
      # set the vertical velocity of the Paddle object
      # -self is the Paddle object
      # -vertical_distance is the int increment by which the paddle moves vertically
      self.vertical_velocity = vertical_distance
   
   def move(self):
      # moves the paddle such that paddle does not move outside the window
      # - self is the Paddle object
      self.rect.move_ip(0,self.vertical_velocity) 
      #touched the right edge of the window 
      # move the paddle 
      if self.rect.bottom >= self.surface.get_height():
         self.rect.bottom = self.surface.get_height()
      elif self.rect.top <= 0:
         #move the paddle back by its width 
         self.rect.top = 0

class Ball: 
   def __init__(self,ball_color,ball_radius,ball_center, ball_velocity, surface,paddle,paddle2):
     # self.color is the color of the ball 
     # self.radius is the radius of the ball
     # self.velocity is the speed at which the ball move at 
     # self.surface is the surface the ball has to move around in
     # self.paddle and self.paddle2 are the different rect objects      
      
      self.color =  pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
      self.paddle = paddle
      self.paddle2 = paddle2
      
   def draw(self):
      # -self is the ball object to draw
      pygame.draw.circle(self.surface,self.color,self.center,self.radius)
   
   def move(self):
      # moves the ball such that paddle does not move outside the window
      # - self is the ball object
      size = self.surface.get_size()   # get the size of the window 
      edge = False    # set what edge the ball hit to False 
      touched_leftpaddle, touched_rightpaddle = self.collidepoint()  # check if the ball hit the left or right paddle 
   
   
      # Change the center of the ball by the velocity to give the image of the ball moving 
      for i in range(0,2):
         self.center[i] = self.center[i] + self.velocity[i]
      
      for i in range(0,2):
         if self.center[i] < self.radius :  # if the ball goes pass the left edge ot the top edge of the window then change the velocity 
             # reached the minimum for this coordinate, turn back
            self.velocity[i] = - self.velocity[i]
         if self.center [i] + self.radius > size[i]: 
             # reached the maximum for this coordinate, turn back
            self.velocity[i] = - self.velocity[i]
     
      if self.center [0] + self.radius >= size[0] and self.velocity[0] < 0: # if the ball hits the right edge assign right to edge
            edge = 'right'
      if self.center [0] - self.radius <= 0 and self.velocity[0] > 0 : # if the ball hits the right edge assign right to edge
            edge = 'left'       
      if touched_leftpaddle or touched_rightpaddle: #if the ball hits the left or right paddle reverse its horizontal velocity 
         self.velocity[0] = - self.velocity[0]

      return edge   # return edge 
         
         
   def collidepoint(self):
      # checks if ball hits left or right paddles and returns if the ball collides with the paddles 
      # set the collisions to false 
      
         touched_left_paddle = False 
         touched_right_paddle = False 
         if self.paddle.rect.collidepoint(self.center) and self.velocity[0] < 0: # if the center of the ball is within the left paddle assign True to  touched_left_paddle
            touched_left_paddle = True 
         if self.paddle2.rect.collidepoint(self.center) and self.velocity[0] > 0: # if the center of the ball is within the right paddle assign True to  touched_right_paddle
            touched_right_paddle = True 
         return touched_left_paddle, touched_right_paddle 
# call main function 
main()