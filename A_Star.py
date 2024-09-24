import math
import heapq
import Pyraminx

class Node:
    def __init__(self):
        # Parent Node
        self.parent = 1
        self.configuration = 1

        # Generate the child configuration
        self.child = 0

        # g, h, f values
        self.g = 1
        self.h = 1
        self.f = 1

        
