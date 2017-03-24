import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
COLOR = "#55FF88"
LEVEL_WID = 32
LEVEL_HEIGHT = 32
LEVEL_COL = "#221144"

def main():
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY) 
	pygame.display.set_caption("Test Game")
	bg = Surface((WIN_WIDTH,WIN_HEIGHT))
	bg.fill(Color(COLOR))
	while 1:
			for i in pygame.event.get():
				if i.type == QUIT:
					raise SystemExit
			screen.blit(bg, (0,0))
			pygame.display.update()


level = [
	"__________________________",
	"_                        _",
	"_                        _",
	"_             ______     _",
	"_                  _     _",
	"_    ___           _     _",
	"_                  _     _",
	"_             ______     _",
	"_                        _",
	"_   ______               _",
	"_        _____           _",
	"_             ___        _",
	"_                        _",
	"__________________________"]

x=y=0
for row in level:
	for col in row:
		if col == "_":
			pf = Surface((LEVEL_WID,LEVEL_HEIGHT))
			pf.fill(Color(LEVEL_COL)) 
			screen.blit(pf,(x,y))
							
			x += LEVEL_WID
			y += LEVEL_HEIGHT
			x = 0 
				

	if __name__ == "__main__":
		main()