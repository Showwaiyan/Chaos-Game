# Module import start
import pygame
# Module import end

class Point:
    # Points that are represent for the random three point on the screen

    point = (0,0) # coordinate
    size = (0,0) # icon size
    color = (0,0,0) # RGB color


    def __init__(self, size, point, color):
        self.size = size
        self.point = point
        self.color = color

    def get_point(self):
        return self.point

    def get_size(self):
        return self.size

    def get_color(self):
        return self.color

    def mid_point(self,point): # The mid point formula
        return ((self.point[0]+point[0])/2, (self.point[1]+point[1])/2)
