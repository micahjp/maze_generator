# Welcome to Maze Generator!

This is a simple maze game. In it's current state the program generates a maze 
and allows you to navigate through it using the arrow keys or vim keys (hjkl).

### Running the Program

To play the game simply clone this repo `git clone https://github.com/micahjp/maze_generator.git`
and run `python3 main.py` from your terminal.

Once the maze is done generating you can use the arrow keys or vim keys to 
navigate. You automatically begin in the top left opening of the maze and will 
have solved the maze once you navigate through the bottom right opening.

If at any point you are bored or stuck you may press the 's' key and the maze 
will solve itself.

Once the maze has been solved the program will automatically close after 5 seconds.

### Customization

If you wish to modify the maze you can edit the 'main.py' file. Change the 
'cell_size_(x/y)' variables to modify the width/height of the cells the maze is
made up of. Change the 'num_(cols/rows)' variables to modify how many cells make
up the maze.
