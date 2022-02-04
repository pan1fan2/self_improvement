# Game 1024



### [Introduction](https://en.wikipedia.org/wiki/2048_(video_game))

1024 is played on a plain 4×4 grid(matrix). The initial matrix has two 2s which are randomly populated in the matrix. A player can move them using one of the four keyboard inputs ['a','d','s','w'] ('a' - move left, 'w' - move up, 's' - move down, 'd' - move right ) . Afrer every move , a new tile randomly appears in an empty spot in the matrix with a value of 2.

A player can move tiles as far as possible in the chosen direction (up/down/left/down) until they are stopped by either another tile or the boundary of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. 

The game is won when a tile with a value of 1024 appears in the matrix. When there is no available moves  the game is over.

### Environment

- Python (3. 7 or up)

### Requirement

- Numpy (1.13.0 or up)

### Usage

`python game1024.py`

