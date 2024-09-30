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
Type: `Node Class`  
Purpose: Represents states in the search space. Each node typically contains:
- State Information: The current configuration of the pyraminx.
- Parent Pointer: A reference to the parent node, used to reconstruct the path once the goal is reached.

- Cost Values: g (cost from the start node), h (heuristic estimate to the goal), and f (sum of g and h).

## Heuristic
This admissible heuristic function searches for groups of misplaced cubies. It will take a look at all 3 corners of the face, adding 1 for every color not matching its original color. It will then look at the edges of the face, split up a little unevenly so it can include all the pieces of the remaining cubies of the face excluding the middle cubie without overlapping, broken up by the left edge having cubies stored at [1, 2, 4, 5], right edge having cubies stored at [3, 7, 8] and the bottom edge having cubies stored at [10, 11, 12, 13, 14]. And it checks the middle cubie as well last. To prevent unnecessary counter additions for edges if there are multiple incorrect cubies, the 'any' function is used only call it 1 time if there is at least 1 misplace, and still 0 times if there are none. After counting all the misplaced corners, edges, and middle pieces, that number will be divided by 9 because that is the most amount of misplaced corners edges and middle pieces on a single move, that move being a base rotation. The code for the heuristic function can be found in the `Face.py` file, as well as below:  
```
 def check_cubies(self) -> int:
        counter = 0
        # Define the specific cubie positions for corners and edges
        corner_indices = [0, 9, 15]  # Example: first index in each corner group
        edge_indices = [(1, 2, 4, 5), (3, 7, 8), (10, 11, 12, 13, 14)]  # Each tuple represents one edge group
        middle_indices = [6]  # Middle layer positions

        # Check corners
        for cubies in corner_indices:
            if self.array[cubies].color != self.color:
                counter += 1

        # Check edges
        for cubies in edge_indices:
            if any(self.array[i].color != self.color for i in cubies):
                counter += 1

        #Check middle layer
        for cubies in middle_indices:
            if self.array[cubies].color != self.color:
                counter += 1

        return counter

def heuristic_function(left_face, front_face, right_face, bottom_face) -> int:
    left_face_count = left_face.check_cubies()
    front_face_count = front_face.check_cubies()
    right_face_count = right_face.check_cubies()
    bottom_face_count = bottom_face.check_cubies()
    return math.ceil((left_face_count + front_face_count + right_face_count + bottom_face_count) / 9)
```

## Results
This is where the results of the output are detailed:  

The program outputs graphs that show how many nodes are expanded in each trial of a k depth randomized pyraminx. The variance in the results is large because of the nature of the implemented pyraminx (see pyraminx recap).  

This is a list of the average number of nodes and k level I as able to test:

- k = 1: ~2 nodes average
- k = 2: ~5 nodes average
- k = 3: ~26 nodes average
- k = 4: ~90 nodes average 
- k = 5: ~505 nodes average

Because of the ability to modify each row individually, the ability to turn the back corner of the pyraminx, and the ability to turn both clockwise and counter clockwise there are many possible states, and the program crashes at a depth of k=6. Additionally, it is possible for a trial to get "lucky" and have two moves that counter-act each other, like a U1 clockwise move, then a U1 counterclockwise move, which would significantly speed up a trial.


## Learning Outcomes
A discussion of learning outcomes had during this assignment:  

### Technical
Deep Copy vs Shallow copy - Again in this assignment I had difficulty navigating deep copy vs shallow copy when trying to affect the pyraminx. In particular when trying to generate the children I had to redefine functions to make my life easier and allocate extra memory to making sure the configuration of the pyraminx wasn't adversly affected by generating new children.

### Project completing skills
Time estimation - This project took longer than expected, specifically ith implimenting the heuristic correctly. I had to do multiple different trials with different ways of coding my heursting before I was finally able to findd the currently best optimization of it which cut down a 5 rotation trial from about 2 hours to about 10 minutes for my computer.

Documentation - For every function I tried to document the inputs and outputs. The documentation may be repeating information, but I am trying to write enough so that if one just looked at that section of the code they at least understand the inputs and outputs with the documentation.

Pseudocode - Understanding how to implement the A* Algorithm was a long arduous process. It was only after asking chatgpt to generate a tailor-made pseudocode for the project that understanding how to implement it finally clicked. I had to split up implementing the algorithm into many steps, where I implemented functions in the Node class to accomodate them.
