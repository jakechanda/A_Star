import random
import Cubies
import math

# Name: Face
# Description: This class will represent a face of the pyraminx
# A face will have a color and an array of values
# A face will have neighbors that will be affected by the rotation
# A face will have a method to check if the face is solved
# A face will have a method to set the neighbors
# A face will have a method to fill the array with a color
class Face:

    # Name: __init__(self, color) -> None:
    # Initializes a Face object with a given color.
    # Parameters:
    # color (str): The color of the face.
    # Returns:
    # None
    def __init__(self, color) -> None:

        self.color = color
        self.array = []

    # Name: generate_cubies(self) -> None:
    # Generates the cubies for the face.
    # Returns:
    # None
    def generate_cubies(self) -> None:
        for i in range(16):
            self.array.append(Cubies.Cubie(i, self.color))

    # Name: check_cubies(self) -> None:
    # Checks the cubies for the face.
    # Returns:
    # None
    def check_cubies(self) -> int:
        counter = 0
        #Define the specific cubie positions for corners and edges, and the middle piece
        corner_indices = [0, 9, 15] 
        #First set represents the designated cubies for the left edge
        #Second set represents designatedd cubies for the right edge
        #Thrid set represents designatedd cubies for the bottom edge
        edge_indices = [(1, 2, 4, 5), (3, 7, 8), (10, 11, 12, 13, 14)] 
        middle_indices = [6] 

        #Check corners
        for corner_cubies in corner_indices:
            if self.array[corner_cubies].color != self.color:
                counter += 1

        #Check edges
        for edge_cubies in edge_indices:
            if any(self.array[i].color != self.color for i in edge_cubies):
                counter += 1

        #Check middle
        for cubies in middle_indices:
            if any(self.array[i].color != self.color for i in middle_indices):
                counter += 1

        return counter

    # Name: output_color(self) -> list:
    # Returns The cubies in the face.
    def output_color(self) -> list:
        return [cubie.color for cubie in self.array]

    # Name: fill_array(self, color) -> None:
    # Fills the array with the given color.
    # Parameters:
    # color (str): The color to fill the array with.
    # Returns:
    # None
    def fill_array(self, color) -> None:
        self.array = [color] * 16    
    
    # Name: is_solved(self) -> bool:
    # Returns whether the face is solved.
    # Returns:
    # bool: True if the face is solved, False otherwise.
    def is_solved(self) -> bool:
        return len(set(self.array)) == 1 and len(self.array) == 16

    # Name: set_neighbors
    # Upper, Left, Right, Back are the planned moves
    # CW, and CCW stand for clockwise and counter-clockwise
    # The neighbors are the faces that are affected by the move
    # The neighbor is the face that the cubies are being moved to given that 
    # rotation, so the upper_cw would be an upper corner piece that is being moved
    # counter clockwise (left)
    def set_neighbors(self, upper_cw, upper_ccw, left_cw, left_ccw, right_cw, right_ccw, back, back_cw, back_ccw) -> None:
        self.upper_cw_neighbor = upper_cw
        self.upper_ccw_neighbor = upper_ccw
        self.left_cw_neighbor = left_cw
        self.left_ccw_neighbor = left_ccw
        self.right_cw_neighbor = right_cw
        self.right_ccw_neighbor = right_ccw
        self.back_neighbor = back
        self.back_cw_neighbor = back_cw
        self.back_ccw_neighbor = back_ccw

# Get input from user
def get_turn() -> str:
    return input('Enter an action: ')

# Get the direction from the user
def get_direction() -> str:
    return input('Enter a direction, 1 for clockwise, 2 for counter clockwise: ')

# Check if the input is valid
def is_valid_input(move) -> bool:
    return move in ["U1","U2","U3","U4","L1","L2","L3","L4","R1","R2","R3","R4","B1","B2","B3","B4"]

