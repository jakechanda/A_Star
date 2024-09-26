import math
import heapq
import Pyraminx
import Face

class Node:
    def __init__(self, parent=None, configuration=None):
        self.parent = parent
        self.configuration = configuration if configuration is not None else Pyraminx.faces_reference

        # Initialize child as None or an empty list if there can be multiple children
        self.child = None

        # g, h, f values
        self.g = 0
        self.h = 0
        self.f = 0

    # Name: get_current_configuration(self)
    # Description: This function will get the current configuration of the Pyraminx
    # Input: None
    # Pyraminx.faces_reference - the faces of the Pyraminx [Face.left_face, Face.front_face, Face.right_face, Face.bottom_face]
    def set_current_configuration(self):
        self.configuration = Pyraminx.faces_reference


    def calculate_costs(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h

    def calculate_heuristic(self):
        self.h = Face.heuristic_function(self.configuration[0], self.configuration[1], self.configuration[2], self.configuration[3])

    def generate_children(self):
        # Generate children
        # For each child, calculate g, h, f values
        # Return the list of children

        children = []
        possible_moves = self.possible_moves()
        clockwise = '1'
        counterclockwise = '2'

        for move in possible_moves:
            Pyraminx.faces_reference = self.configuration
            child = Node(self, self.configuration)
            child.apply_move(move, clockwise, Face.front_face)
            child.set_current_configuration()
            child.calculate_heuristic()
            children.append(child)

        Pyraminx.faces_reference = self.configuration
        
        for move in possible_moves:
            Pyraminx.faces_reference = self.configuration
            child = Node(self, self.configuration)
            child.apply_move(move, counterclockwise, Face.front_face)
            child.set_current_configuration()
            child.calculate_heuristic()
            children.append(child)
        
        Pyraminx.faces_reference = self.configuration

        return children

    def possible_moves(self) -> list:
        # Get the possible moves for the current configuration
        possible_moves = Face.moves
        return possible_moves

    def apply_move(self, arg, direction, face):
        # Apply the move to the current configuration
        Face.rotate_face(arg, direction, face)
        Pyraminx.faces_reference = [Face.left_face, Face.front_face, Face.right_face, Face.bottom_face]

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
    closed_list = set()

    # Add the start node to the open list
    heapq.heappush(open_list, (start_pyraminx.f, start_pyraminx))

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)[1]

        # If the goal is reached, reconstruct the path and return it
        if current_node.configuration == goal_pyraminx.configuration:
            path = []
            while current_node:
                path.append(current_node.configuration)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Add the current node to the closed list
        closed_list.add(tuple(map(tuple, current_node.configuration)))

        # Generate children
        children = current_node.generate_children()

        for child in children:
            if tuple(map(tuple, child.configuration)) in closed_list:
                continue

            # Calculate g, h, f values
            child.calculate_costs(current_node.g + 1, child.calculate_heuristic())

            # Check if child is already in open list with a higher g value
            for open_node in open_list:
                if child == open_node[1] and child.g > open_node[1].g:
                    break
            else:
                heapq.heappush(open_list, (child.f, child))

    return None  # If no path is found


list = Node()
children = list.generate_children()

for child in children:
    print(child.h)