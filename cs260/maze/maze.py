
#Me and Sam Jadzak worked on this together, so our code might look slightly similar.

file = open("C:/Users/iamth/Documents/Academics/School/csportfolio/cs260/maze/examplemaze.txt","r")
x = file.read()
y = x.split('\n')

class Stack:
    """Python implementation for an abstract Stack class"""
    def __init__(self):
        """Initializes a Stack"""
        self.items = []

    def isEmpty(self):
        """Returns true if the Stack is Empty"""
        return self.items == []

    def push(self, item):
        """Pushes an item onto the Stack."""
        self.items.append(item)

    def pop(self):
        """Pops an item from the stack."""
        return self.items.pop()

    def peek(self):
        """Peeks at an item on the Stack."""
        return self.items[len(self.items)-1]

    def size(self):
        """"Returns the size of the Stack."""
        return len(self.items)
    
    def show(self):
        """Prints out the content of the Stack"""
        print(self.items)


class Runner:
    """The Runner class runs through the maze"""
    def __init__(self):
        """Initializes runner. The y starts at 0 at the top of the maze and then increases as it goes down."""
        self.maze = None
        self.s = Stack()
        # self.x = None
        # self.y = None
        self.prevx = None
        self.prevy = None

    def run(self,maze,x,y):
        """Gives the runner a maze to go through, along with starting positions. The maze given should be a txt file."""
        self.maze = maze.split('\n')
        self.x = x
        self.y = y
        completed = False
        s = 1
        while completed == False:
            self.look(self.x,self.y)
            cords = self.s.pop()
            self.prevx = self.x
            self.prevy = self.y
            self.x = cords[0]
            self.y = cords[1]
            print(self.show(self.x,self.y))
            if self.checkEnded(self.x,self.y) == True:
                completed = True
                print("Completed the maze. Horray")
            else:
                pass
        
    def checkEnded(self,x,y):
        """Checks to see if the runner has reached the end of the maze."""
        if self.maze[y][x+1] == "X": #look right
            return True
        elif self.maze[y+1][x+1] == "X": #look down right
            return True
        elif self.maze[y+1][x] == "X": #look down
            return True
        elif self.maze[y+1][x-1] == "X": #look down left
            return True
        elif self.maze[y][x-1] == "X": #look left
            return True
        elif self.maze[y-1][x-1] == "X": #look up left
            return True
        elif self.maze[y-1][x] == "X": #look up
            return True
        elif self.maze[y-1][x+1] == "X": #look up right
            return True
        
    def displayEnd(self):
        print("Ended!")

    def show(self,x,y):
        """Supplants a R onto the screen to represent the runner's location."""
        maze = ""
        for i in range(len(self.maze)):
            if i==y: #if it's the row that the runner is on
                row = self.maze[i]
                r = []
                for c in row:
                    r.append(c)
                r[x] = "R"
                row = ""
                for d in range(len(r)):
                    row = row + r[d]
                maze = maze + str(row) + '\n'
            else: #if it's any other row
                maze = maze + self.maze[i] + '\n'
        return maze

    def look(self,x,y):
        """Looks around a given position, says if there is an opening or if there's a wall."""
        vals = []
        if self.maze[y][x+1] == "0": #look right
            vals.append((x+1,y))
        if self.maze[y+1][x+1] == "0": #look down right
            vals.append((x+1,y+1))
        if self.maze[y+1][x] == "0": #look down
            vals.append((x,y+1))
        if self.maze[y+1][x-1] == "0": #look down left
            vals.append((x-1,y+1))
        if self.maze[y][x-1] == "0": #look left
            vals.append((x-1,y))
        if self.maze[y-1][x-1] == "0": #look up left
            vals.append((x-1,y-1))
        if self.maze[y-1][x] == "0": #look up
            vals.append((x,y-1))
        if self.maze[y-1][x+1] == "0": #look up right
            vals.append((x+1,y-1))
        self.s.push((self.prevx,self.prevy))
        for i in range(len(vals)):
            v = vals.pop()
            if v[0] == self.prevx and v[1] == self.prevy:
                pass
            else:
                self.s.push(v)

import unittest

class test(unittest.TestCase):
    def testMathAndEq(self):
        """Tests Runner"""
        r = Runner()
        r.run(x,0,1)  

if __name__ == '__main__':
    unittest.main()