# Name: rotate_upper_cw
# Rotate the upper corner of the face clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_back (list): The copied back face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow: 
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the upper clockwise neighbor, and the upper counterclockwise neighbor
# Returns:
# None
def rotate_upper_cw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.upper_ccw_neighbor.array.copy()
    temp_clockwise = face.upper_cw_neighbor.array.copy()
    temp_back = face.back_neighbor.array.copy()

    affected_indexes = []
    
    if user_arg == "U1":
        affected_indexes = [0]
    elif user_arg == "U2":
        affected_indexes = [1,2,3]
    elif user_arg == "U3":
        affected_indexes = [4,5,6,7,8]
    elif user_arg == "U4":
        affected_indexes = [9,10,11,12,13,14,15]
    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in affected_indexes:
        face.array[i] = temp_counterclockwise[i]
        face.upper_cw_neighbor.array[i] = temp_front[i]
        face.upper_ccw_neighbor.array[i] = temp_clockwise[i]

    if(user_arg == "U4"):
        for i in range(16):
            face.back_neighbor.array[i] = temp_back[counterclockwise_rotation[i]]

# Name: rotate_upper_ccw
# Rotate the upper corner of the face counter-clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_back (list): The copied back face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the upper clockwise neighbor, and the upper counterclockwise neighbor
# Returns:
# None
def rotate_upper_ccw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.upper_ccw_neighbor.array.copy()
    temp_clockwise = face.upper_cw_neighbor.array.copy()
    temp_back = face.back_neighbor.array.copy()

    affected_indexes = []
    
    if user_arg == "U1":
        affected_indexes = [0]
    elif user_arg == "U2":
        affected_indexes = [1,2,3]
    elif user_arg == "U3":
        affected_indexes = [4,5,6,7,8]
    elif user_arg == "U4":
        affected_indexes = [9,10,11,12,13,14,15]
    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in affected_indexes:
        face.array[i] = temp_clockwise[i]
        face.upper_cw_neighbor.array[i] = temp_counterclockwise[i]
        face.upper_ccw_neighbor.array[i] = temp_front[i]

    if(user_arg == "U4"):
        for i in range(16):
            face.back_neighbor.array[i] = temp_back[clockwise_rotation[i]]

# Name: rotate_left_cw
# Rotate the left corner of the face clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_right (list): The copied right face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the left clockwise neighbor, and the left counterclockwise neighbor
# Returns:
# None
def rotate_left_cw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.left_ccw_neighbor.array.copy()
    temp_clockwise = face.left_cw_neighbor.array.copy()
    temp_right = face.right_cw_neighbor.array.copy()

    if user_arg == "L1":
        frontaffected_indexes = [9]
        cwaffected_indexes = [15]
        ccwaffected_indexes = [15]
    elif user_arg == "L2":
        frontaffected_indexes = [11,10,4]
        cwaffected_indexes = [14,13,8]
        ccwaffected_indexes = [14,13,8]
    elif user_arg == "L3":
        frontaffected_indexes = [13,12,6,5,1]
        cwaffected_indexes = [12,11,7,6,3]
        ccwaffected_indexes = [12,11,7,6,3]
    elif user_arg == "L4":
        frontaffected_indexes = [15,14,8,7,3,2,0]
        cwaffected_indexes = [10,9,5,4,2,1,0]
        ccwaffected_indexes = [10,9,5,4,2,1,0]
    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in frontaffected_indexes:
        face.array[i] = temp_counterclockwise[clockwise_rotation[i]]

    for j in cwaffected_indexes:
        face.left_cw_neighbor.array[j] = temp_front[counterclockwise_rotation[j]]

    for k in ccwaffected_indexes:
        face.left_ccw_neighbor.array[k] = temp_clockwise[k]

    if(user_arg == "L4"):
        for i in range(16):
            face.right_cw_neighbor.array[i] = temp_right[counterclockwise_rotation[i]]

