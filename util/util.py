def derivative(dif, point, f, eps=0.0001):  # нам важен знак, большой esp приводит к нулю
    if dif == 0:
        return f(point)
    else:
        dif -= 1
        return (derivative(dif, point + eps, f) - derivative(dif, point, f)) / eps
