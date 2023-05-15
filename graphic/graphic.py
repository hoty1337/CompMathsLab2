import numpy as np
import matplotlib.pyplot as plt


def plot_math_function(func, x_min, x_max, num_points=1000):
	x_values = np.linspace(x_min, x_max, num_points)
	y_values = func(x_values)

	plt.plot(x_values, y_values)

	plt.axhline(0, color='black', linewidth=0.5)
	plt.axvline(0, color='black', linewidth=0.5)
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('y = f(x)')
	plt.grid(True)
	plt.show()


def plot_math_function_sys(funcs, num_points=1000):
	x = []
	y = []
	i = 0
	for f in funcs:
		x.append(np.linspace(f[1][0], f[1][1], num_points))
		y.append(f[0](x[i]))
		i += 1

	for j in range(len(x)):
		plt.plot(x[j], y[j])
	plt.axhline(0, color='black', linewidth=0.5)
	plt.axvline(0, color='black', linewidth=0.5)
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('y = f(x)')
	plt.grid(True)
	plt.show()


def plot_sys_3d(funcs, num_points=1000):
	x = np.linspace(-np.pi, np.pi, 50)
	y = x
	z = np.cos(x)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot(x, y, z)