# Name: rotate_left_ccw
# Rotate the left corner of the face counter-clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_right (list): The copied right face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the left clockwise neighbor, and the left counterclockwise neighbor
# Returns:
# None
def rotate_left_ccw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.left_ccw_neighbor.array.copy()
    temp_clockwise = face.left_cw_neighbor.array.copy()
    temp_right = face.right_cw_neighbor.array.copy()

    if user_arg == "L1":
        frontaffected_indexes = [9]
        cwaffected_indexes = [15]
        ccwaffected_indexes = [15]
    elif user_arg == "L2":
        frontaffected_indexes = [11,10,4]
        cwaffected_indexes = [14,13,8]
        ccwaffected_indexes = [14,13,8]
    elif user_arg == "L3":
        frontaffected_indexes = [13,12,6,5,1]
        cwaffected_indexes = [12,11,7,6,3]
        ccwaffected_indexes = [12,11,7,6,3]
    elif user_arg == "L4":
        frontaffected_indexes = [15,14,8,7,3,2,0]
        cwaffected_indexes = [10,9,5,4,2,1,0]
        ccwaffected_indexes = [10,9,5,4,2,1,0]
    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in frontaffected_indexes:
        face.array[i] = temp_clockwise[clockwise_rotation[i]]

    for j in cwaffected_indexes:
        face.left_cw_neighbor.array[j] = temp_counterclockwise[j]

    for k in ccwaffected_indexes:
        face.left_ccw_neighbor.array[k] = temp_front[counterclockwise_rotation[k]]

    if(user_arg == "L4"):
        for i in range(16):
            face.right_cw_neighbor.array[i] = temp_right[clockwise_rotation[i]]

# Name: rotate_right_cw
# Rotate the right corner of the face clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_left (list): The copied left face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the right clockwise neighbor, and the right counterclockwise neighbor
# Returns:
# None
def rotate_right_cw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.right_ccw_neighbor.array.copy()
    temp_clockwise = face.right_cw_neighbor.array.copy()
    temp_left = face.left_ccw_neighbor.array.copy()

    if user_arg == "R1":
        frontaffected_indexes = [15]
        cwaffected_indexes = [9]
        ccwaffected_indexes = [9]
    elif user_arg == "R2":
        frontaffected_indexes = [14,13,8]
        cwaffected_indexes = [11,10,4]
        ccwaffected_indexes = [11,10,4]
    elif user_arg == "R3":
        frontaffected_indexes = [12,11,7,6,3]
        cwaffected_indexes = [13,12,6,5,1]
        ccwaffected_indexes = [13,12,6,5,1]
    elif user_arg == "R4":
        frontaffected_indexes = [10,9,5,4,2,1,0]
        cwaffected_indexes = [15,14,8,7,3,2,0]
        ccwaffected_indexes = [15,14,8,7,3,2,0]

    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in frontaffected_indexes:
        face.array[i] = temp_counterclockwise[counterclockwise_rotation[i]]

    for j in cwaffected_indexes:
        face.right_cw_neighbor.array[j] = temp_front[clockwise_rotation[j]]

    for k in ccwaffected_indexes:
        face.right_ccw_neighbor.array[k] = temp_clockwise[k]

    if(user_arg == "R4"):
        for i in range(16):
            face.left_ccw_neighbor.array[i] = temp_left[counterclockwise_rotation[i]]

# Name: rotate_right_ccw
# Rotate the right corner of the face counter-clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_left (list): The copied left face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the right clockwise neighbor, and the right counterclockwise neighbor
# Returns:
# None
def rotate_right_ccw(face, user_arg) -> None:
    temp_front = face.array.copy()
    temp_counterclockwise = face.right_ccw_neighbor.array.copy()
    temp_clockwise = face.right_cw_neighbor.array.copy()
    temp_left = face.left_ccw_neighbor.array.copy()

    if user_arg == "R1":
        frontaffected_indexes = [15]
        cwaffected_indexes = [9]
        ccwaffected_indexes = [9]
    elif user_arg == "R2":
        frontaffected_indexes = [14,13,8]
        cwaffected_indexes = [11,10,4]
        ccwaffected_indexes = [11,10,4]
    elif user_arg == "R3":
        frontaffected_indexes = [12,11,7,6,3]
        cwaffected_indexes = [13,12,6,5,1]
        ccwaffected_indexes = [13,12,6,5,1]
    elif user_arg == "R4":
        frontaffected_indexes = [10,9,5,4,2,1,0]
        cwaffected_indexes = [15,14,8,7,3,2,0]
        ccwaffected_indexes = [15,14,8,7,3,2,0]
    else:
        print("Invalid input that made it past the check function")
        return
    
    for i in frontaffected_indexes:
        face.array[i] = temp_clockwise[counterclockwise_rotation[i]]

    for j in cwaffected_indexes:
        face.right_cw_neighbor.array[j] = temp_counterclockwise[j]

    for k in ccwaffected_indexes:
        face.right_ccw_neighbor.array[k] = temp_front[clockwise_rotation[k]]

    if(user_arg == "R4"):
        for i in range(16):
            face.left_ccw_neighbor.array[i] = temp_left[clockwise_rotation[i]]

