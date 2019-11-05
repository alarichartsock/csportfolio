# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

file = open("C:/Users/iamth/Documents/Academics/School/csportfolio/cs260/maze/examplemaze.txt","r")
x = file.read()
y = x.split('\n')


class Stack:
    """Python implementation for an abstract Stack class"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Runner:
    def __init__(self):
        """Initilizing Runner. Input raw maze data. A 0 is interpreted as a path, anything else is considered an obstacle.""" 
        self.pathStack = Stack()
    
    def show(self,x,y,maze):
        """Prints the entire maze with the runner inside of it, represented as R. Y Value is the runners position # of rows down from the top, X value is # of characters from the left."""
        mazerow = list(maze[y]) 
        mazerow[x] = "R"
        mazerowstr = "".join(mazerow)
        maze[y] = mazerowstr #Inserting our runner
        mazestring = "" 
        for i in range(len(maze)): #Turning the list back to a string to print
            mazestring = mazestring + maze.pop(0)
            mazestring = mazestring + '\n'
        print(mazestring)

    def run(self,startx,starty,maze):
        realmaze = maze
        completed = False
        currentx = startx
        currenty = starty
        previousx = None
        previousy = None
        while completed == False:
            self.show(currentx,currenty,realmaze)
            print(self.pathStack.size())
            self.look(maze,currentx,currenty,previousx,previousy) # look for new places to walk
            if self.pathStack.size() == 0:
                print("Maze is inescapable!")
                return
            else:
                #moving to the next cordinate
                newcoords = self.pathStack.pop()
                previousx = currentx
                previousy = currenty
                currentx = newcoords[0]
                currenty = newcoords[1]

    def look(self,maze,currentx,currenty,oldx,oldy):
        """Looks right, below, up, and left in that order for places to walk."""
        mazerow = list(maze[currenty])
        # if(mazerow[currentx] == "X"):
        #     print("Found the end of the maze!!")
        #     completed = True
        #     return
        try:
            mazerowabove = list(maze[currenty-1])
            mazerowbelow = list(maze[currenty+1])
        except IndexError as e:
            pass
        if mazerow[currentx+1]=="0" and not (currentx+1==oldx and currenty==oldy): #look right
            print("trying this")
            self.pathStack.push([currentx+1,currenty])
        elif mazerowbelow[currentx]=="0" and not (currentx==oldx and currenty+1==oldy): #look below
            print("trying this")
            self.pathStack.push([currentx,currenty+1])
        elif mazerowabove[currentx]=="0" and not (currentx==oldx and currenty-1==oldy): #look above
            print("trying this")
            self.pathStack.push([currentx,currenty-1])
        elif mazerow[currentx-1] == "0" and not (currentx-1==oldx and currenty==oldy): #look left
            print("trying this")
            self.pathStack.push([curretx-1,currenty])


runner = Runner()
runner.run(0,1,y)
