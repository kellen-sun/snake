import pygame, random, sys
import pkg_resources.py2_warn

def game():
    game_over, points, x, y, x_change, y_change, foodx, foody = False, 0, 5, 10, 0, 0, 15, 10
    snake_len = [(x,y)]
    dis = pygame.display.set_mode((800, 800))
    dis.fill((0,0,0))
    button1 = pygame.Rect(0, 0, 400, 400)
    pygame.draw.rect(dis, [255, 0, 0], button1)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("1", True, (0, 0, 0)), [180, 195])
    
    button2 = pygame.Rect(400, 0, 400, 400)
    pygame.draw.rect(dis, [255, 250, 0], button2)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("2", True, (0, 0, 0)), [580, 195])
    
    button3 = pygame.Rect(0, 400, 400, 400)
    pygame.draw.rect(dis, [10, 250, 30], button3)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("3", True, (0, 0, 0)), [180, 595])
    
    button4 = pygame.Rect(400, 400, 400, 400)
    pygame.draw.rect(dis, [0, 0, 200], button4)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("4", True, (0, 0, 0)), [580, 595])
    button5 = pygame.Rect(325, 375, 150, 50)
    pygame.draw.rect(dis, [250, 250, 200], button5)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("Speed", True, (0, 0, 0)), [348, 372])
    pygame.display.update()
    l = True
    while l:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 400 and mouse_pos[1] < 400:
                    speed = 1
                    l = False
                elif mouse_pos[0] > 400 and  mouse_pos[1] < 400:
                    speed = 2
                    l = False
                elif mouse_pos[0] < 400 and  mouse_pos[1] > 400:
                    speed = 3
                    l = False
                elif mouse_pos[0] > 400 and  mouse_pos[1] > 400:
                    speed = 4
                    l = False
    highscore = open("highscore.txt","r")
    h = int(highscore.read())
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = 1
                    y_change = 0
                elif event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -1
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    x_change = 0
                    y_change = -1
                elif event.key == pygame.K_DOWN and y_change == 0:
                    x_change = 0
                    y_change = 1
        x, y = x+x_change, y+y_change
        dis.fill((0,0,0))
        if x >= 20 or x < 0 or y >= 20 or y < 0:
            game_over = True
        snake_len.insert(0, (x, y))
        snake_len.pop(-1)
        if x == foodx and y == foody:
            snake_len.append((foodx - x_change, foody - y_change))
            moves=[]
            for x1 in range(20):
                for y1 in range(20):
                    if (x1, y1) not in snake_len:
                        moves.append((x1, y1))
            if moves != []:
                foodx, foody = random.choice(moves)
            else:
                game_over=True
            points += 1
        for j in range(1,  len(snake_len)):
            if x == snake_len[j][0] and y == snake_len[j][1]:
                game_over = True
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("Highcore: " + str(h), True, (255, 255, 200)), [0, 40])
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("Score: " + str(points), True, (255, 255, 200)), [0, 0])
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("Speed: " + str(speed), True, (255, 255, 200)), [0, 80])
        pygame.draw.rect(dis, (250, 50, 50), [foodx*40, foody*40, 40, 40])
        for i in range(0, len(snake_len)):
            pygame.draw.rect(dis, (0, 250, 100), [snake_len[i][0]*40, snake_len[i][1]*40, 40, 40])
        if points > h:
            h = points
        pygame.time.Clock().tick(speed*(speed+1)+10)
        pygame.display.update()
    highscore = open("highscore.txt","w")
    highscore.write(str(h))
    return [dis, points]

