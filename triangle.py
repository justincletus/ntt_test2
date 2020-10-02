import random
import graphics

vertices = []
win=graphics.GraphWin("Triangle",500,500)
win.setBackground("white")

img_width = 800;
img_height = 600;

vertices = [img_width*3/10, img_height*2/10, img_width*2/10, img_height*5/10, img_width*4/10, img_height*5/10]

vertices = [int(i) for i in vertices]

axis = []

for i in range(0, len(vertices), 2):
    axis.append(graphics.Point(vertices[i], vertices[i+1]))

vertices2 = [int(img_width*3/10), int(img_height*2/10), 190, 180, 300, 180]
axis2 = []

for i in range(0, len(vertices2), 2):
    axis2.append(graphics.Point(vertices2[i], vertices2[i+1]))

vertices3 = [230, 310, 140, 310, 180, 230]
axis3 = []

for i in range(0, len(vertices3), 2):
    axis3.append(graphics.Point(vertices3[i], vertices3[i+1]))


vertices4 = [300, 230, 340, 310, 250, 310]
axis4 = []

for i in range(0, len(vertices4), 2):
    axis4.append(graphics.Point(vertices4[i], vertices4[i+1]))


triangle = graphics.Polygon(axis)
triangle.setFill('blue')
triangle.draw(win)

triangle = graphics.Polygon(axis2)
triangle.setFill('red')
triangle.draw(win)

triangle = graphics.Polygon(axis3)
triangle.setFill('red')
triangle.draw(win)

triangle = graphics.Polygon(axis4)
triangle.setFill('red')
triangle.draw(win)


win.getMouse()
win.close()