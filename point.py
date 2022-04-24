import pygame

class Point:

    point = (0,0)
    size = (0,0)
    color = (0,0,0)


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

    def mid_point(self,point):
        return ((self.point[0]+point[0])/2, (self.point[1]+point[1])/2)
