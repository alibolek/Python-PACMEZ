# Muhammed Ali BOLEK 120709020
# Cihan SELIM        120709019
import maze
import turtle
import random
#TURTLESS
drawer = turtle.Turtle()
score_drawer =  turtle.Turtle()
lost_drawer =  turtle.Turtle()
cerceveci=turtle.Turtle()
lost_drawer.hideturtle()
mario = maze.MazeTurtle()
life_drawer= turtle.Turtle()
life_drawer.hideturtle()
life_drawer.penup()
def turn_left():
   mario.dir = maze.LEFT
def turn_right():
   mario.dir = maze.RIGHT
def turn_up():
   mario.dir = maze.UP
def turn_down():
   mario.dir = maze.DOWN
def is_wall(cell):
    return (abs(cell.x) == maze.width + 1)   or   \
           (abs(cell.y) == maze.height + 1)  or   \
           cell in walls
def debug():
    maze.clear_cell(drawer, maze.Cell(6,6))
    mario.move_to_cell(maze.Cell(0,0))
def start():
    score_drawer.undo()
    score_drawer.goto (-287, 250)
    score_drawer.write("SCORE = {0}".format(int(mario.score)), move=False, \
                       font=("Tempus Sans ITC", 12, "bold"))
    life_drawer.goto (218, 250)
    life_drawer.write("LIVES = {0}".format(mario.lives), move=False, \
                               font=("Tempus Sans ITC", 12, "bold"))
    life_drawer.speed(100)
    mario.showturtle()
    mario.goto(0, 0)
def update():
   if (mario.dir != maze.STAND):
       old_heading = mario.heading()
       if (mario.dir == maze.LEFT): new_heading = 180
       elif (mario.dir == maze.RIGHT): new_heading = 0
       elif (mario.dir == maze.UP): new_heading = 90
       else: new_heading = 270
       if (old_heading != new_heading):
          old_speed = mario.speed()
          mario.speed(0)
          mario.setheading(new_heading)
          mario.speed(old_speed)


       new_cell = maze.Cell(mario.cell.x, mario.cell.y)
       if (mario.dir == maze.LEFT): new_cell.x -= 1
       elif (mario.dir == maze.RIGHT): new_cell.x += 1
       elif (mario.dir == maze.UP): new_cell.y += 1
       else: new_cell.y -= 1
#SCORE TABELA
       if (not is_wall(new_cell)):
          mario.forward(maze.cell_size)
          mario.cell = new_cell
          if(mario.cell in items) and mario.lives>0:
            mario.shape("circle")
            mario.color(maze.bg_color)
            mario.shapesize(0.8)
            mario.stamp()
            mario.color("darkblue", "white")
            mario.shape("turtle")
            mario.score += 10

            items.remove(mario.cell)
            score_drawer.undo()
            score_drawer.goto (-287, 250)
            score_drawer.write("SCORE = {0}".format(int(mario.score)), move=False, \
                               font=("Tempus Sans ITC", 12, "bold"))

# ############## LEVEL 2 E GECIS
          elif mario.score==gecis*10 and mario.score!=100:

            mario.home()
            lost_drawer.penup()
            lost_drawer.goto(0, -280)
            lost_drawer.pendown()
            lost_drawer.write("LEVEL 2",align = "center", font= ("Tempus Sans ITC", 20, "bold"))
            mario.heading()
            mario.hideturtle()

            drawer.clear()
            level2()

            mario.score=50.1
            mario.showturtle()

# ############## LEVEL 3 E GECIS
          if mario.score==150.1:
            drawer.clear()
            level3()
            mario.score=150.2
            lost_drawer.penup()
            lost_drawer.goto(0, -280)
            lost_drawer.pendown()
            lost_drawer.write("LEVEL 3",align = "center", font= ("Tempus Sans ITC", 20, "bold"))
            lost_drawer.undo()
            mario.heading()
          if mario.score == 300.2:
                lost_drawer.penup()

                lost_drawer.goto(0,0)
                lost_drawer.pendown()
                mario.hideturtle()
                mario.move_to_home()
                for i in range(100) :

                    lost_drawer.write("YOU WON",align = "center", font= ("Tempus Sans ITC", 31, "bold"))
                    lost_drawer.undo()

#LIVES TABELA
          if(mario.cell in traps):
            mario.move_to_home()
            mario.dir= maze.STAND
            mario.lives -= 1
            life_drawer.undo()
            life_drawer.goto (218, 250)

            if mario.lives > 0:

                lost_drawer.pendown()
                life_drawer.clear()

                lost_drawer.color = ("white")
                life_drawer.write("LIVES = {0}".format(mario.lives), move=False, \
                         font=("Tempus Sans ITC", 12, "bold"))