# Name: rotate_back_cw
# Rotate the back corner of the face clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_back (list): The copied back face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes
# Rotate the face array, the back neighbor, the back clockwise neighbor, and the back counterclockwise neighbor
# Returns:
# None

# Not needed for the pyraminx

def rotate_back_cw(face, user_arg) -> None:
     temp_front = face.array.copy()
     temp_back = face.back_neighbor.array.copy()
     temp_counterclockwise = face.back_ccw_neighbor.array.copy()
     temp_clockwise = face.back_cw_neighbor.array.copy()

     if user_arg == "B1":
         backaffected_indexes = [0]
         cwaffected_indexes = [9]
         ccwaffected_indexes = [15]
     elif user_arg == "B2":
         backaffected_indexes = [1,2,3]
         cwaffected_indexes = [11,10,4]
         ccwaffected_indexes = [14,13,8]
     elif user_arg == "B3":
         backaffected_indexes = [4,5,6,7,8]
         cwaffected_indexes = [13,12,6,5,1]
         ccwaffected_indexes = [12,11,7,6,3]
     elif user_arg == "B4":
         backaffected_indexes = [9,10,11,12,13,14,15]
         cwaffected_indexes = [15,14,8,7,3,2,0]
         ccwaffected_indexes = [10,9,5,4,2,1,0]
     else:
         print("Invalid input that made it past the check function")
         return
    
     for i in backaffected_indexes:
         face.back_neighbor.array[i] = temp_counterclockwise[counterclockwise_rotation[i]]

     for j in cwaffected_indexes:
         face.back_cw_neighbor.array[j] = temp_back[counterclockwise_rotation[j]]

     for k in ccwaffected_indexes:
         face.back_ccw_neighbor.array[k] = temp_clockwise[counterclockwise_rotation[k]]

     if(user_arg == "B4"):
         for i in range(16):
             face.array[i] = temp_front[clockwise_rotation[i]]

# Name: rotate_back_ccw
# Rotate the back corner of the face counter-clockwise
# Parameters:
# face (Face): The face to rotate.
# user_arg (str): The user input.
# Variables:
# temp_front (list): The copied front face.
# temp_counterclockwise (list): The copied counterclockwise face.
# temp_clockwise (list): The copied clockwise face.
# temp_back (list): The copied back face.
# affected_indexes (list): The indexes that are affected by the move.
# clockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# counterclockwise_rotation (list): The mapping of the cubies before the rotation and after the rotation.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the affected indexes

# Not needed for the pyraminx

