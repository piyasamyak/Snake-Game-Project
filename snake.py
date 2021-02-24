from turtle import Turtle, Screen
INITIAL_SEGS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake(INITIAL_SEGS)
        self.head = self.snake[0]

    # Create a Snake body
    def create_snake(self, num_of_segments=1):
        for new_segment in range(len(self.snake), len(self.snake) + num_of_segments, 1):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            self.snake.append(new_segment)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_xcor = self.snake[seg - 1].xcor()
            new_ycor = self.snake[seg - 1].ycor()
            self.snake[seg].setpos(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)


    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)