def two_player():
    dis = pygame.display.set_mode((900, 900))
    button1 = pygame.Rect(0, 0, 450, 450)
    pygame.draw.rect(dis, [255, 0, 0], button1)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("1", True, (0, 0, 0)), [220, 220])
    
    button2 = pygame.Rect(450, 0, 450, 450)
    pygame.draw.rect(dis, [255, 250, 0], button2)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("3", True, (0, 0, 0)), [670, 220])
    
    button3 = pygame.Rect(0, 450, 450, 450)
    pygame.draw.rect(dis, [10, 250, 30], button3)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("5", True, (0, 0, 0)), [220, 670])
    
    button4 = pygame.Rect(450, 450, 450, 450)
    pygame.draw.rect(dis, [100, 150, 250], button4)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("7", True, (0, 0, 0)), [670, 670])
    button5 = pygame.Rect(375, 425, 150, 50)
    pygame.draw.rect(dis, [250, 250, 200], button5)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("Foods", True, (0, 0, 0)), [398, 422])
    pygame.display.update()
    l = True
    while l:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 450 and mouse_pos[1] < 450:
                    speed = 1
                    l = False
                elif mouse_pos[0] > 450 and  mouse_pos[1] < 450:
                    speed = 3
                    l = False
                elif mouse_pos[0] < 450 and  mouse_pos[1] > 450:
                    speed = 5
                    l = False
                elif mouse_pos[0] > 450 and  mouse_pos[1] > 450:
                    speed = 7
                    l = False
    game_over, points1, x1, y1, x_change1, y_change1 = False, 0, 5, 5, 0, 0
    snake_len1 = [(x1,y1)]
    x2, y2, x_change2, y_change2, points2 = 25,25,0,0,0
    snake_len2 = [(x2,y2)]
    alive1, alive2 = True, True
    food = [(15, 15)]
    for x in range(speed-1):
        foodx, foody = random.randint(1, 30), random.randint(1, 30)
        food.append((foodx, foody))
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and x_change1 == 0:
                    x_change1 = 1
                    y_change1 = 0
                elif event.key == pygame.K_LEFT and x_change1 == 0:
                    x_change1 = -1
                    y_change1 = 0
                elif event.key == pygame.K_UP and y_change1 == 0:
                    x_change1 = 0
                    y_change1 = -1
                elif event.key == pygame.K_DOWN and y_change1 == 0:
                    x_change1 = 0
                    y_change1 = 1
                if event.key == pygame.K_d and x_change2 == 0:
                    x_change2 = 1
                    y_change2 = 0
                elif event.key == pygame.K_a and x_change2 == 0:
                    x_change2 = -1
                    y_change2 = 0
                elif event.key == pygame.K_w and y_change2 == 0:
                    x_change2 = 0
                    y_change2 = -1
                elif event.key == pygame.K_s and y_change2 == 0:
                    x_change2 = 0
                    y_change2 = 1
        if alive1:
            x1, y1 = x1+x_change1, y1+y_change1
        if alive2:
            x2, y2= x2+x_change2, y2+y_change2
        dis.fill((0,0,0))
        if x2 >= 30 or x2 < 0 or y2 >= 30 or y2 < 0:
            alive2 = False
        if x1 >= 30 or x1 < 0 or y1 >= 30 or y1 < 0:
            alive1 = False
        snake_len1.insert(0, (x1, y1))
        snake_len1.pop(-1)
        snake_len2.insert(0, (x2, y2))
        snake_len2.pop(-1)
        if (x1,y1) in food:
            snake_len1.append((x1 - x_change1, x2 - y_change1))
            moves=[]
            food.remove((x1,y1))
            for i in range(30):
                for j in range(30):
                    if (i, j) not in snake_len1 and (i, j) not in snake_len2:
                        moves.append((i, j))
            if moves != []:
                foodx, foody = random.choice(moves)
                food.append((foodx, foody))
            else:
                game_over=True
            points1 += 1
        if (x2,y2) in food:
            snake_len2.append((x2 - x_change2, y2 - y_change2))
            moves=[]
            food.remove((x2,y2))
            for i in range(30):
                for j in range(30):
                    if (i, j) not in snake_len2 and (i, j) not in snake_len1:
                        moves.append((i, j))
            if moves != []:
                foodx, foody = random.choice(moves)
                food.append((foodx, foody))
            else:
                game_over=True
            points2 += 1
        
        for j in range(1,  len(snake_len1)):
            if x1 == snake_len1[j][0] and y1 == snake_len1[j][1]:
                alive1 = False
        for j in range(1,  len(snake_len2)):
            if x1 == snake_len2[j][0] and y1 == snake_len2[j][1]:
                alive1 = False
        for j in range(1,  len(snake_len1)):
            if x2 == snake_len1[j][0] and y2 == snake_len1[j][1]:
                alive2 = False
        for j in range(1,  len(snake_len2)):
            if x2 == snake_len2[j][0] and y2 == snake_len2[j][1]:
                alive2 = False
        if not alive1 and not alive2:
            game_over = True
        for t in range(len(food)):
            pygame.draw.rect(dis, (250, 50, 50), [food[t][0]*30, food[t][1]*30, 30, 30])
        if alive1:
            for i in range(0, len(snake_len1)):
                pygame.draw.rect(dis, (0, 250, 100), [snake_len1[i][0]*30, snake_len1[i][1]*30, 30, 30])
        if alive2:
            for i in range(0, len(snake_len2)):
                pygame.draw.rect(dis, (100, 250, 0), [snake_len2[i][0]*30, snake_len2[i][1]*30, 30, 30])
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("Score of 1: " + str(points1), True, (255, 255, 200)), [0, 0])
        dis.blit(pygame.font.SysFont("comicsansms", 36).render("Score of 2: " + str(points2), True, (255, 255, 200)), [0, 40])
        pygame.time.Clock().tick(15)
        pygame.display.update()
    return [dis, points1, points2]

