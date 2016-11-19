#!/usr/bin/env python

########## Toy Robot Simulator ##########
# Assumption:

# Tabletop is represented by [x,y] 

# ^ y axis
# 5 x x x x x x
# 4 x x x x x x
# 3 x x x x x x
# 2 x x x x x x
# 1 x x x x x x
# 0 x x x x x x
#   0 1 2 3 4 5 x axis >

# Direction North ^

# The robot's current state is represented using 3 variables: [posX,posY,direction] where posX is position in x axis, 
#   posY is position in y axis and direction is the direction where the robot is facing

# Robot movements are treated as a markov chain, where it changes from one state to the next state 
#   based on the commands given. 

# The future state of the robot is calculated based on its initial state and the command that has been given

# If the future state is not allowed (i.e. the robot falls off the table), the initial state will be retained
#   and the robot will be ready for the next command

##########################################

import sys

# global variable
# turn on verbose for more detailed output
verbose = 0

#---------------------------------------------------------
# function definition for executeCommand
#---------------------------------------------------------
def executeCommand(robotState,tabletop,commandLine):
  # declare local variable
  robotFutureState = []

  # declare mapping for MOVE command
  # for example: if robot is facing east, a move command will mean an increment to its x position
  moveMap = {'EAST':[1,0],
             'NORTH':[0,1],
             'WEST':[-1,0],
             'SOUTH':[0,-1]}

  # declare mapping for a left move command
  # for example: if robot is facing east, a left command will mean the robot will face north
  rotationLeftMap = {'EAST':'NORTH',
                     'NORTH':'WEST',
                     'WEST':'SOUTH',
                     'SOUTH':'EAST'}

  # declare mapping for a right move command
  rotationRightMap = {'EAST':'SOUTH',
                      'NORTH':'EAST',
                      'WEST':'NORTH',
                      'SOUTH':'WEST'}

  # convert command line to list
  commandList = commandLine.split(" ")

  if verbose: 
    print " > command: ", commandList
    print "   > initial state: ", robotState  

  # branch on command
  if commandList[0] == "PLACE":
    tmpState = commandList[1].split(",")
    robotFutureState = [int(tmpState[0]),int(tmpState[1]),tmpState[2]]
  else:
    if not robotState:
      # the initial state of the robot is an empty list, which means robot is not on the table
      # ignore all the commands and keep the robot in its initial state
      robotFutureState = []
    else:
      if commandList[0] == "MOVE":
        # Find the robot's future state, take its x,y position and add the increment value from the mapping. 
        # Direction remains the same
        robotFutureState = [robotState[0]+moveMap[robotState[2]][0],robotState[1]+moveMap[robotState[2]][1],robotState[2]] 
      if commandList[0] == "LEFT":
        # Find its future state, x,y position remains the same, direction is new based on the mapping
        robotFutureState = [robotState[0],robotState[1],rotationLeftMap[robotState[2]]]        
      if commandList[0] == "RIGHT":
        # Find its future state, x,y position remains the same, direction is new based on the mapping
        robotFutureState = [robotState[0],robotState[1],rotationRightMap[robotState[2]]]        
      if commandList[0] == "REPORT":
        # Report robot position, state remains the same
        robotFutureState = robotState
        print robotState[0] , "," , robotState[1] , "," , robotState[2]

  if verbose: print "   > candidate future state: ", robotFutureState

  # check whether future state is acceptable 
  if not robotFutureState:
     # future state is an empty list, keep initial state
     result = robotState
  elif ((robotFutureState[0] >= 0 and robotFutureState[0] <= tabletop[0]) and
        (robotFutureState[1] >= 0 and robotFutureState[1] <= tabletop[1]) and
        (robotFutureState[2] in ['EAST','NORTH','WEST','SOUTH'])): 
     # future state is valid, robot is on the table facing to a valid direction,
     # keep future state
     result = robotFutureState
  else:
     # future state is not valid, keep initial state
     result = robotState

  if verbose: print "   > outcome: ", result

  return result


#---------------------------------------------------------
# Main program start 
#---------------------------------------------------------

# robot variable definition
robot = []

# table top variable definition
tabletop = [5,5]

# check command line argument
if len(sys.argv) == 1:
  print "ERROR: Need to enter the input filename as argument"
  sys.exit()

filename = sys.argv[1]

# open the file containing input data
f = open(filename,'r')

data = f.readlines()

# iterate through each line of data
for line in data:
  
  # execute command
  robot = executeCommand(robot,tabletop,line.rstrip("\n"))

f.close

