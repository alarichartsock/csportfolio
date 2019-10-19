# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

file = open("C:/Users/iamth/Documents/Academics/School/csportfolio/cs260/maze/examplemaze.txt","r")
x = file.read()
print(x)
y = x.split('\n')
print(y)
z = y[1].split()
