from graphics import Window
from maze import Maze
import sys


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)

    print("Adventure Begins!")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Adventure Failed!")
    else:
        print("Veni, Vidi, Vici!😎")
    win.wait_for_close()


main()