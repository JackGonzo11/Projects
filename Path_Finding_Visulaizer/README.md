# Pathfinding Visualizer
This folder contains a maze generation program and pathfinding visualizer. The maze generation uses recursive backtracking using a stack to generate the maze. It is able to generate any size maze. The pathfinding visualizer ustalizes the algortihms Deapth First Search, Dijkstra's, and A* to solve the maze. 

## Installation
This code ran on a windows based system, but cna be easily transferable to other OS's. 
The code runs on Python version 3.7.7, which can be downloaded here [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
This program also ustalizes the Python library Pygame, which can be installed using the pip tool, (automatically installed with Python installation). To install pygame simple copy the following line into the terminal.
 ```bash
 python -m pip install -U pygame --user
 ```
 Finally, you can simple clone the github code via the internet or within the command line using
 ```bash
 git clone https://github.com/JackGonzo11/Projects.git
 ```
 Once all the steps above are done, you can navigate to the file in your terminal and run the sample codes using either
 ```bash
python Sample_Maze
python Sample_Algorithm
 ```

## Files
Cell:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This file contains the class Cell. The maze is generated on a tile map with each tile being represented by a Cell.

Maze_Generator:	This file contains the class Maze, which contains functions that creates a maze via recursive backtracking using a stack.

Algorithm_Examples:
	This file contains the class definitions of Deapth_First_Search, Dijkstras, and AStar. All of these class take a maze as an argument and apply their respective pathfinding algorithms to the maze. 
Sample_Maze:
	This file contains a simple python script that asks the user for 2 inputs. 
	The first is how big you want the maze to be in terms of rows and columns. 
		EX. If you input 50... it would generate a 50x50 maze
	The second is how big you want the window to be in terms of pixels.
		EX. If you enter 1000... it would generate a window of 1000x1000.
Sample_Algorithm:
	This file contains a simple python script that asks the user for 3 inputs.
	The first is which algorithm you would like to see solve the maze.
	The second is how big you want the maze to be in terms of rows and columns. 
		EX. If you input 50... it would generate a 50x50 maze
	The third is how big you want the window to be in terms of pixels.
		EX. If you enter 1000... it would generate a window of 1000x1000. 
WARNING: Try to make the inputs divisible by each other to ensure that the maze looks nice and 		maintains its square appearance. Also note the ratio of your current moniter, if choosing a 	window size of 2000x2000, The maze will be cut off. Try to stick to <= 1000.

## Pseudo code
Deapth First Search:

## Contributors
Jack Gonzales:
	Jack Gonzo11@gmail.com
	407-919-5302
	[LinkedIn](https://www.linkedin.com/in/jackgonzales112/)