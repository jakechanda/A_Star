import math
import heapq
import Pyraminx
import Face
import copy

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
            print(move + ' ' + 'clockwise')
            print(child.h)
            children.append(child)
        
        self.reset_faces()
        
        for move in possible_moves:
            self.reset_faces()
            child = Node(self, self.configuration)
            child.apply_move(move, counterclockwise, Face.front_face)
            child.set_current_configuration()
            child.calculate_heuristic()
            print(move + ' ' + 'counterclockwise')
            print(child.h)
            children.append(child)
        
        self.reset_faces()

        return children

    def possible_moves(self) -> list:
        # Get the possible moves for the current configuration
        possible_moves = Face.moves
        return possible_moves

    def apply_move(self, arg, direction, face):
        # Apply the move to the current configuration
        Face.rotate_face(arg, direction, face)
        self.set_faces()
        Pyraminx.faces = [Face.left_face.output_color(), Face.front_face.output_color(), Face.right_face.output_color(), Face.bottom_face.output_color()]

    def reset_faces(self):
        Face.left_face.array = self.left.copy()
        Face.front_face.array = self.front.copy()
        Face.right_face.array = self.right.copy()
        Face.bottom_face.array = self.bottom.copy()

    def set_faces(self):
        self.left, self.front, self.right, self.bottom = self.deepcopy_arrays()

    def __eq__(self, other):
        return self.left == other.left and self.front == other.front and self.right == other.right and self.bottom == other.bottom

    def __hash__(self):
        return hash((tuple(map(tuple, self.left)), tuple(map(tuple, self.front)), tuple(map(tuple, self.right)), tuple(map(tuple, self.bottom))))

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

    while open_list:
        # Get the node with the lowest f value
        current_node = heapq.heappop(open_list)[1]

        # If the goal is reached, reconstruct the path and return it
        if current_node == goal_pyraminx:
            path = []
            while current_node:
                path.append(current_node)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        # Add the current node to the closed list
        closed_list.append(current_node)

        # Generate children
        children = current_node.generate_children()

        for child in children:
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

    goal_pyraminx = Node()
    goal_pyraminx.set_current_configuration()
    goal_pyraminx.calculate_heuristic()

    Face.get_random_turn()

    start_pyraminx = Node()
    start_pyraminx.set_current_configuration()
    start_pyraminx.calculate_heuristic()



    path = A_Star(start_pyraminx, goal_pyraminx)
    if path is None:
        print("No path found")
    else:
        print("Path found:")
        for configuration in path:
            print(configuration)
            left = [cubie.color for cubie in configuration.left]
            front = [cubie.color for cubie in configuration.front]
            right = [cubie.color for cubie in configuration.right]
            bottom = [cubie.color for cubie in configuration.bottom]
            Pyraminx.faces = [left, front, right, bottom]
            Pyraminx.craft_pyramid()
    
if __name__ == '__main__':
    main()