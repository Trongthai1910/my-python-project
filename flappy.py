import pygame
from random import randint
pygame.init()
		#màu
rect_color = (212,227,0)
screen_color = (230,252,250)
soil_color = (163,86,15)
text_color = (167,171,176)
column_color = (48,207,17)
	#các biến game
#con tream
x = 100
y = 217 
#nhảy và rơi xuống
y_co = 0
force = 0
gravity = 0
state = 0 #(1 = nhảy; 2 = rơi xuống)
#cột trụ 1 và 2
x_column1 = 700
y_column1 = 50
x_column2 = x_column1 + 430
y_column2 = 300
x_column_move = 0.25
#random (cái này để mấy cái cột màu xanh chạy mãi mãi)
ran = 0
#điểm
score = 0
score_end = 0
#trạng thái cửa sổ game
state_game = 0 #(0 = bắt đầu game;  1 = chơi game;  2 = end game)	
running = True #(True = chạy cửa sổ game; False = thoát game)
	#chuẩn bị: window game,title, văn bản,...
screen = pygame.display.set_mode((700,664))
pygame.display.set_caption("Flappy Rectangle")
font = pygame.font.SysFont('comicsansms',30)
font2 = pygame.font.SysFont('comicsansms',50)
font3 = pygame.font.SysFont('comicsansms',70)
font4 = pygame.font.SysFont('comicsansms',60)
start_text = font.render("TAP TO START",True,text_color)
again_text = font.render("PLAY AGAIN",True,text_color)
intro_text = font4.render("FLAPPY RECTANGLE",True,(186,177,7))
	#chạy cửa sổ game
while running:
	if state_game == 0: #(bắt đầu game)
			#window game
		screen.fill(screen_color)
		pygame.draw.rect(screen, soil_color, (0,614,700,50))
		pygame.draw.rect(screen, rect_color, (100,217,35,30))
		screen.blit(intro_text,(49,140))
		screen.blit(start_text,(250,300))
			#sự kiện game
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				state_game = 1
		score = 0
	if state_game == 1: #(chơi game)
		score_text = font2.render(str(score),True,text_color) #(viết điểm)
			#window game
		screen.fill(screen_color)
		pygame.draw.rect(screen, soil_color, (0,614,700,50))
			#sự kiện game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				y_co = y
				state = 1
				force = 0.5
			#logic game
		#trạng thái của con tream
		gravity = 0.25
		if y >= 584:
			gravity = 0
			state_game = 2
		if y <= 0:
			state = 2
		if y > 0:
			if state == 1:
				if y > (y_co-100):
					y -= force
				if y == (y_co-100):
					force = 0
					state = 2
		if state == 2:
			y += gravity
		#trạng thái của cây cột
		if x_column2 == 375:	
			x_column1 = 805
			y_column1 = randint(50,150)
		if x_column1 == 375:
			x_column2 = 805
			y_column2 = randint(50,150)
		x_column1 -= x_column_move
		x_column2 -= x_column_move
		#tính điểm:
		if x==x_column1+55 or x==x_column2:
			score += 1
			score_end = score
		#kết quả
		if x_column1-35<=x<=x_column1+55: #con cheem đâm vào cột 1
			if y_column1-30<=y<=y_column1+50 or y_column1+200<=y<=y_column1+280:
				state_game = 2
		if x==x_column1-25:
			if 0<=y<=y_column1-30 or y_column1+280<=y<=584:
				state_game = 2
		if x_column2-35<=x<=x_column2+55: #con cheem đâm vào cột 2
			if y_column2-30<=y<=y_column2+50 or y_column2+200<=y<=y_column2+280:
				state_game = 2
		if x==x_column2-25:
			if 0<=y<=y_column2-30 or y_column2+280<=y<=584:
				state_game = 2	
		
			#hiển thị lên màn hình
		pygame.draw.rect(screen, rect_color, (x,y,35,30))  #(con tream)
		pygame.draw.rect(screen, column_color, (x_column1,y_column1,55,50))        				#(cột 1)
		pygame.draw.rect(screen, column_color, (x_column1+10,0,35,y_column1))
		pygame.draw.rect(screen, column_color, (x_column1,y_column1+230,55,50))    				#(cột 1')
		pygame.draw.rect(screen, column_color, (x_column1+10,y_column1+280,35,334-y_column1))
		pygame.draw.rect(screen, column_color, (x_column2,y_column2,55,50))					#(cột 2)
		pygame.draw.rect(screen, column_color, (x_column2+10,0,35,y_column2))
		pygame.draw.rect(screen, column_color, (x_column2,y_column2+230,55,50))  				#(cột 2')
		pygame.draw.rect(screen, column_color, (x_column2+10,y_column2+280,35,334-y_column2))
		screen.blit(score_text,(340,40))
	if state_game == 2: #(end game)
		score_end_text = font3.render(str(score_end),True,text_color)
			#window game
		screen.fill(screen_color)
		pygame.draw.rect(screen, soil_color, (0,614,700,50))
		pygame.draw.rect(screen, rect_color, (x,y,35,30)) #(con tream)
		pygame.draw.rect(screen, column_color, (x_column1,y_column1,55,50))        				#(cột 1)
		pygame.draw.rect(screen, column_color, (x_column1+10,0,35,y_column1))
		pygame.draw.rect(screen, column_color, (x_column1,y_column1+230,55,50))    				#(cột 1')
		pygame.draw.rect(screen, column_color, (x_column1+10,y_column1+280,35,334-y_column1))
		pygame.draw.rect(screen, column_color, (x_column2,y_column2,55,50))					#(cột 2)
		pygame.draw.rect(screen, column_color, (x_column2+10,0,35,y_column2))
		pygame.draw.rect(screen, column_color, (x_column2,y_column2+230,55,50))  				#(cột 2')
		pygame.draw.rect(screen, column_color, (x_column2+10,y_column2+280,35,334-y_column2))
		screen.blit(again_text,(260,300))
		screen.blit(score_end_text,(340,200))
		score = 0
		mousex, mousey = pygame.mouse.get_pos()
			#sự kiện game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if 250<=mousex<=430 and 300<=mousey<=330:
					y = 217
					x_column1 = 700
					y_column1 = 50
					x_column2 = x_column1 + 430
					y_column2 = 300
					x_column_move = 0.25
					state_game = 0
	pygame.display.flip()
pygame.quit