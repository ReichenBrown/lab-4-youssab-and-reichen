#Authors: Reichen Brown & Youssab Girgis
#Date: 09/05/2023
#Description: Create a maze that the user can navigate through to solve.

import check_input
import random

def read_maze():
  maze = []
  ran = str(random.randint(1,2))
  file = open("maze" + ran + ".txt")
  for row in file:
    line = row.strip()
    maze.append(line)

  file.close()  
  return maze

def find_start(maze):
  start = []
  row_num = 0
  for row in maze:
    row_num += 1
    column_num = 0
    for column in row:
      column_num += 1
      if column == 's':
        return [row_num-1, column_num-1]

def display_maze(maze,loc):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if [row, col] == loc:
                print('X', end=' ')
            else:
                print(maze[row][col], end=' ')
        print()


def main():
  print("-Maze Solver-")
  print()
  
  maze = read_maze()
  start = find_start(maze)
  usr_loc = start
  
  '''while maze[usr_loc[0]][usr_loc[1]] != "f":
    display_maze(maze, usr_loc)

    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")

    choice = check_input.get_int_range("Enter choice: ", 1, 4)
    '''
  display_maze(maze,start)

    
  
  

main()