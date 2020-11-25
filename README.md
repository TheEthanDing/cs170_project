# CS 170 Project Fall 2020

Take a look at the project spec before you get started!

Requirements:

Python 3.6+

You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

If using pip to download, run `python3 -m pip install networkx`


Files:
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

When writing inputs/outputs:
- Make sure you use the functions `write_input_file` and `write_output_file` provided
- Run the functions `read_input_file` and `read_output_file` to validate your files before submitting!
  - These are the functions run by the autograder to validate submissions

We'll need: 

Input parameters:
- n = Number of students in the class
- hi j = Happiness student i and j give each other
- si j = Stress student i and j induce on each other
- Smax = Maximum total stress across all breakout rooms

Output values:
- Hr = Happiness of breakout room r
- Sr = Stress of breakout room r
- Htotal = Total happiness across all breakout rooms
- k = Total number of breakout rooms opened