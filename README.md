# Master Pyraminx A* Solver
A solver using the A* algorithm of 2D representation of the master pyraminx, a 4x4 triangular pyramid rubix cube  
CS463G Fall 2024

## How to run
Install python 3.12.5  
Navigate to the project folder/directory  
Install the matplotlib package
```
pip install matplotlib
```
Run the A_Star.py python file in a terminal, preferably one with a black background color 
```
python A_Star.py
```
Enjoy!

## The Pyraminx recap
The pyraminx has 4 faces. In this representation a player will only rotate the front face. To make a move, the player must specify a corner, and which layer to turn. The possible corners are the upper corner, the left corner, the right corner, and the back corner. So the user could input one of the following: U, L, R, B followed by one of the four layers: 1, 2, 3, 4. Then to specify the direction the user inputs 1 or 2 to specify clockwise or counterclockwise respectively. In the program the solver only interacts with the front face. This may differ from your standard pyraminx representation that only lets you change the first row, the first and second row, the third row, and the fourth row. As such this pyraminx has orders of magnitude more states that the pyraminx can be in after a few moves than a standard pyraminx.

## Data structures
#### Open List
Type: `Min-Heap` (implemented using a list with heapq functions)  

Purpose: The open list keeps track of nodes that need to be explored. Nodes in this list are prioritized based on their f value (the sum of the cost to reach the node and the estimated cost to reach the goal from the node).  

Operations:
- Insertion: `heapq.heappush(open_list, (node.f, node))` adds a node to the heap while maintaining the heap property.

- Extraction: `heapq.heappop(open_list)` removes and returns the node with the smallest f value.
#### Closed List
Type: `List`
- Purpose: The closed list keeps track of nodes that have already been explored to avoid reprocessing them.
#### Nodes
Type: `Node Class` (made by me)  
Purpose: Represents states in the search space. Each node typically contains:
- State Information: The current configuration of the pyraminx.
- Parent Pointer: A reference to the parent node, used to reconstruct the path once the goal is reached.

- Cost Values: g (cost from the start node), h (heuristic estimate to the goal), and f (sum of g and h).

## Heuristic
The description of the admissible heuristic used in this program:  
The admissible heuristic for this program sums up the amount of cubies in wrong spots on all the four faces, divides the result by 21, then takes the ceiling. This is admissible because the function leverages the fact that at most 21 cubies can be displaced in one turn, that being the layer four turn. The code for the heuristic function can be found in the `Face.py` file, as well as below:  
```
def heuristic_function(left_face, front_face, right_face, bottom_face) -> int:
    left_face_count = left_face.check_cubies()
    front_face_count = front_face.check_cubies()
    right_face_count = right_face.check_cubies()
    bottom_face_count = bottom_face.check_cubies()
    return math.ceil((left_face_count + front_face_count + right_face_count + bottom_face_count) / 21)
```

## Results
This is where the results of the output are detailed:  

The program outputs graphs that show how many nodes are expanded in each trial of a k depth randomized pyraminx. The variance in the results is large because of the nature of the implemented pyraminx (see pyraminx recap).  

The program can solve pyraminxes up to k=6 randomization, where the program will run for hours then crash before even solving one trial.    

This is a list of runtimes and k level:

- k = 1: instant
- k = 2: instant
- k = 3: instant to 1 minute runtime
- k = 4: 30 seconds to 2 minute runtime
- k = 5: Around 1 hour runtime
- k = 6: crashes

Because of the ability to modify each row individually, the ability to turn the back corner of the pyraminx, and the ability to turn both clockwise and counter clockwise there are many possible states, and the program crashes at a depth of k=6. Additionally, it is possible for a trial to get "lucky" and have two moves that counter-act each other, like a U1 clockwise move, then a U1 counterclockwise move, which would significantly speed up a trial.


## Learning Outcomes
A discussion of learning outcomes had during this assignment:  

### Technical
Deep Copy vs Shallow copy - Again in this assignment I had difficulty navigating deep copy vs shallow copy when trying to affect the pyraminx. In particular when trying to generate the children I had to redefine functions to make my life easier and allocate extra memory to making sure the configuration of the pyraminx wasn't adversly affected by generating new children.

### Project completing skills
Time estimation - This project took a lot longer than expected. When I would discover a bug in the algorithm I had to rerun all the test cases, which when the program got to k=5, took hours each time.

Documentation - For every function I tried to document the inputs and outputs. The documentation may be repeating information, but I am trying to write enough so that if one just looked at that section of the code they at least understand the inputs and outputs with the documentation.

Pseudocode - Understanding how to implement the A* Algorithm was a long arduous process. It was only after asking chatgpt to generate a tailor-made pseudocode for the project that understanding how to implement it finally clicked. I had to split up implementing the algorithm into many steps, where I implemented functions in the Node class to accomodate them.