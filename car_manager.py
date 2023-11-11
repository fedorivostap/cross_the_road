from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for _ in range(20):
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto((random.randint(300, 900), random.randint(-290, 290)))
            self.cars.append(new_car)

    def increase_new_level_speed(self):
        self.speed += MOVE_INCREMENT

    def move(self):
        for car in self.cars:
            curr_x_cor = car.xcor()
            curr_x_cor -= self.speed
            car.setx(curr_x_cor)
            if car.xcor() < -320:
                car.goto((random.randint(300, 900), random.randint(-290, 290)))