def rotate_back_ccw(face, user_arg) -> None:
     temp_front = face.array.copy()
     temp_back = face.back_neighbor.array.copy()
     temp_counterclockwise = face.back_ccw_neighbor.array.copy()
     temp_clockwise = face.back_cw_neighbor.array.copy()

     if user_arg == "B1":
         backaffected_indexes = [0]
         cwaffected_indexes = [9]
         ccwaffected_indexes = [15]
     elif user_arg == "B2":
         backaffected_indexes = [1,2,3]
         cwaffected_indexes = [11,10,4]
         ccwaffected_indexes = [14,13,8]
     elif user_arg == "B3":
         backaffected_indexes = [4,5,6,7,8]
         cwaffected_indexes = [13,12,6,5,1]
         ccwaffected_indexes = [12,11,7,6,3]
     elif user_arg == "B4":
         backaffected_indexes = [9,10,11,12,13,14,15]
         cwaffected_indexes = [15,14,8,7,3,2,0]
         ccwaffected_indexes = [10,9,5,4,2,1,0]
     else:
         print("Invalid input that made it past the check function")
         return
    
     for i in backaffected_indexes:
         face.back_neighbor.array[i] = temp_clockwise[clockwise_rotation[i]]

     for j in cwaffected_indexes:
         face.back_cw_neighbor.array[j] = temp_counterclockwise[clockwise_rotation[j]]

     for k in ccwaffected_indexes:
         face.back_ccw_neighbor.array[k] = temp_back[clockwise_rotation[k]]

     if(user_arg == "B4"):
         for i in range(16):
             face.array[i] = temp_front[counterclockwise_rotation[i]]

#Calls random to pick any move from the moves array
def get_random_move() -> str:
    return random.choice(moves)

#Calls random to pick 1 or 2 to determine if it will be spun clockwise or counterclockwise
def get_random_direction() -> str:
    return random.choice(["1", "2"])

def get_random_turn(number_of_turns) -> str:
    for _ in range(number_of_turns): #Creates a chosen number of random moves
        arg = get_random_move()
        direction = get_random_direction()
        print(f"Move: {arg}, Direction: {direction}") #Prints the randomly selected move to the console
        rotate_face(arg, direction, front_face) #Calls def rotate_face to make the randomly selected move

# Print the instructions for the game
def print_instructions() -> None:
    print("Moves!__________________________________________________________")
    print("The first input must be character must be U, L, or R")
    print("followed by an integer between 1 and 4.")
    print("Hit enter and then the second input must be a 1 or 2") 
    print("for the clockwise or counter clockwise rotation.")      
    print("You are always interacting with the front face.")
    print("For instance, U1 will rotate the top layer of the front face clockwise.")
    print("Face changing!____________________________________________________")
    print("Input 'Face' into the console to change the face you are interacting with.")
    print("Then, type the name of the face you want change to the front face.")
    print("Valid faces are: Left, Front, Right, Bottom.")
    print("In order to randomize the pyramid, type 'random' or 'randomize'")
    print("__________________________________________________________________")

# Name: rotate_face
# Rotate the face based on the user input
# Parameters:
# arg (str): The user input.
# direction (str): The direction of the move.
# face (Face): The face to rotate.
# Flow:
# Check the user input and call the appropriate rotation function
# Returns:
# None
def rotate_face(arg, direction, face) -> None:
    if arg[0] == "U" and direction == "1":
        rotate_upper_cw(face, arg)
    elif arg[0] == "U" and direction == "2":
        rotate_upper_ccw(face, arg)
    elif arg[0] == "L" and direction == "1":
        rotate_left_cw(face, arg)
    elif arg[0] == "L" and direction == "2":
        rotate_left_ccw(face, arg)
    elif arg[0] == "R" and direction == "1":
        rotate_right_cw(face, arg)
    elif arg[0] == "R" and direction == "2":
        rotate_right_ccw(face, arg)
    elif arg[0] == "B" and direction == "1":
         rotate_back_cw(face, arg)
    elif arg[0] == "B" and direction == "2":
         rotate_back_ccw(face, arg)
    else:
        pass