#LOST YAZISI
            elif mario.lives<=0:
                lost_drawer.write("YOU LOST",align = "center", font= ("Tempus Sans ITC", 25, "bold"))
                mario.hideturtle()
                mario.goto(0,0)
                mario.heading()

       else:
          mario.dir = maze.STAND
       wn.title("Mario at ({0}, {1})  SCORE={2}".format(mario.cell.x, mario.cell.y, int(mario.score)))

   wn.ontimer(update,100)

""" # # # # # # # # # # LEVEL 1 # # # # # # # # # # # # # """
def level1():

    mario.dir=maze.STAND
    mario.move_to_home()
    rng = random.Random()
    global item_apple
    global gecis
    global walls
    global items
    global traps

    #ELMA RANDOM
    items = []
    elma_sayisi=5
    gecis=elma_sayisi
    item_apple =elma_sayisi
    while (item_apple > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in items):
          continue
       else:
          items.append(new_cell)
          item_apple -= 1

    lost_drawer.penup()
    lost_drawer.goto(0, -280)
    lost_drawer.pendown()
    lost_drawer.write("LEVEL 1",align = "center", font= ("Tempus Sans ITC", 20, "bold"))
    print(items)
    drawer.color("black", "darkgreen")
    drawer.shape("circle")
    drawer.shapesize(0.8)
    for cell in items:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

    #KUTU RANDOM
    walls = []
    wall_count = 10
    while (wall_count > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in walls or new_cell in items):
          continue
       else:
          walls.append(new_cell)
          wall_count -= 1
    print(walls)

    #TUZAK RANDOM
    traps = []
    trap_x = 5
    while (trap_x > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in traps or new_cell in items):
          continue
       else:
          traps.append(new_cell)
          trap_x -= 1
    print(traps)
    drawer.color("black", "red")
    drawer.shape("triangle")
    drawer.shapesize(0.8)
    for cell in traps:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

    drawer.fillcolor("black")
    for cell in walls:
        (x,y) = cell.to_coord(True)
        x += 1
        y -= 1
        maze.fill_rect(drawer, x, y, maze.cell_size-2, maze.cell_size-2)
    lost_drawer.clear()

#LISTS FOR 1
    myfile = open("1stLevelItems.txt", "w")
    myfile.write("1stLevelApples")
    myfile.write(str(items))
    myfile.write("\n")
    myfile.write("1stLevelTraps")
    myfile.write(str(traps))
    myfile.write("\n")
    myfile.write("1stLevelWalls")
    myfile.write(str(walls))
    myfile.write("\n")
    myfile.close()


""" # # # # # # # # # # LEVEL 2 # # # # # # # # # # # # # """
def level2():
    mario.dir=maze.STAND
    mario.move_to_home()
    rng = random.Random()
    global gecis
    global walls
    global items
    global traps
    #ELMA RANDOM
    items = []
    elma_sayisi=10

    gecis=elma_sayisi
    item_apple =elma_sayisi
    while (item_apple > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in items):
          continue
       else:
          items.append(new_cell)
          item_apple -= 1

    print(items)
    lost_drawer.penup()
    lost_drawer.goto(0, -280)
    lost_drawer.pendown()
    lost_drawer.write("LEVEL 2",align = "center", font= ("Tempus Sans ITC", 20, "bold"))
    drawer.color("black", "darkgreen")
    drawer.shape("circle")
    drawer.shapesize(0.8)
    for cell in items:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

    #KUTU RANDOM
    walls = []
    wall_count = 15
    while (wall_count > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in walls or new_cell in items):
          continue
       else:
          walls.append(new_cell)
          wall_count -= 1
    print(walls)

    #TUZAK RANDOM
    traps = []
    trap_x = 8
    while (trap_x > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in traps or new_cell in items):
          continue
       else:
          traps.append(new_cell)
          trap_x -= 1
    print(traps)
    drawer.color("black", "red")
    drawer.shape("triangle")
    drawer.shapesize(0.8)
    for cell in traps:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

    drawer.fillcolor("black")
    for cell in walls:
        (x,y) = cell.to_coord(True)
        x += 1
        y -= 1
        maze.fill_rect(drawer, x, y, maze.cell_size-2, maze.cell_size-2)
    lost_drawer.clear()

#LISTS FOR 2
    myfile = open("2ndLevelItems.txt", "w")
    myfile.write("2ndLevelApples")
    myfile.write(str(items))
    myfile.write("\n")
    myfile.write("2ndLevelTraps")
    myfile.write(str(traps))
    myfile.write("\n")
    myfile.write("2ndLevelWalls")
    myfile.write(str(walls))
    myfile.write("\n")
    myfile.close()

