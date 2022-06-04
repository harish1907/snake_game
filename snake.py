from turtle import *

SEGMENT_POSITION = [(0, 0), (20, 0), (40, 0)]
MOVE_STEP = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for i in SEGMENT_POSITION:
            self.add_segments(i)

    def add_segments(self, i):
        new_segments = Turtle(shape="circle")
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(i)
        self.all_segments.append(new_segments)

    def extend(self):
        self.add_segments(self.all_segments[-1].position())

    def move(self):
        for segments in range(len(self.all_segments) - 1, 0, -1):
            x_cor = self.all_segments[segments - 1].xcor()
            y_cor = self.all_segments[segments - 1].ycor()
            self.all_segments[segments].goto(x_cor, y_cor)
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
