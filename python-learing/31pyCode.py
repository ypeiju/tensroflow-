import turtle
print("Drawing a squre...")
turtle.color("Red","Yellow")
turtle.shape("turtle")
turtle.begin_fill()
for t in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.getscreen()._root.mainloop()


