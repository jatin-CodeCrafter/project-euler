# project-euler
import turtle

def draw_text(text, colors, start_x, start_y, font_size=40):
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(3)
    pen.penup()
    pen.goto(start_x, start_y)
    
    for i, letter in enumerate(text):
        pen.color(colors[i % len(colors)])  # Cycle through colors
        pen.write(letter, font=("Arial", font_size, "bold"))
        pen.forward(font_size * 0.6)  # Move forward to the next letter
    
    pen.hideturtle()
    screen.mainloop()

text = "Project Euler"
colors = ["red", "blue", "green", "orange", "purple", "brown", "pink"]

draw_text(text, colors, start_x=-150, start_y=0)
