import numpy as np
from util.util import derivative


def chord_method(a, b, f, e, cnt_iter=100):
    if f(b) * derivative(2, a, f) < 0:
        point_0 = a
        x = b
    elif f(a) * derivative(2, a, f) < 0:
        point_0 = b
        x = a
    else:
        x = a - (b - a) / (f(b) - f(a)) * f(a)
        point_0 = None

    x_flag = x + 2 * e
    table_iter = [['a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', 'd'], [a, b, x, f(a), f(b), f(x), abs(a - b)]]
    current_cnt = 0

    while current_cnt < cnt_iter and abs(x - x_flag) > e:
        if point_0 is None:
            if f(a) * f(x) < 0:
                b = x
            else:
                a = x
            x, x_flag = a - (b - a) / (f(b) - f(a)) * f(a), x
            table_iter.append([a, b, x, f(a), f(b), f(x), abs(x - x_flag)])
        else:
            x, x_flag = x - (point_0 - x) / (f(point_0) - f(x)) * f(x), x
            if point_0 == a:
                table_iter.append([point_0, x, x, f(point_0), f(x), f(x), abs(x - x_flag)])
            else:
                table_iter.append([x, point_0, x, f(x), f(point_0), f(x), abs(x - x_flag)])
        current_cnt += 1

    return x, f(x), current_cnt, table_iter, current_cnt==cnt_iter


def iteration_method(x0, f, e, cnt_iter=100):
    def g(g_x):
        return g_x + (-1 / derivative(1, g_x, f)) * f(g_x)
        # -2 < C*f'(x) < 0
        # -2/f'(x) < C < 0
        # c = -1/f'(x)
        # выбор оптимального С по методу релаксации сводиться к методу Ньютона

    x = g(x0)
    table_iter = [['xk', 'xk_1', 'fx', 'd'], [x0, x, f(x), abs(x - x0)]]

    current_cnt = 0
    while abs(x - x0) > e and current_cnt < cnt_iter:
        if derivative(1, x, g) >= 1:
            return x,f(x),current_cnt,table_iter,False
        x0, x = x, g(x)
        table_iter.append([x0, x, f(x), abs(x - x0)])
        current_cnt += 1

    return x, f(x), current_cnt, table_iter,True


def Newton_method(f, x0, e=1e-6, cnt_iter=100):
    x = x0.copy()
    n = len(x)
    Newton_table = [['x_v', 'fx_v', 'xk - xk_1']]
    for i in range(cnt_iter):
        fx = f(x)
        dx = np.zeros((n, n))
        for j in range(n):
            dx[:, j] = (f(x + 1e-8 * np.eye(n)[:, j]) - fx) / 1e-8
        x_last =x
        x = x - np.linalg.solve(dx, fx)
        Newton_table.append([x, fx, x_last-x])
        if np.linalg.norm(fx) < e:
            return x, Newton_table , True
    return x, Newton_table, False
