import turtle

cell_size = 23  # keep it odd

# maze dimensions
width = 11  # cells at left and right of cell(0,0)
height = 9  # cells at top and bottom of cell(0,0)

# enumeration of directions for fast comparision
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
STAND = 5
# # #
bg_color = "lightblue"

class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def to_coord(self, top_left = False):
        """ Returns the midpoint (or top_left corner) of the cell as screen
             coordinates """
        global cell_size
        x = self.x * cell_size
        y = self.y * cell_size
        if (top_left):
            x -= cell_size / 2
            y += cell_size / 2
        return (x,y)

    def __repr__(self):
        return "C:({0},{1})".format(self.x, self.y)

    # to check if two cells are equal or not by using == we define __eq__.
    # example: cell_old == cell_new
    # this is called operator overloading since we are changing the behavior of the == operator
    def __eq__(self, other):
        """Two cells should be seen as equivalent if their coordinates are same."""
        return self.x == other.x and self.y == other.y

class MazeTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)  # first initialize MazeTurtle as a Turtle
        self.penup()
        self.shape("turtle")
        # new properties specific to MazeTurtles
        self.cell = Cell(0,0)
        self.dir = STAND
        self.score = 0
        self.lives = 3

    def move_to_cell(self,cell):
        self.goto(cell.to_coord())
        self.cell = cell
# # #
    def move_to_home(self):
        self.goto(0,0)
        self.cell = Cell(0,0)

def fill_rect(t,x,y,w,h):
    """Makes turtle t draw a rectangle where (x,y) is its top left corner
       and w and h are its dimensions"""
    t.goto(x,y)
    t.begin_fill()
    t.goto(x+w,y)
    t.goto(x+w,y-h)
    t.goto(x,y-h)
    t.goto(x,y)
    t.end_fill()

def clear_cell(t,cell):
    """Makes turtle t, clear a cell by drawing a rectangle there
       with background color"""
    old_color = t.fillcolor()
    t.fillcolor(bg_color)
    (x,y) = cell.to_coord(True)
    fill_rect(t, x, y, cell_size, cell_size)
    t.fillcolor(old_color)  # restore the original color

# # # # #
# # # # #


def clearScreen(t):
    t.goto(-cell_size*width,cell_size*height)
    fill_rect(t,-cell_size*width,cell_size*height,2*cell_size*width,2*cell_size*height)


