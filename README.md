# Simple Infection Simulation
Pygame draws an n by n matrix of rectangles. Each individual cell can be infected by infected neighbours, disinfected cells have a chance to heal neighbouring infected cells. Tweaking the code yield different patterns and behaviour such as clustering.

## Requirements
* Python
* Pygame (Easily installed by using Python's package manager: `pip install pygame`.)

## Getting Started
When both Python and pygame are installed, just run
`python3 main.py` or `python main.py`, depending on your installation.

### Interaction
One can interact with the cells by clicking on them. Clicking on a cell will yield the cell and its surrounding cells infected when the cells are disinfected and vice versa.

## Work in progress
The `main.py` procedural variant of the simulation is a mess, so everything will be object-orientated soon.