# Change the face that the user is interacting with
# Parameters:
# face_arg (str): The face that the user wants to change to the front face.
# front_face (Face): The face that the user is interacting with.
# Variables:
# temp_front (list): The copied front face.
# temp_left (list): The copied left face.
# temp_right (list): The copied right face.
# temp_bottom (list): The copied bottom face.
# Flow:
# Deep Copy all the face arrays to temporary arrays
# Check the user input and set the front face to the desired face
# Maintain the correct neighbors for the faces given the new front face
# Returns:
# None
def change_face(face_arg, front_face) -> None:
    temp_front = front_face.array.copy()
    temp_left = front_face.left_ccw_neighbor.array.copy()
    temp_right = front_face.right_cw_neighbor.array.copy()
    temp_bottom = front_face.back_neighbor.array.copy()
    if face_arg == 'L' or face_arg == 'l' or face_arg == 'Left' or face_arg == 'left': 
        front_face.array = temp_left
        front_face.left_ccw_neighbor.array = temp_right
        front_face.right_cw_neighbor.array = temp_front
        front_face.back_neighbor.array = temp_bottom
        print("Left face is now the front face")
    elif face_arg == 'F' or face_arg == 'f' or face_arg == 'Front' or face_arg == 'front':
        print("Front face is already the front face! Think about it!")
    elif face_arg == 'R' or face_arg == 'r' or face_arg == 'Right' or face_arg == 'right':
        front_face.array = temp_right
        front_face.left_ccw_neighbor.array = temp_front
        front_face.right_cw_neighbor.array = temp_left
        front_face.back_neighbor.array = temp_bottom
        print("Right face is now the front face")
    elif face_arg == 'B' or face_arg == 'b' or face_arg == 'Bottom' or face_arg == 'bottom':
        front_face.array = temp_bottom
        front_face.left_ccw_neighbor.array = temp_right
        front_face.right_cw_neighbor.array = temp_left
        front_face.back_neighbor.array = temp_front
        print("Bottom face is now the front face")
    else:
        print("Invalid input that made it past the Face change check function")

# Check if the game is solved
def solved() -> bool:
    return left_face.is_solved() and front_face.is_solved() and right_face.is_solved() and bottom_face.is_solved()

# Name: heuristic_function
# The heuristic function for the A* algorithm
# It goes through all the faces, and checks the number of cubies that are not the same color as the face
# It then returns the ceiling of number of cubies that are not the same color as the face divided by 9
# Parameters:
# All faces
# Returns:
# int: The heuristic value.
def heuristic_function(left_face, front_face, right_face, bottom_face) -> int:
    left_face_count = left_face.check_cubies()
    front_face_count = front_face.check_cubies()
    right_face_count = right_face.check_cubies()
    bottom_face_count = bottom_face.check_cubies()
    #Dividing by 9 because that is the maximum amount of misplaced corners/edges on a worse case scenario for 1 move needed to solve (a bottom layer rotation)
    return math.ceil((left_face_count + front_face_count + right_face_count + bottom_face_count) / 9)

#Create list of possible moves
moves = ["U1", "U2", "U3", "U4", "L1", "L2", "L3", "L4", "R1", "R2", "R3", "R4", "B1", "B2", "B3", "B4"]

# A mapping of the placement of the cubies before the rotation before a turn (which is the index) and after (value of the index)
# Used in both rotation between faces and within the face on the event of a fourth row turn
# Note: This took a while to map out with the pyraminx
clockwise_rotation = [9, 11, 10, 4, 13, 12, 6, 5, 1, 15, 14, 8, 7, 3, 2, 0]
counterclockwise_rotation = [15, 8, 14, 13, 3, 7, 6, 12, 11, 0, 2, 1, 5, 4, 10, 9]

# Create the faces
# The faces are created with the colors of the face based on the pyraminx given in class
left_face = Face('G')
front_face = Face('B')
right_face = Face('Y')
bottom_face = Face('R')

# Fill the arrays with the colors of the faces
left_face.generate_cubies()
front_face.generate_cubies()
right_face.generate_cubies()
bottom_face.generate_cubies()

# Set the neighbors for each face
left_face.set_neighbors(right_face, front_face, bottom_face, right_face, front_face, bottom_face, bottom_face, right_face, front_face)
front_face.set_neighbors(left_face, right_face, bottom_face, left_face, right_face, bottom_face, bottom_face, left_face, right_face)
right_face.set_neighbors(front_face, left_face, bottom_face, front_face, left_face, bottom_face, bottom_face, front_face, left_face)
bottom_face.set_neighbors(right_face, left_face, front_face, right_face, left_face, front_face, front_face, right_face, left_face)

