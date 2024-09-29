import math
import heapq
import Pyraminx
import Face
import copy
import matplotlib.pyplot as plt

class Node:
    def __init__(self, parent=None, configuration=None):
        self.parent = parent
        self.configuration = configuration if configuration is not None else Pyraminx.faces_reference
        self.left, self.front, self.right, self.bottom = self.deepcopy_arrays()
        # Initialize child as None or an empty list if there can be multiple children
        self.child = None

        # g, h, f values
        self.g = 0
        self.h = 0
        self.f = 0

    # Name: __lt__(self, other)
    # Description: This function will compare the f values of two nodes
    # Input: other - the other node to compare
    # Used in: heapq.heappush(open_list, (child.f, child))
    def __lt__(self, other):
        return self.f < other.f

    # Name: get_current_configuration(self)
    # Description: This function will get the current configuration of the Pyraminx
    # Input: None
    # Pyraminx.faces_reference - the faces of the Pyraminx [Face.left_face, Face.front_face, Face.right_face, Face.bottom_face]
    def set_current_configuration(self):
        self.configuration = Pyraminx.faces_reference

    # Name: deepcopy_arrays(self)
    # Description: This function will deepcopy the arrays of the Pyraminx
    def deepcopy_arrays(self):
        return [Face.left_face.array.copy(), Face.front_face.array.copy(), Face.right_face.array.copy(), Face.bottom_face.array.copy()]

    def calculate_costs(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h

    def calculate_heuristic(self):
        self.h = Face.heuristic_function(self.configuration[0], self.configuration[1], self.configuration[2], self.configuration[3])

    # Name: generate_children(self)
    # Description: This function will generate the children of the current node
    # Input: None
    # Flow:
    # For each child generated, calculate the heuristic value
    # Make sure the faces are reset after each child is generated
    # Return: children - the list of children of the current node
    def generate_children(self):
        # Generate children
        # For each child, calculate g, h, f values
        # Return the list of children

        children = []
        possible_moves = self.possible_moves()
        clockwise = '1'
        counterclockwise = '2'

        for move in possible_moves:
            self.reset_faces()
            child = Node(self, self.configuration)
            child.apply_move(move, clockwise, Face.front_face)
            child.set_current_configuration()
            child.calculate_heuristic()
            children.append(child)
        
        self.reset_faces()
        
        for move in possible_moves:
            self.reset_faces()
            child = Node(self, self.configuration)
            child.apply_move(move, counterclockwise, Face.front_face)
            child.set_current_configuration()
            child.calculate_heuristic()
            children.append(child)
        
        self.reset_faces()

        return children

    # Name: possible_moves(self) -> list
    # Description: This function will return the possible moves for the current configuration
    # Input: None
    # Output: possible_moves - the possible moves for the current configuration
    def possible_moves(self) -> list:
        # Get the possible moves for the current configuration
        possible_moves = Face.moves
        return possible_moves

    # Name: apply_move(self, arg, direction, face)
    # Description: This function will apply a move to the current configuration
    # Input: arg - the move to apply
    #        direction - the direction of the move
    #        face - the face to apply the move to
    # The move is applied to the current configuration
    def apply_move(self, arg, direction, face):
        # Apply the move to the current configuration
        Face.rotate_face(arg, direction, face)
        self.set_faces()

    # Name: reset_faces(self)
    # Description: This function will reset the faces of the Pyraminx to the current configuration
    # Input: None
    # The faces of the Pyraminx are reset to the current configuration so that the moves can be applied correctly
    def reset_faces(self):
        Face.left_face.array = self.left.copy()
        Face.front_face.array = self.front.copy()
        Face.right_face.array = self.right.copy()
        Face.bottom_face.array = self.bottom.copy()

    # Name: set_faces(self)
    # Description: This function will set the faces of the Pyraminx to the current configuration
    # Input: None
    # There are so many references to objects in the Pyrminx and Faces program that it is just easier
    # to make a new function that for sure deep copies the arrays
    def set_faces(self):
        self.left, self.front, self.right, self.bottom = self.deepcopy_arrays()

    # Name: __eq__(self, other)
    # Description: This function will compare the current configuration of the Pyraminx with another configuration
    # Input: other - the other configuration to compare
    # This function will return True if the configurations are the same
    def __eq__(self, other):
        return self.left == other.left and self.front == other.front and self.right == other.right and self.bottom == other.bottom

# list = Node()
# list.set_current_configuration()
# list.calculate_heuristic()
# print(list.configuration)
# print(list.h)

# Pyraminx.test()

def A_Star(start_pyraminx, goal_pyraminx):
    # Initialize the open list
    open_list = []
    # Initialize the closed list
    closed_list = []

    # Add the start node to the open list
    heapq.heappush(open_list, (start_pyraminx.f, start_pyraminx))


    # Counter to track how many nodes were expanded
    nodes_expanded = 0


    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)[1]
        nodes_expanded += 1

        # If the goal is reached, reconstruct the path and return it
        if current_node == goal_pyraminx:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1], nodes_expanded  # Return reversed path

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Generate children
        children = current_node.generate_children()

        for child in children:
            # Check if child is in closed list
            if any(child == closed_node for closed_node in closed_list):
                continue

            # Calculate g, h, f values
            child.calculate_costs(current_node.g + 1, child.h)

            # Check if child is already in open list with a higher g value
            for open_node in open_list:
                if child == open_node[1] and child.g > open_node[1].g:
                    break
            else:
                heapq.heappush(open_list, (child.f, child))

    return None  # If no path is found


