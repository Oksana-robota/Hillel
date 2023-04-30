import json


# 1
class JsonParser:

    def __init__(self, obj):
        self.object = obj

    def __enter__(self):
        return json.loads(self.object)

    def __exit__(self, type, value, traceback):
        pass


# 2
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


# 3
class Rectangle:

    def __init__(self, start_point_left, end_point_right):
        self.start_point = start_point_left
        self.end_point = end_point_right

    def contains(self, obj):
        if self.start_point.x <= obj.x <= self.end_point.x and self.start_point.y <= obj.y <= self.end_point.y:
            return True
        return False

    def __contains__(self, obj):
        if self.start_point.x <= obj.x <= self.end_point.x and self.start_point.y <= obj.y <= self.end_point.y:
            return True
        return False
