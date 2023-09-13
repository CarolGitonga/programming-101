"""
To process the records in the drawing1.txt file we can write a Python program
that reads the lines of this file and does the appropriate turtle graphics commands
for each record in the file. Since each record (i.e. drawing command) is on its own
line in the file format we can read the file by using a for
loop to read the lines of the file. This program that reads these
commands and processes each record in the file, drawing the picture that it contains.
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
    #for loop reads the lines of the file, one at a time
    # and executes the body of the loop once for each line of the file.
    for line in file:
        #strips off the newline character at the end of the line
        # and any blanks that might be at the start or end of the line.
        text = line.strip()
        #splits the text variable into its pieces.
        commandList = text.split(",")
        # get the drawing command
        command = commandList[0]
        if command == "goto":
            #makes a float object out of the string found in commandList[]
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
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