"""
Sometimes records of a file are not one per line. Records of a file may cross multiple
lines like in drawing2.txt. In that case, you can’t use a for loop to read the file. You need a while loop
instead. When you use a while loop, you need to be able to check a condition to see
if you are done reading the file. But, to check the condition you must first try to read
at least a little of a record. Computer programmers have a name for this problem
as it relates to reading from files. It is called the Loop and a Half Pattern. To use a
while loop to read from a file, we need a loop and a half. The half comes before the
while loop.
"""
# import the turtle graphics module
import turtle

#the main code of the program
def main():
    #reads a line of input from the user
    filename = input("Please enter drawing filename: ")
    #create turtle graphics window to draw in
    t = turtle.Turtle()
    #screen is used at the end of the program
    screen = t.getscreen()
    #opens the file for "r" or reading
    file = open(filename, "r")
    # half a loop to get things started. Reading our first graphics command
    # lets us determine if the file is empty or not.
    command = file.readline().strip()
    # If the command is empty, there are no more commands left in the file.
    while command != "":
        
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command =="endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unkown command found in file:", command)

        #If command is empty it is because there were no more commands in the
        # file and the while loop will terminate.
        command = file.readline().strip()
    #close the file
    file.close()
    #hide the turtle that we used to draw the picture.
    t.ht()
    #hold the turtle graphics window open until the mouse is clicked.
    screen.exitonclick()
    print("Program Execution Completed. ")
    
# This code calls the main function to get everything started.
if __name__ == "__main__":
    main()