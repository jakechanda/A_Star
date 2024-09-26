import Face

# ANSI color codes
color_map = {
    'G': '\033[92m',  # Green
    'B': '\033[94m',  # Blue
    'R': '\033[91m',  # Red
    'Y': '\033[93m',  # Yellow
    'ENDC': '\033[0m' # Reset to default color
}

# List of faces
global faces
faces = [Face.left_face.output_color(), Face.front_face.output_color(), Face.right_face.output_color(), Face.bottom_face.output_color()]
faces_reference = [Face.left_face, Face.front_face, Face.right_face, Face.bottom_face]

# Number of layers in the pyramid
layers = 4

# Name: def craft_pyramid() -> None:
# Description: This function will print the entire pyramid
# It will loop through each layer and print the row
# Input: None
# Variables:
# i - the current layer of the pyramid
# Flow:
# Loop through each layer
# Call the print_row function to print the row of the pyramid
# Print the labels for the faces of the pyramid
# Return: None
def craft_pyramid() -> None: 
    # Loop through each layer
    for i in range(layers):
        print_row(i)
    print(' ' + 'Left' + ' ' * 7 + 'Front' + ' ' * 6 + 'Right' + ' ' * 6 + 'Bottom')

# Name: def print_row(iterator) -> None:
# Description: This function will print a row of the pyramid
# This function will print a row of the pyramid
# Input: iterator - the current layer of the pyramid
#        j_terator - the current face of the pyramid to print
#        k_terator - the current position in the face array
# Variables:
# j_terator - the current face of the pyramid to print
# k_terator - the current position in the face array
# Flow:

def print_row(iterator) -> None:

    k_terator = reset_iterator(iterator)

    for j_terator in range(layers):
        
        print(' ' * (layers - iterator - 1), end='')

        # Print the character with color
        # char gets the value from the face array of the index j_terator (the array of faces) and k_terator (the array containing the values in the face)
        # color gets the value from the color_map of the character in char
        # The character is printed in the color specified by the color_map
        # The k_terator is incremented to move to the next character in the face array

        for _ in range(2 * iterator + 1):
            char = faces[j_terator][k_terator]
            color = color_map[char]
            print(color + char, end='')
            k_terator += 1
        k_terator = reset_iterator(iterator)
        print(color_map['ENDC'], end='')

        print(' ' * (layers - iterator + 3), end='')
    # Print a new line after each row is printed
    print()

# This is a switch statement to reset the third iterator I use
# to track the position of the character in the face array
# Input: iterator - the current layer of the pyramid
# Output: the reset value of the iterator
# The output value corresponds to the starting index of the 
# first character in the layer of the pyramid
def reset_iterator(iterator: int) -> int:
    if iterator == 0:
        return 0
    elif iterator == 1:
        return 1
    elif iterator == 2:
        return 4
    elif iterator == 3:
        return 9
    else:
        return -1

# Name: def play_game() -> tuple:
# Description: This function will play the game, taking in user input
# Input: None
# Variables:
# arg - the user input for the move
# direction - the direction of the move
# Flow:
# Get the user input for the move
# Check if the user wants to quit the game
# Check if the user wants to see the instructions
# Check if the user wants to randomize the pyramid
# Check if the user wants to change the front face of the pyramid
# Check if the user input is valid
# Get the direction of the move
# Return: a tuple of the move and the direction
def play_game() -> tuple:
    arg = Face.get_turn()
    if arg == 'q' or arg == 'Q' or arg == 'quit' or arg == 'Quit' or arg == 'exit' or arg == 'Exit': 
        print("Goodbye!")
        exit()
    elif arg == 'help':
        Face.print_instructions()
        direction = "1"
        return arg, direction
    elif arg == 'randomize' or arg == 'random':
        Face.get_random_turn()
        direction = "1"
        return arg, direction
    elif arg == 'Face':
        face_arg = input("Enter the name of the face you want change to the front face: ")
        valid_faces = ["L", "l", "Left", "left", "F", "f", "Front", "front", "R", "r", "Right", "right", "B", "b", "Bottom", "bottom"]
        while face_arg not in valid_faces:
            print("Invalid input, please try again")
            face_arg = input("Enter the face you want change to the front face: ")
        direction = "1"  
        Face.change_face(face_arg, Face.front_face)
        global faces
        faces = [Face.left_face.array, Face.front_face.array, Face.right_face.array, Face.bottom_face.array]
        return arg, direction

    while not Face.is_valid_input(arg):
        print("Invalid input, please try again")
        print("The first character must be U, L, or R followed by an integer between 1 and 4")
        arg = Face.get_turn()

    direction = Face.get_direction()

    while not ['1', '2'].__contains__(direction):
        print("Invalid input, please try again")
        print("The input must be 1 or 2")
        direction = Face.get_direction()
            
    return arg, direction

# Main function
# Flow:
# Print the welcome message
# Take in the user input for the move
# Goto the play_game function
# Rotate the face based on the user input
# Print the pyraminx
# Return: None
def main():
    print("Welcome to the Pyraminx!")
    print("Please enter help for instructions on how to play the game.")
    print("Enter q to exit the game!")
    craft_pyramid()
    while True:

        arg, direction = play_game()

        if arg == 'Face' or arg == 'help':
            craft_pyramid()
            continue

        Face.rotate_face(arg, direction, Face.front_face)
        global faces
        faces = [Face.left_face.output_color(), Face.front_face.output_color(), Face.right_face.output_color(), Face.bottom_face.output_color()]
        craft_pyramid()
        print("Heuristic value: " + str(Face.heuristic_function(Face.left_face, Face.front_face, Face.right_face, Face.bottom_face)))

def test():
    Face.rotate_face('U1', '1', Face.front_face)
    global faces
    faces = [Face.left_face.output_color(), Face.front_face.output_color(), Face.right_face.output_color(), Face.bottom_face.output_color()]
    craft_pyramid()
    print("Heuristic value: " + str(Face.heuristic_function(Face.left_face, Face.front_face, Face.right_face, Face.bottom_face)))