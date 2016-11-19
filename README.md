-------------------------------------------------
Toy Robot Simulator Programming Challange
-------------------------------------------------

The application is a simulation of a toy robot moving on a square tabletop,
of dimensions 5 units x 5 units. It is written in python.

Syntax:
python toy-robot.py < input-filename >

where < input-filename > is the file containing a series of input commands
for the robot.

Example Input (input1.txt):
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

Output:
3 , 3 , NORTH

-------------------------------------------------
Development Note
-------------------------------------------------

Robot movements are treated as a markov chain, where it changes from one state to the next state
based on the commands given.

The future state of the robot is calculated based on its initial state and the command that has been given

If the future state is not allowed (i.e. the robot falls off the table), the initial state will be retained
and the robot will be ready for the next command

It is possible to change the verbose option inside the script to further illustrate this changing states 
of the robot.

Example output with verbose option:

Example 1. Command accepted and state updated succesfully:

 > command:  ['PLACE', '1,2,EAST']
   > initial state:  []
   > candidate future state:  [1, 2, 'EAST']
   > outcome:  [1, 2, 'EAST']
 > command:  ['MOVE']
   > initial state:  [1, 2, 'EAST']
   > candidate future state:  [2, 2, 'EAST']
   > outcome:  [2, 2, 'EAST']

Example 2. Command will cause robot to fall off, initial state retained:

> command:  ['MOVE']
   > initial state:  [3, 5, 'NORTH']
   > candidate future state:  [3, 6, 'NORTH']
   > outcome:  [3, 5, 'NORTH']




