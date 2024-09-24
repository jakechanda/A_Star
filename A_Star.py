import math
import heapq
import Pyraminx

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

    def get_current_configuration(self):
        self.configuration = Pyraminx.faces

    def calculate_costs(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h