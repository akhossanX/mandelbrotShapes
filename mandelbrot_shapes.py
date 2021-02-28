import	turtle
import	sys


def init():
	""" Initializes the turtle canvas """

	return	turtle.Turtle()


def	draw_mandelbrot_shape(nodes=10, times_table=2, radius=200):
	"""
		Draws a Mandelbrot shape given a set of params:
		nodes: number of equally-spaced points on the edge of the circle
		times_table: nodes to multiply by.
		radius: the radius of the mandelbrot circle.
	"""

	# Initializing turtle canvas
	t = init()
	t.ht()
	t.speed(0)
	# Sets a color for the circle
	t.color('black', 'black')
	t.up()
	# Moving turtle up by radius units
	t.goto(0, -radius)
	t.left(180)
	t.down()
	# Recording shape coordinates
	t.begin_poly()
	# Drawing the mandelbrot circle
	t.begin_fill()
	t.circle(-radius, steps=nodes)
	t.end_fill()
	# Stop recording coordinates
	t.end_poly()
	# Store coordinate in a list of coordinates
	l_coordinates = list(t.get_poly())
	# Delete the last element
	l_coordinates.pop(nodes)

	t.color(sys.argv[1])
	# Drawing mandelbrot shape
	for i in range(nodes):
		t.down()
		t.goto(l_coordinates[(i * times_table) % nodes])
		t.up()
		if i + 1 < nodes:
			t.goto(l_coordinates[i + 1])
	
	turtle.mainloop()
	
if __name__ == "__main__":

	draw_mandelbrot_shape(nodes=200, times_table=int(sys.argv[3]), radius=int(sys.argv[2]))
