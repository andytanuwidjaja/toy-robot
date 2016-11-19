#!/usr/bin/env python

# function definition for each command
def fPlace( robot,tabletop,location ):
  print "attempting a place"
  print "  > location = ", location
  return

def fMove( robot,tabletop ):
  print "attempting a move"
  return

def fLeft( robot ):
  print "attempting a left"
  return

def fRight( robot ):
  print "attempting a right"
  return

def fReport( robot ):
  print "attempting a report"
  return

# robot variable definition
# format is posX,posY,direction
robot = []

# table top variable definition
# format is sizeX,sizeY
tabletop = [5,5]

# open the file containing input data
f = open('input.txt','r')

data = f.readlines()

# iterate through each line of data
for line in data:
  
  # convert string to list
  list = line.rstrip("\n").split(" ")

  # execute function as per command in list
  if list[0] == "PLACE":
    fPlace(robot, tabletop, list[1])
  elif list[0] == "MOVE":
    fMove(robot, tabletop)
  elif list[0] == "LEFT":
    fLeft(robot)
  elif list[0] == "RIGHT":
    fRight(robot)
  elif list[0] == "REPORT":
    fReport(robot)
  else:
    print "Unrecognised command:", list[0]


f.close

