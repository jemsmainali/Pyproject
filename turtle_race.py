import turtle
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'yellow', 'black', 'purple', 'pink', 'orange', 'brown', 'blue', 'cyan']


def get_number_of_racer():
    while True:
        racers = input("Enter the number of racers (2–10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
        print("Invalid input. Please enter a number between 2 and 10.")


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing Game!")
    return screen


def create_turtles(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.setheading(90)
        racer.goto(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            racer.forward(random.randint(1, 20))
            x, y = racer.pos()
            if y >= HEIGHT//2 - 20:
                return colors[turtles.index(racer)]


racers = get_number_of_racer()
random.shuffle(COLORS)
colors = COLORS[:racers]

screen = init_turtle()
winner = race(colors)

print("🏆 The winner is:", winner)
turtle.done()
