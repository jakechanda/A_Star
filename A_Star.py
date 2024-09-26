import math
import heapq
import Pyraminx
import Face

class Node:
    def __init__(self, parent=None, configuration=None):
        self.parent = parent
        self.configuration = configuration if configuration else self.get_current_configuration()

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
    def get_current_configuration(self):
        self.configuration = Pyraminx.faces_reference

    def calculate_costs(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h

    def calculate_heuristic(self):
        self.h = Face.heuristic_function(self.configuration[0], self.configuration[1], self.configuration[2], self.configuration[3])

list = Node()
list.get_current_configuration()
list.calculate_heuristic()
print(list.configuration)
print(list.h)