def run1():
    pygame.init()
    pygame.display.set_caption('Snake')
    ret = game()
    dis, score = ret[0], ret[1]
    highscore = open("highscore.txt","r")
    h = int(highscore.read())
    highscore.close()
    if score > h:
        highscore = open("highscore.txt","w")
        highscore.write(str(score))
    dis.fill((0,0,0))
    dis.blit(pygame.font.SysFont("comicsansms", 36).render('Highscore: '+str(h), True, (255, 255, 200)), [300, 150])
    dis.blit(pygame.font.SysFont("comicsansms", 48).render(str(score), True, (255, 255, 200)), [400, 240])
    dis.blit(pygame.font.SysFont("comicsansms", 48).render("Game Over", True, (255, 255, 200)), [300, 300])
    button = pygame.Rect(320, 380, 200, 50)
    pygame.draw.rect(dis, [255, 0, 0], button)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("Retry", True, (255, 255, 200)), [370, 375])
    button1 = pygame.Rect(10, 10, 170, 45)
    pygame.draw.rect(dis, [25, 0, 200], button1)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("2 players", True, (255, 255, 200)), [15, 4])
    pygame.display.update()
    restart = True
    while restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 520 and mouse_pos[0] >320 and mouse_pos[1] > 380 and mouse_pos[1] < 430:
                    restart = False
                elif mouse_pos[0] < 180 and mouse_pos[0] >10 and mouse_pos[1] > 10 and mouse_pos[1] < 55:
                    run2()
    run1()

def run2():
    pygame.init()
    pygame.display.set_caption('Snake')
    ret = two_player()
    dis, score1, score2 = ret[0], ret[1], ret[2]
    dis.fill((0,0,0))
    dis.blit(pygame.font.SysFont("comicsansms", 36).render('Player 1: '+str(score1), True, (255, 255, 200)), [380, 250])
    dis.blit(pygame.font.SysFont("comicsansms", 36).render('Player 2: '+str(score2), True, (255, 255, 200)), [380, 300])
    dis.blit(pygame.font.SysFont("comicsansms", 48).render("Game Over", True, (255, 255, 200)), [350, 350])
    button = pygame.Rect(370, 430, 200, 50)
    pygame.draw.rect(dis, [255, 0, 0], button)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("Retry", True, (255, 255, 200)), [420, 425])
    button1 = pygame.Rect(10, 10, 150, 45)
    pygame.draw.rect(dis, [25, 0, 200], button1)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("1 player", True, (255, 255, 200)), [15, 4])
    pygame.display.update()
    restart = True
    while restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 570 and mouse_pos[0] >370 and mouse_pos[1] > 430 and mouse_pos[1] < 480:
                    restart = False
                elif mouse_pos[0] < 160 and mouse_pos[0] >10 and mouse_pos[1] > 10 and mouse_pos[1] < 55:
                    run1()
    run2()
    
def start():
    pygame.init()
    pygame.display.set_caption('Snake')
    dis = pygame.display.set_mode((800, 800))
    dis.fill((0,0,0))
    button = pygame.Rect(420, 400, 200, 50)
    pygame.draw.rect(dis, [55, 0, 200], button)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("2 players", True, (255, 255, 200)), [445, 396])
    button1 = pygame.Rect(200, 400, 200, 50)
    pygame.draw.rect(dis, [255, 0, 0], button1)
    dis.blit(pygame.font.SysFont("comicsansms", 36).render("1 player", True, (255, 255, 200)), [230, 396])
    pygame.display.update()
    restart = True
    while restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if mouse_pos[0] < 620 and mouse_pos[0] >420 and mouse_pos[1] > 400 and mouse_pos[1] < 450:
                    run2()
                elif mouse_pos[0] < 400 and mouse_pos[0] >200 and mouse_pos[1] > 400 and mouse_pos[1] < 450:
                    run1()

start()
