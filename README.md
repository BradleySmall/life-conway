Conway's Game of Life.

Given a grid of cells each of which is either "live" or "dead" progress through a simulation of steps.

At each step a given cell will either maintain its state, or change its state. 

If a live cell has < 2 live neighbors it will die of lonliness. 
If a dead cell has 3 live neighbors it will be born to life from warmth.
If a live cell has > 3 live neighbors it will smother to death.
All other cases simply maintain state.

Since Python uses utf8 using a full block character is possible
