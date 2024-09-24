# Master Pyraminx
A 2D representation of the master pyraminx, a 4x4 triangular pyramid rubix cube  
CS463G Fall 2024

## How to run
Install python 3.12.5  
Navigate to the project folder/directory  
Run the Pyraminx.py python file in a terminal, preferably one with a black background color 
```
python Pyraminx.py
```
In order to run the randomizer, type "random" or "randomize" into the terminal while the program is running

## The Pyraminx
The pyraminx has 4 faces. In this representation a player will only rotate the front face. To make a move, the player must specify a corner, and which layer to turn. The possible corners are the upper corner, the left corner, and the right corner. So the user must input one of the following: U, L, R followed by one of the four layers: 1, 2, 3, 4. Then to specify the direction the user inputs 1 or 2 to specify clockwise or counterclockwise respectively. In the program you interact with the front face, with the ability to change which face the front is so that it is possible to solve the puzzle.

## Data structure
The data structure used to represent the master pyraminx in this project is a class called Face. Four
instances of this object are instantiated in the program, one to represent each side of the pyraminx.
The object instanciates with an array, and a color which represents the initial color of each cubie in
the face. The array at index 0 represent the first row, indexes 1-3, the second row, indexes 4-8, the third,
indexes 9-15, the fourth. Here is a visual representation of how the the data structure is represented:
```
           [0,
         1, 2, 3,
       4, 5, 6, 7, 8,
  9, 10, 11, 12, 13, 14, 15]
```
### Neighbors
Each Face object also has a set of neighbors which are used in the process of rotation. These neighbors are 
references to the array of the other 3 faces of the pyraminx and model one of the configurations of a 
pyraminx given in class. Below is the method used to set the neighbors. With a map of all the neighbors, rotation can
be implemented for each face that affects the correct neighbors.
```
Function name and parameters:
def set_neighbors(self, upper_cw, upper_ccw, left_cw, left_ccw, right_cw, right_ccw, back, back_cw, back_ccw) -> None:

Setting the neighbors:
left_face.set_neighbors(right_face, front_face, bottom_face, right_face, front_face, bottom_face, bottom_face, right_face, front_face)
front_face.set_neighbors(left_face, right_face, bottom_face, left_face, right_face, bottom_face, bottom_face, left_face, right_face)
right_face.set_neighbors(front_face, left_face, bottom_face, front_face, left_face, bottom_face, bottom_face, front_face, left_face)
bottom_face.set_neighbors(right_face, left_face, front_face, right_face, left_face, front_face, front_face, right_face, left_face)
```
### Rotation
For each of the rotation on the front face there is a function that takes the affected faces and applies a transformation
corresponding to the indexes of the affected faces.

- `rotate_upper_cw()`: Rotates the specified upper layers clockwise.
- `rotate_upper_ccw()`: Rotates the specified upper layers counterclockwise.
- `rotate_left_cw()`: Rotates the specified left layers clockwise.
- `rotate_left_ccw()`: Rotates the specified left layers counterclockwise.
- `rotate_right_cw()`: Rotates the specified right layers clockwise.
- `rotate_right_ccw()`: Rotates the specified right layers counterclockwise.

Each rotation transformation between faces can be described as a mapping of indexes before and after rotation, which is what was mapped out, implemented as two arrays, and used in the rotation functions to implement the rotation. 

`clockwise_rotation = [9, 11, 10, 4, 13, 12, 6, 5, 1, 15, 14, 8, 7, 3, 2, 0]`
`counterclockwise_rotation = [15, 8, 14, 13, 3, 7, 6, 12, 11, 0, 2, 1, 5, 4, 10, 9]`

These mappings work both for rotations between faces, and when a fourth layer turn action is taken by the player, the mappings work the rotation of cubies within the needed face.

### Change Faces
The ability to change the current front face is implemented. When the player inputs 'Face' into the application it prompts
them to change the current front face. The program does this by swapping the arrays inside each affected face when changing
faces.

## GUI Output

```
   G          B          Y          R
  GGG        BBB        YYY        RRR
 GGGGG      BBBBB      YYYYY      RRRRR
GGGGGGG    BBBBBBB    YYYYYYY    RRRRRRR
 Left       Front      Right      Bottom
```

## Randomizer
The random library is imported to gain access to randomly selecting contents of an array, and randomly choose between two numbers.
Return random.choice(moves) accesses the array moves to sekect one of the 16 possible moves when called.
Return random.choice(["1", "2"]) to return either 1 or 2 when called.
def get_random_turn() calles both of those commands, and loops itself 20 times (that number can be changed to the desired number of random moves by changing the number in "for _ in range(20)")
After those two commands are called, the two values used to call rotate_face to perform the action of the random move on the front face.

## Heuristic
The goal is to get the Pyraminx into the solved state by having all 4 sides be 1 solid color. We will add up corners, edges, and center pieces and divide them into 9. The number 9 is chosen because in a worst-case scenario the number of misplaced corners, edges, and centers in 1 move is 9. When we implement the heuristic, there will be cubies assigned to corners, edges with the base of the cubie facing the edge making up 1 edge, and a center cubie. On every face, a misplaced corner, edge, and center piece will make up 1 to add to the heuristic. All misplaced values will be added, then divided by 9 to give the final heuristic value for minimum amount of moves to solve the pyraminx. To check if the cubies are in the right place or not, for example, for the blue face, we will check array spots 0, 9, and 15 to see if they are all three colored blue to match the face. 
## Learning Outcomes

### Technical
Deep Copy vs Shallow copy - When setting the neighbors of a face I wanted a pass by reference so that
an action taken one one Face accurately affects and updates the other, but this being python and not C
I had to look into how this works, luckily it's handled and the assignment operator makes a reference in 
memory to the object. When creating the temporary arrays I needed to call the .copy() function which creates
a deep copy that does not affect the original array/list when referenced.
I had to look up library commands for the random library as I have never dealt with that library in python before.

### Project completing skills
Test-Driven- I used a test-driven development style to complete this project. I implemented a feature, then tested it and broke it to find the edge cases, and fixed those, then repeated. I learned this style takes me longer than writing code and then testing it all at once after to find the bugs, but the way I implemented the rotations it seemed like the best way to go about it. One of the rotation values, the back gave too much trouble and it was axed from the project, so I also learned to let things go since it was technically unnecessary.

Time estimation - This project took a lot longer than expected. I learned that I need to estimate time to complete a feature more
liberally because it takes time to test and bug fix.

Documentation - For every function I tried to document the inputs, outputs, and flow of code. This may have resulted in the project becoming unnecessarily long, but I feel I have learned/developed skills to better what it means to describe my code in english.

Heuristic - The heuristic took a lot more thought than I originally anticipated, there would always be 1 or 2 moves that would make it not admissible, or it would be a very low heuristic value that wouldn't be very accurate to the total number of moves, though admissible. 