def main():


    print("Welcome to the A* Pyraminx Solver!")
    print("Please input k, the number of moves you would like to randomize the Pyraminx by")
    k = int(input())
    results = []
    print("Randomizing the Pyraminx by " + str(k) + " moves...")

    print("There will be five trials done with the Pyraminx being randomized by " + str(k) + " moves")


    node_counts = []

    # Initialize the goal Pyraminx when the pyraminx is solved
    goal_pyraminx = Node()
    goal_pyraminx.set_current_configuration()
    goal_pyraminx.calculate_heuristic()
    # Values k = 3 to 20
    for k in range(3, 20):

        print("Welcome to the pyramid randomized by " + str(k) + " turns trials")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        results = []

        for trial in range(5):

            print("This is trial number " + str(trial + 1))

            Face.left_face.array = goal_pyraminx.left.copy()
            Face.front_face.array = goal_pyraminx.front.copy()
            Face.right_face.array = goal_pyraminx.right.copy()
            Face.bottom_face.array = goal_pyraminx.bottom.copy()

            # Randomize the Pyraminx
            Face.get_random_turn(k)

            start_pyraminx = Node()
            start_pyraminx.set_current_configuration()
            start_pyraminx.calculate_heuristic()

            # Call A_Star to solve the pyraminx
            path, nodes_expanded = A_Star(start_pyraminx, goal_pyraminx)

            if path is None:
                print("No path found")
            else:
                print("Path found:")
                results.append(nodes_expanded)

                # Print the path
                # For each configuration in the path, format the GUI and output the configuration
                for configuration in path:

                    # Format GUI
                    left = [cubie.color for cubie in configuration.left]
                    front = [cubie.color for cubie in configuration.front]
                    right = [cubie.color for cubie in configuration.right]
                    bottom = [cubie.color for cubie in configuration.bottom]
                    Pyraminx.faces = [left, front, right, bottom]

                    # Output configuration
                    Pyraminx.craft_pyramid()
                    # Calculate the average number of nodes expanded for this value of k
            print("The nodes expanded for trial " + str(trial + 1) + " is " + str(nodes_expanded))

        if results:    
            plot_results(results, k)




def plot_results(results, k):
    # Create a list for trial numbers (1 to 5)
    trial_numbers = list(range(1, len(results) + 1))

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(trial_numbers, results, marker='o', linestyle='-', color='b')
    plt.xlabel('Trial Number')
    plt.ylabel('Nodes Expanded')
    plt.title(f'Nodes Expanded in Each Trial for k={k} (A* on Pyraminx)')
    plt.grid(True)
    plt.xticks(trial_numbers)  # Ensure only integer trial numbers are shown on the x-axis
    # Determine the step size for y-axis ticks
    step_size = max(1, (max(results) - min(results)) // 10)
    plt.yticks(range(min(results), max(results) + 1, step_size))
    plt.savefig(f'plot_k_{k}.png')
    print(f"Plot saved as plot_k_{k}.png")
    # plt.show()


if __name__ == '__main__':
    main()