import pygame
from pygame.locals import *
#
# CLICKABLE BUTTON WITH AN IMAGE INSIDE IT
#
class Button:
	
	def __init__(self,x,y,imagefile):
		# load in the icon that will go in the middle of the button
		self.insideimg = pygame.image.load(imagefile).convert_alpha()
		self.insiderect = self.insideimg.get_rect()
		self.ix = self.insiderect.size[0]
		self.iy = self.insiderect.size[1]

		# set up base values for the size of this button to the image inside it
		self.image = pygame.surface.Surface((self.ix+8,self.iy+8))
		self.rect = self.image.get_rect()
		self.rect.left = x
		self.rect.top = y

		# set button as unpressed
		self.popup()

	# draw the button in an "unpressed" state
	def popup(self):
		self.image.fill((96,96,96))
		pygame.draw.line(self.image, (224,224,224), (0,0),(self.ix+8,0) )
		pygame.draw.line(self.image, (224,224,224), (0,0),(0,self.ix+8) )
		pygame.draw.line(self.image, (224,224,224), (1,1),(self.ix+7,1) )
		pygame.draw.line(self.image, (224,224,224), (1,1),(1,self.ix+7) )
		pygame.draw.line(self.image, (224,224,224), (2,2),(self.ix+6,2) )
		pygame.draw.line(self.image, (224,224,224), (2,2),(2,self.ix+6) )
		pygame.draw.rect(self.image, (160,160,160), ((3,3),(self.ix+3,self.iy+3)) )
		# put the button icon on the button
		self.image.blit(self.insideimg,(4,4))

	# draw the button in a "pressed" state
	def press(self):
		self.image.fill((224,224,224))
		pygame.draw.line(self.image, (96,96,96), (0,0),(self.ix+8,0) )
		pygame.draw.line(self.image, (96,96,96), (0,0),(0,self.ix+8) )
		pygame.draw.line(self.image, (96,96,96), (1,1),(self.ix+7,1) )
		pygame.draw.line(self.image, (96,96,96), (1,1),(1,self.ix+7) )
		pygame.draw.line(self.image, (96,96,96), (2,2),(self.ix+6,2) )
		pygame.draw.line(self.image, (96,96,96), (2,2),(2,self.ix+6) )
		pygame.draw.rect(self.image, (160,160,160), ((3,3),(self.ix+3,self.iy+3)) )
		# put the button icon on the button
		self.image.blit(self.insideimg,(4,4))
		

	# this gets called if the mouse is clicked - check if the button was hit
	def clicked(self, pos):
		if (self.rect.left < pos[0] < self.rect.right) and (self.rect.top < pos[1] <
		self.rect.bottom):
			return True

#
# BASIC USE
#

pygame.init()

screen = pygame.display.set_mode((400, 400))

screen.fill( (255,255,255) )

# create the button at 100,100 and put an image called go.png inside it
gobut = Button(100,100,"undo.png")
# put the button on the screen
screen.blit(gobut.image,gobut.rect)
pygame.display.flip() #update display

while True : # this would be like your main loop
	k = pygame.event.poll() #look for an event
	
	if k.type == MOUSEBUTTONDOWN: #if they click,
		print 'click'
		
		if gobut.clicked(pygame.mouse.get_pos()): #check if the button's limits are clicked
			gobut.press() #depress the button
			screen.blit(gobut.image,gobut.rect) #update the screen
			print "they clicked the go button"
			
			
			
	pygame.display.flip() #update display
	#do_whatever_else() #call your "go" function here
