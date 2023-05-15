from method.methods import *
from math import sin
from graphic.graphic import plot_math_function, plot_math_function_sys
from pandas import DataFrame


def f1(x):
	return 0.4 * x * x * x + 3 * x * x + x - 13


def f2(x):
	return sin(x) + 0.1


def f3(x):
	return 3 * x ** 3 + 1.7 * x ** 2 - 15.42 * x + 6.89


def f1_1(x):
	return 0.4 * x * x * x + 3 * x * x + x - np.full(len(x), 13)


def f2_1(x):
	return np.sin(x) + np.full(len(x), 0.1)


def f3_1(x):
	return 3 * x ** 3 + 1.7 * x ** 2 - 15.42 * x + np.full(len(x), 6.89)


def fsys1(x):
	x1 = x[0] * x[0] + x[1] * x[1] - 4
	x2 = x[0] * x[0] - x[1] * x[1] - 1
	return np.asarray([x1, x2])


def fsys1_1(x):  # -2 2
	return np.sqrt(np.full(len(x), 4) - np.multiply(x, x))


def fsys1_2(x):  # -2 2
	return -np.sqrt(np.full(len(x), 4) - np.multiply(x, x))


def fsys1_3(x):
	return np.sqrt(np.multiply(x, x) - np.full(len(x), 1))


def fsys1_4(x):
	return -np.sqrt(np.multiply(x, x) - np.full(len(x), 1))


def fsys2(x):
	x1 = x[0] * x[0] + x[1] * x[1] - 4
	x2 = x[0] - x[1] + 1
	return np.asarray([x1, x2])


def fsys2_1(x):  # -2 2
	return np.sqrt(np.full(len(x), 4) - np.multiply(x, x))


def fsys2_2(x):  # -2 2
	return -np.sqrt(np.full(len(x), 4) - np.multiply(x, x))


def fsys2_3(x):
	return x + np.full(len(x), 1)


def fsys3(x):
	x1 = x[0] * x[0] + x[1] * x[1] + x[2] * x[2] - 4
	x2 = x[0] * x[0] + x[1] * x[1] - x[2] * x[2] - 2
	x3 = x[0] + 2 * x[1] - x[2] - 1
	return np.asarray([x1, x2, x3])


def main():
	choose = int(input(
		"выбор уравнений и систем\n1) 0.4*x^3+3*x^2+x=13\n2) sin(x)=-0.1\n3) 3x^3 + 1,7x^2 − 15,42x + 6,89=0\n4) x^2+y^2=4, x^2-y^2=1\n5) x^2+y^2=4, x-y=-1\n6) x^2+y^2+z^2=4, x^2+y^2-z^2=2, x+2*y-z=1\n"))

	eps = float(input("epsilon for methods\n"))
	if choose <= 3:
		left = float(input("left for secant method\n"))
		right = float(input("right for secant method\n"))
		x = float(input("x for fixed point method\n"))
		f = 0
		f_graph = 0
		if choose == 1:
			f = f1
			f_graph = f1_1

		if choose == 2:
			f = f2
			f_graph = f2_1

		if choose == 3:
			f = f3
			f_graph = f3_1
		if left >= right:
			print("left >= right")
			return

		if f(left) * f(right) >= 0:
			print("have not solve or have many solve on this segment")

		x_ch, f_x_ch, iter_ch, table_ch, check_ch = chord_method(left, right, f, eps)
		x_it, f_x_it, iter_it, table_it, check_it = iteration_method(x, f, eps)
		plot_math_function(f_graph, left, right)
		if check_ch:
			print(DataFrame(table_ch[1:], columns=table_ch[0]))
			print('\n-----------------\n')
			print("x=", x_ch, " fx=", f_x_ch, ' iter=', iter_ch)
		if check_it:
			print(DataFrame(table_it[1:], columns=table_it[0]))
			print('\n-----------------\n')
			print("x=", x_it, " fx=", f_x_it, ' iter=', iter_it)
		else:
			print("iteration method can't solve")

	else:
		f = 0
		x = [float(input('x1= ')), float(input('x2= '))]
		if choose == 6:
			x.append(float(input('x3= ')))
			f = fsys3

		if choose == 4:
			f = fsys1
			funcs = [[fsys1_1, (-2, 2)], [fsys1_2, (-2, 2)], [fsys1_3, (-5, -1)], [fsys1_4, (1, 5)], [fsys1_3, (1, 5)],
							 [fsys1_4, (-5, -1)]]
			plot_math_function_sys(funcs)
		if choose == 5:
			f = fsys2
			funcs = [[fsys2_1, (-2, 2)], [fsys2_2, (-2, 2)], [fsys2_3, (-3, 3)]]

			plot_math_function_sys(funcs)
		x = np.asarray(x)
		x0, Newton_table, check = Newton_method(f, x, eps)
		if check:
			print(Newton_table[0])
			nt = Newton_table[1:]
			for i in nt:
				print('x_v =', i[0])
				print('fx_v =', i[1])
				print('norm2=', i[2])
			print('\n-----------------\nresult=', x0, ' iter=', len(nt))

		else:
			print("can't solve")


if __name__ == '__main__':
	main()