""" # # # # # # # # # # LEVEL 3 # # # # # # # # # # # # # """
def level3():
    mario.dir=maze.STAND
    mario.move_to_home()
    rng = random.Random()
    global gecis
    global walls
    global items
    global traps
    #ELMA RANDOM
    elma_sayisi=15
    items = []

    gecis=elma_sayisi
    item_apple =elma_sayisi
    while (item_apple > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in items):
          continue
       else:
          items.append(new_cell)
          item_apple -= 1

    print(items)
    lost_drawer.penup()
    lost_drawer.goto(0, -280)
    lost_drawer.pendown()
    lost_drawer.write("LEVEL 3",align = "center", font= ("Tempus Sans ITC", 20, "bold"))
    drawer.color("black", "darkgreen")
    drawer.shape("circle")
    drawer.shapesize(0.8)
    for cell in items:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()

    #KUTU RANDOM
    walls = []
    wall_count = 10
    while (wall_count > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in walls or new_cell in items):
          continue
       else:
          walls.append(new_cell)
          wall_count -= 1
    print(walls)

    #TUZAK RANDOM
    traps = []
    trap_x = 11
    while (trap_x > 0):
       i = rng.randint(-maze.width+1, maze.width-1)
       j = rng.randint(-maze.height+1, maze.height-1)
       new_cell = maze.Cell(i,j)
       if ((i == 0 and j == 0) or new_cell in traps or new_cell in items):
          continue
       else:
          traps.append(new_cell)
          trap_x -= 1
    print(traps)
    drawer.color("black", "red")
    drawer.shape("triangle")
    drawer.shapesize(0.8)
    for cell in traps:
        (x,y) = cell.to_coord()
        drawer.goto(x,y)
        drawer.stamp()
    drawer.fillcolor("black")
    for cell in walls:
        (x,y) = cell.to_coord(True)
        x += 1
        y -= 1
        maze.fill_rect(drawer, x, y, maze.cell_size-2, maze.cell_size-2)
    lost_drawer.clear()
#LISTS FOR 3
    myfile = open("3rdLevelItems.txt", "w")
    myfile.write("3rdLevelApples")
    myfile.write(str(items))
    myfile.write("\n")
    myfile.write("3rdLevelTraps")
    myfile.write(str(traps))
    myfile.write("\n")
    myfile.write("3rdLevelWalls")
    myfile.write(str(walls))
    myfile.write("\n")
    myfile.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
wn = turtle.Screen()
wn.bgcolor(maze.bg_color)
wn.title("Maze")
wn.setup(710,710)
wn.screensize(700,700)
wn.onkey(turn_left, "Left")
wn.onkey(turn_right, "Right")
wn.onkey(turn_up, "Up")
wn.onkey(turn_down, "Down")
wn.onkey(start, "s")
wn.onkey(start, "S")
wn.onkey(debug, "d")
#MARIO OZELLIK
mario.hideturtle()
mario.shapesize(0.7)
mario.color("darkblue", "white")
#ORTA YAZI
for t in [drawer, score_drawer]:
    t.fillcolor("black")
    t.speed(0)
    t.hideturtle()
    t.penup()
(x,y) = maze.Cell(0,maze.height+2).to_coord()
score_drawer.goto(x,y-8)
score_drawer.goto(0,250)
score_drawer.color("black")
score_drawer.write("Press 'S' to begin the game", align = "center", font= ("Tempus Sans ITC", 12, "bold") )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CERCEVE
cerceveci.penup()
cerceveci.hideturtle()
cerceveci.speed(100)
short_side = maze.cell_size
long_side_w = (2*maze.width+3)*maze.cell_size
long_side_h = (2*maze.height+3)*maze.cell_size
(x,y) = maze.Cell(-maze.width-1, maze.height+1).to_coord(True)
maze.fill_rect(cerceveci,x,y,short_side, long_side_h)
maze.fill_rect(cerceveci,x,y,long_side_w,short_side)
(x,y) = maze.Cell(-maze.width-1, -maze.height-1).to_coord(True)
maze.fill_rect(cerceveci,x,y,long_side_w,short_side)
(x,y) = maze.Cell(maze.width+1, maze.height+1).to_coord(True)
maze.fill_rect(cerceveci,x,y,short_side,long_side_h)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # INPUT

choice =  turtle.numinput("Your choice:", "Which level do you want to start in? \n 1- Easy \n 2- Medium \n 3- Hard", 2,1,3)
if choice == 1:
    level1()
    update()
if choice == 2:
    mario.score = 50
    mario.score=mario.score+0.1
    update()
    level2()
if choice == 3:
    mario.score = 150.1
    mario.score=mario.score+0.1
    level3()
    update()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
rng = random.Random()

wn.listen()
wn.mainloop()